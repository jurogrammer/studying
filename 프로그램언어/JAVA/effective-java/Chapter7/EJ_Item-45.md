# Use streams judiciously

stream은 bulk operations의 부담을 줄이기 위해 Java 8에서 추가되었습니다.

이 API는 stream, stream pipeline이라는 2개의 핵심 abstraction을 제공해줍니다.



## StreamAPI

### 1. stream

* represents a finite or infinite sequence of data element
* stream이 될 수 있는 대상은 collections, arrays, file등등이 있습니다.



### 2. stream pipeline

#### 구성요소

##### source stream

* stream이 될 수 있는 요소로써, collections, arrays 등을 의미합니다.

##### intermediate operations

* 중간 operation을 의미합니다.
* 0개 이상의 중간 연산자가 있을 수 있습니다.
* 한 스트림을 다른 스트림으로 바꾸는 역할을 합니다. 동일 타입일 수도 있습니다.

##### terminal operation

* stream의 최종 연산에 해당합니다.
  * collection으로 elements를 반환하거나,
  * 특정 값 만을 반환하거나
  * 모든 elements를 출력합니다.



#### 특성

##### lazy evalulation

terminal operation을 만날때까지 평가되지 않습니다. silent no-op로 볼 수 있죠. 이러한 특성 덕분에 infinite streams도 처리할 수 있게 됬습니다.



##### fluent

가독성이 향상됩니다.



stream은 반드시 사용해야만 하는건 아니며, 작성 방법에 따라 가독성이 좋을 수도, 안좋을 수도 있습니다.



## 예제 - Anagram

아나그램 예제로 그 예를 알아보겠습니다.



아나그램이란, 문자는 같지만 배열이 다른 두 개의 문자열 관계를 의미합니다. abc acb는 아나그램이라 할 수 있죠. 이 예제에서는 

1. 정렬된 문자열을 key로, value를 해당 문자를 넣는 셋인 타입인 map을 구현하고, 
2. 사용자가 정한 문자열의 수 이내의 아나그램만 
3. 출력하는

코드를 구현하겠습니다.

loop

```java

// Prints all large anagram groups in a dictionary iteratively
public class Anagrams {
    public static void main(String[] args) throws IOException {
        File dictionary = new File(args[0]);
        int minGroupSize = Integer.parseInt(args[1]);
        Map<String, Set<String>> groups = new HashMap<>();
        try (Scanner s = new Scanner(dictionary)) {
            while (s.hasNext()) {
                String word = s.next();
                groups.computeIfAbsent(alphabetize(word),
                        (unused) -> new TreeSet<>()).add(word);
            }
        }
        for (Set<String> group : groups.values())
            if (group.size() >= minGroupSize)
                System.out.println(group.size() + ": " + group);
    }

    private static String alphabetize(String s) {
        char[] a = s.toCharArray();
        Arrays.sort(a);
        return new String(a);
    }
}
```

이 코드는 stream과 loop를 섞어서 가독성을 높혔습니다.



주목할만한 부분은 

1. `computeIfAbsent`입니다.

이 method는 java 8에서 추가되었으며 그 기능을 만약 키가 존재한다면, normal하게 add연산을 수행하고, key가 없다면, 해당 키를 생성한 뒤, lambda expression으로 생성한 value를 집어넣는 연산을 수행합니다.



2. `alphabetize`

   alphabetize helper method를 통해 가독성을 높혔죠.



### Steam지옥

```java

// Overuse of streams - don't do this!
public class Anagrams {
    public static void main(String[] args) throws IOException {
        Path dictionary = Paths.get(args[0]);
        int minGroupSize = Integer.parseInt(args[1]);
        try (Stream<String> words = Files.lines(dictionary)) {
            words.collect(
                    groupingBy(word -> word.chars().sorted()
                            .collect(StringBuilder::new,
                                    (sb, c) -> sb.append((char) c),
                                    StringBuilder::append).toString()))
                    .values().stream()
                    .filter(group -> group.size() >= minGroupSize)
                    .map(group -> group.size() + ": " + group)
                    .forEach(System.out::println);
        }
    }
}
```

위와 동일한 연산을 stream의 남용으로 구현한 예제입니다. 그나마 잘한 점은 try with resource statements를 통해 자동으로 자원 할당 해제를 도모했다는 점이죠.



또한, char stream에서 강제 형변환한 부분을 주목하시길 바랍니다. (`(sb, c) -> sb.append((char) c),`)

char stream은 타입을 char로 반환해줘야할 것 같지만, int로 반환합니다. 그렇기 때문에 char 타입으로 캐스팅해줘야 하지요.



### best

```java

// Tasteful use of streams enhances clarity and conciseness
public class Anagrams {
    public static void main(String[] args) throws IOException {
        Path dictionary = Paths.get(args[0]);
        int minGroupSize = Integer.parseInt(args[1]);
      
        try (Stream<String> words = Files.lines(dictionary)) {
            words.collect(groupingBy(word -> alphabetize(word)))
              .values().stream()
              .filter(group -> group.size() >= minGroupSize)
              .forEach(g -> System.out.println(g.size() + ": " + g));
        }
    }
    // alphabetize method is the same as in original version
}
```

try-with-resource를 썼을 뿐만 아니라, 모두 stream으로 간결하게 표현했죠.



