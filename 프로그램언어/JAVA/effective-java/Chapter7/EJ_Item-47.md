# Prefer Collection to Stream as a return type

Java 8 이전에 elements sequence를 반환하는 메서드들을 많이 봤을 겁니다.

Collection, Set, List같은 Collection interface와 Iterable, arrays등 말이죠.



기본적으로는 Collection으로 반환하고,

Collection으로 구현할 수 없거나 for-each에서만 쓰인다면 Iterable을 구현하고

성능 향을 기대한다면 arrays를 썼겠죠.



하지만! Stream이 등장함으로써 상황이 좀 더 복잡한 양상을 띄게 되었습니다.



## Stream

stream은 앞서 봤 듯, iteration을 지원하지 않죠. 그래서 for-each문을 쓰고 싶은 사람의 기대는 만족시킬 수 없습니다.

> 한편으로, stream은 iteration의 기능을 다 포함하는데, 사용못하는 이유는 단순히 extends하지 않아서입니다.



### interation 우회하는 방법

#### 방법1 - iterator method

```java
// Won't compile, due to limitations on Java's type inference
for (ProcessHandle ph : ProcessHandle.allProcesses()::iterator) { // Process the process
}
```

타입을 추론하지 못하여 컴파일타임 에러가 발생합니다.

```
Test.java:6: error: method reference not expected here
for (ProcessHandle ph : ProcessHandle.allProcesses()::iterator) {
												^
```



#### 방법2 - Casting

```java
// Hideous workaround to iterate over a stream
for (ProcessHandle ph : (Iterable<ProcessHandle>)
     ProcessHandle.allProcesses()::iterator)
```

딱봐도 난잡하고 직관성이 떨어지죠...



#### 방법3 - adapter method

```java
// Adapter from  Stream<E> to Iterable<E>
public static <E> Iterable<E> iterableOf(Stream<E> stream) {
  return stream::iterator;
}
```

adapter 메서드를 구현하면 됩니다. 이렇게 하면 타입추론을 잘 하죠

```java
for (ProcessHandle p : iterableOf(ProcessHandle.allProcesses())){
  
}
```



#### stream - iteration

stream,  iteration를 반환하는 케이스와 동일한 맥락으로 사용방법을 바꾼것입니다.

Files.lines는 모든 예외를 처리해줘서 우수하나, for-each는 처리하기 어려워지죠. 그렇다고 for-each만 반환하도록 한다면 stream 사용자가 난감하겠죠?

그래서 보통 public API를 만들 때는 어댑터로 두 가지 모두 사용할 수 있도록 마련해주는게 좋습니다.



Collection interface는 Iterable의 subclass여서 loop문에 사용할 수 있을 뿐만 아니라 .stream()을 통해 stream api를 지원해줍니다. 따라서 public API에서는 Collection을 구현하도록 하는게 좋겠지요. 이미 두 가지 지원해주도록 하는 클래스니까요.



##  Iteration 구현

### 주의점

Collection을 반환한다는 이유로 매우 큰 시퀀스를 메모리에 할당해서는 안됩니다.

sequence가 크지만, 표현을 간결하게 할 수 있으면 전용 컬렉션을 구현하는 것도 좋은 방안입니다.



### 부분집합 예제

집합의 원소 갯수가 n개일 때 부분집합의 갯수는 2^n 개가 되므로 Collection으로 무작정 반환하는 건 큰 문제가 되겠지요.

AbstractList를 구현하면 전용컬렉션을 쉽게 구현할 수 있습니다.

비트벡터를 이용하면 되는 것이지요.

```java
// Returns the power set of an input set as custom collection
public class PowerSet {
  public static final <E> Collection<Set<E>> of(Set<E> s) {
    List<E> src = new ArrayList<>(s);
    if (src.size() > 30)
      throw new IllegalArgumentException("Set too big " + s); return new AbstractList<Set<E>>() {
      @Override public int size() {
        return 1 << src.size(); // 2 to the power srcSize
      }
      @Override public boolean contains(Object o) {
        return o instanceof Set && src.containsAll((Set)o);
      }
      @Override public Set<E> get(int index) {
        Set<E> result = new HashSet<>();
        for (int i = 0; index != 0; i++, index >>= 1)
          if ((index & 1) == 1)
            result.add(src.get(i));
        return result;
      }
    }; }
}
```

> 한편으로, 입력집합 원소의 수가 30개가 넘으면 Exception을 던지도록 하였습니다. Int의 크기는 2^31-1 로 제한되니까요. 
>
> Collection 명세에는 컬렉션이 엄청 크고, 무한일 때 2^31-1을 반환하라고 되있지만, 나이스한 방법은 아니라고 생각합니다.



### Abstraction collection

AbstractionCollection을 이용해 Iteration을 구현할 땐 contains, size만 더 구현하면 됩니다. 

만약에 반복 시작 전 시퀀스 내용을 확신할 수 없을 땐 contains, size를 구현할 수 없으므로 stream이나 Iterable을 반환하도록하죠.



## Stream 구현

동일한 문제를 스트림으로 구현해보겠습니다.

약간의 통찰력...?만 있으면 된답니다.

{a,b,c}의 부분집합에 대하여

prefix: 첫 번째 원소를 포함하는 부분리스트 ex:) {a},{a,b}, {a,b,c}

suffix: 마지막 원소를 포함하는 부분리스트 ex:) {abc},{b,c},{c}

여기서, 어떤 리스트의 부분리스트는 단순히 그prefix + suffix + {} or suffix + prefix + {} 의 조합이 됩니다.



```java
// Returns a stream of all the sublists of its input list
public class SubLists {
  public static <E> Stream<List<E>> of(List<E> list) {
    return Stream.concat(Stream.of(Collections.emptyList()),
                         prefixes(list).flatMap(SubLists::suffixes));
  }
  
  private static <E> Stream<List<E>> prefixes(List<E> list) {
    return IntStream.rangeClosed(1, list.size())
      .mapToObj(end -> list.subList(0, end));
  }
  
  private static <E> Stream<List<E>> suffixes(List<E> list) {
    return IntStream.range(0, list.size())
      .mapToObj(start -> list.subList(start, list.size()));
  }
}

```





## 전용 Collection 사용 이점

(조슈아씨 컴퓨터 환경)

loop 문을 써야하는 상황에서 stream을 Iterable로 반환해주는 어댑터를 구현하면 2.3배 느려지고, 클라이언트 코드가 어수선해집니다. 

전용 컬렉션을 사용하면 1.4배가 빨라지죠.

