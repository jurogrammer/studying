# Prefer side-effect-free functions in streams

스트림은 처음 봤을 때 뭐가 좋아서 도입했는지 모를 수 있습니다. 하지만 스트림은 단순히 API가 아닌, 함수형 프로그래밍에 기초한 패러다임입니다.

이 패러다임을 그대로 받아들여야 표현력,속도, 병렬성까지 얻을 수 있죠.



## 핵심

스트림의 핵심은 계산을 일련의 변환(transformation)으로 재구성하는 부분입니다.

이때 각 변환 단계는 **순수함수**여야 합니다. 다시 말해서, parameter에 의해서만 output이 변경되어야 합니다. 또한 외부상태를 변경시켜서도 안되죠.



따라서 다음과 같은 코드는 stream을 잘못사용했다고 말할 수 있습니다.

### bad-case

```java
// Uses the streams API but not the paradigm--Don't do this!
Map<String, Long> freq = new HashMap<>();
try (Stream<String> words = new Scanner(file).tokens()) {
  words.forEach(word -> {
    freq.merge(word.toLowerCase(), 1L, Long::sum);
  }); 
}
```

forEach 스트림을 이용해서 freq Map을 변경시키고 있기 때문에 안좋은 코드라고 볼 수 있습니다.

loop문보다 길고, 읽기 어렵고, 유지보수에도 좋지 않기 때문이지요.



### good-case

```java
// Proper use of streams to initialize a frequency table
Map<String, Long> freq;
try (Stream<String> words = new Scanner(file).tokens()) {
  freq = words
    .collect(groupingBy(String::toLowerCase, counting()));
}
```

> tokens는 java9부터 지원해주는 stream으로 변환해주는 기능입니다. 이전 버전은 Stream.of를 사용하시기 바랍니다.

이와 같이 코드를 고치는 것이 좋지요. 외부 상태를 변경하지도 않았고, 짧아졌죠.



forEach문을 쓸때는 계산하는데는 쓰지마시고, 스트림 계산 결과를 보고할 때만 사용하시기 바랍니다.



## collector

위 코드에서는 collector라는 새로운 개념이 등장합니다. 스트림을 사용하려면 꼭 배워야 하는 개념이죠.

`java.util.stream.Collectors`에는 39가지의 메서드를 가지고 있습니다! 이중에는 input 파라미터가 5개인 메서드도 존재하죠. 덜덜합니다.

처음에 익숙해지기 전까지는 함수의 특징 그대로 블랙박스 모델로 이해하시는게 좋습니다.

단순히 reduction을 해주는 기능들이라고 보시면 됩니다. 즉, 하나의 개체로 모아주는 기능이라고 보라는 것이죠. 그리고 일반적으로 collector가 모아준 객체의 타입은 보통 Collection이 됩니다.

그래서 collector라는 네이밍이 명명된 것입니다.



### 종류

* toList()

* toSet()

* toCollection(collectionFactory)

  사용자 지정 Collection Type

이렇게 총 3가지가 되겠습니다.



### 사용 예제

앞서 배운 내용을 바탕으로 빈도 테이블에서 가장 빈도 수 높은 10개의 단어를 추출하는 예제를 작성해보겠습니다.

```java
// Pipeline to get a top-ten list of words from a frequency table
List<String> topTen = freq.keySet().stream()
  .sorted(comparing(freq::get).reversed())
  .limit(10)
  .collect(toList());
```

> toList()는 collectors의 method인데, static import하여 사용하는 것이 가독성에 좋습니다.



여기서 그나마 어려운 부분(tricky part)이라면 `comparing(freq::get).reversed()`가 되겠습니다.

comparing은 Item14에서 배웠듯, key extraction function을 받는 comparator construction method입니다.

key extraction function은 `freq::get`이 되겠습니다. 단어를 key로 하여 빈도표에서 추출합니다. 그리고 그 빈도를 반환하는 것이죠.