#### 이름은 신중하게

stream에서는 lambda expression을 사용하기 때문에 변수명을 신중히 짓는 것이 중요합니다. 이전 장과 동일한 말이죠.

따라서 words, groupd이란 파라미터명으로 이름을 변경하였습니다.





## stream vs loop

stream을 처음보면, 기존에 작성되었던 loop문을 모두 stream으로 변경하고 싶은 욕구가 들것입니다. 하지만, stream이 만능은 아니며 stream으로 대체하기 어려운 loop의 이점이 있습니다.



### loop가 좋은 경우

* local variable을 읽거나 수정할 수 있습니다. 이와 달리 lambdas는 마지막 변수만 읽을 수 있죠. 그리고 local variable을 수정할 수도 없습니다.
* code block에서 return하거나 break하거나 continue하거나 에러까지 던질 수 있죠. 람다는 이중에서 하나도 못합니다.

### stream이 좋은 경우

* sequence of elements를 통일성 있게 변경할 경우

* sequence of elements를 필터링할 경우

* sequence of elements를 단일 op를 통해 combine할 경우

  ex:) add them, concatenate them, 최소 값을 구할 때

* 누적된 sequence of elements를 collection에 저장하고 싶을 때. 

  ex:) 특정 원소로 grouping하기

* 특정 기준에 부합하는 sequence of elements를 찾을 때





### stream으로 하기 정말 어려운 것

pipeline의 여러 스테이지의 원소를 동시에 접근할 수 없습니다. 다시 말해서, 다른 하나의 스트림 값을 선택하면 다른 스트림은 잃게 되죠.

어떻게든 자료구조를 구현하려고 하면 코드가 더러워질 뿐입니다. 그래도 정~ 구하고 싶다면 역 연산을 취하세요. 다음 메르센 소수가 그런 예제입니다.

#### 예제 - 메르센 소수

메르센 **숫자**란, 2^p - 1 의 수를 의미합니다. 여기서, p가 소수면 이 메르센 수도 소수가 될 수 있죠. 만약 그렇다면 그 소수를 메르센 **소수**라고 부릅니다.



infinite stream을 고려해봅시다. primes() method가 그런 예제이지요. (그리고 가독성을 위해 stream은 복수로 지읍시다.)

```java
 static Stream<BigInteger> primes() {
       return Stream.iterate(TWO, BigInteger::nextProbablePrime);
}

```

Stream.iterate(TWO, BigInteger::nextProbablePrime); 는 2가지 parameter를 받습니다. 하나는 stream의 첫번째 수이며, 다른 하나는 스트림에서 이전 element로부터 다른 element를 생성하는 function입니다.



이 코드는 20개의 메르센 수를 반환하는 예제입니다.

```java
public static void main(String[] args) {
       primes().map(p -> TWO.pow(p.intValueExact()).subtract(ONE))
           .filter(mersenne -> mersenne.isProbablePrime(50))
           .limit(20)
           .forEach(System.out::println);
}
```

여기서 매직넘버 50은 seed number로 보시면 됩니다.



이제, p로 무언가 작업을 하자고 합시다. 이 값 p는 처음에만 나타나고 종단 부분에선 access할 수 없습니다. 앞서 말했듯이, stream에서는 이 p에 접근하기 어려우나, 이 예제에서는 연산으로 p를 구하기 쉽기 때문에 p에 접근할 수 있게 되죠.

2*p - 1은 p의 bit 길이를 의미합니다. 즉, 메르센 소수의 bit길이가 곧 p가 됩니다.

```java
.forEach(mp -> System.out.println(mp.bitLength() + ": " + mp));
```



다시 말하자면, terminal에서 처음 input에 접근하기 어려우니 쉽게 가능하다면 위처럼 우회해서 접근하라는 예제입니다.



### stream이 좋을 지, loop가 좋을지 애매한 경우 - 데카르트 곱

뭐가 더 나은지 애매할 때가 있습니다. 둘 다 읽기 쉬워보이죠. 카테시안 곱(데카르트 곱)예제로 살펴보겠습니다.



모양, 숫자를 지닌 모든 종류의 카드를 생성하는 예제입니다. 이때, 모양별, 숫자별 모든 모양을 만들어야 합니다. 이걸 집합에서 수학적인 용어로 카테시안 곱이라고 부르죠.



##### loop version

```java
// Iterative Cartesian product computation
private static List<Card> newDeck() {
  List<Card> result = new ArrayList<>();
  for (Suit suit : Suit.values())
    for (Rank rank : Rank.values())
      result.add(new Card(suit, rank));
  return result;
}
```

딱봐도 가독성에 문제가 없죠? 읽기 괜찮구요.



##### stream version

```java
// Stream-based Cartesian product computation
private static List<Card> newDeck() {
  return Stream.of(Suit.values())
    .flatMap(suit ->
             Stream.of(Rank.values())
             .map(rank -> new Card(suit, rank))) .collect(toList());
}
```

이것도 읽기 쉬우신가요? 그렇다면 stream에 익숙하신 분입니다. 그렇지 않은 분들은 이 코드가 어렵게 느껴지실 수 있죠.

애매할 땐 loop문으로 작성하시는게 좋습니다. 일반적으로 이해하기 쉬우니까요.