그리고 reversed를 통해 comparing을 역순으로 정렬합니다.



## 나머지 36가지

대부분 맵으로 취합하는 기능으로, Collection에 취합하는 것보다 훨씬 복잡합니다.  스트림의 원소는 키 하나, 값 하나에 연관되어 있습니다. 그리고 다수의 스트림 원소를 기준으로는 동일한 키에 연관있을 수도 있죠.

> 앞으로는 요약 설명하기 때문에 https://docs.oracle.com/javase/10/docs/api/java/util/stream/Collectors.html 를 보고 하나씩 짚어보시길 바랍니다.



### toMap

#### parameter가 2개

`toMap(keyMapper, valueMapper)`형태를 지닙니다. 스트림의 원소를 키, 값에 매핑하는 함수이지요.

```java
// Using a toMap collector to make a map from string to enum
private static final Map<String, Operation> stringToEnum =
  Stream.of(values()).collect(
  toMap(Object::toString, e -> e));
```

만약에 동일 key를 맵핑하려한다면 `IllegalStateException`이 발생합니다.



#### parameter가 3개

위와 같은  `IllegalStateException`에러를 피하기 위해 다양한 전략을 제공해줍니다.

그래서 병합 함수까지 제공하죠.

병합함수의 형태는 `BinaryOperator<U>`가 되며, U는 Map의 value Type입니다.

어떤 키와 그 키에 연관된 원소들 중 하나를 골라 연관짓는 맵을 만들 때 유용하죠.



예를 들어, 다양한 음악가의 앨범들을 담은 스트림을 가지고 음악가와 그 음악가의 베스트 앨범을 연관짓는다면 다음처럼 작성할 수 있습니다.

```java
// Collector to generate a map from key to chosen element for key
Map<Artist, Album> topHits = albums.collect( toMap(Album::artist, a->a, maxBy(comparing(Album::sales))));
```



또는 충돌이 나면 마지막 값을 취하는 collector를 만들때도 용이하죠

```java
// Collector to impose last-write-wins policy
toMap(keyMapper, valueMapper, (v1, v2) -> v2)
```



#### parameter가 4개

네번째 인수로 맵팩터리를 받아서 특정 맵 구현체를 만들 수 있습니다.



### groupingBy

input으로 분류함수를 받고, 출력으로는 원소들을 카테고리별로 모아 놓은 맵을 담은 수집기를 반환합니다.

#### parameter가 1개

```java
words.collect(groupingBy(word -> alphabetize(word)))
```



#### paramter가 2개

다른 타입의 value를 가지고 싶다면 2번째에 downstream 수집기를 명시해주면 됩니다. `toSet()`처럼 말이죠.

또는 counting()이란 메서드도 있는데, 원소의 개수가 값으로 매핑되죠.

```java
Map<String, Long> freq = 
  words.collect(groupingBy(String::toLowerCase, counting()));
```



#### parameter가 3개

Map factory도 지정할 수 있습니다. 하지만, 3개일 경우엔 telescoping argument list pattern에 어긋나 mapFactory 매개변수가 downStream 매개변수보다 앞에 위치하게 됩니다.



### joining

CharSequence instance의 스트림에만 적용할 수 있습니다.

파이썬의 join과 동일하다고 보면 됩니다.

#### 파라미터가 0개

 단순히 연결해주는 기능만 가지고 있습니다.

#### 파라미터가 1개

delimiter를 매개변수로 받을 수 있습니다. ','를 넣는다면 csv파일 형식으로 만들 수 있다는 뜻이죠.

#### 파라미터가 3개

prefix와 suffix도 받습니다. (prefix, delimiter, suffix)형태죠.





## 핵심 정리

1. 스트림 파이프라인 프로그래밍은 side effect가 없어야 합니다.
2. forEach는 결과 보고에만 써야 하며
3. 잘 사용하기 위해 collector를 알아두어야 합니다.
4. 가장 중요한 collector는 toList, toSet, toMap, groupingBy,joining입니다.