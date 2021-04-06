# Favor generic methods

class가 generic이 될 수 있는 것 처럼, method또한 generic이 될 수 있습니다. 대부분의 Static utility methods는 generic으로 선언되어 있으며, 심지어 Collections에 있는 모든 algorithms는 generic으로 되어 있죠.



generic method를 만드는 것은 generic types를 만드는 것과 유사합니다. Set 예제를 통해 변환해보겠습니다.

# 예제 - Set

### 코드

Set에서 두 Set을 받아 union한 뒤 그 Set을 반환하는 예제입니다.

```java
public static Set union(Set s1, Set s2) {
  Set result = new HashSet(s1);
  result.addAll(s2);
  return result;
}
```

이 코드는 RawType을 사용하고 있습니다. 



### 실행

이 메서드를 컴파일하면 다음과 같은 경고 문구가 출력됩니다.

![스크린샷 2020-12-23 오후 8.33.42](/Users/ju/Desktop/스크린샷 2020-12-23 오후 8.33.42.png)

```
Union.java:5: warning: [unchecked] unchecked call to HashSet(Collection<? extends E>) as a member of raw type HashSet
           Set result = new HashSet(s1);
                        ^
```

![스크린샷 2020-12-23 오후 8.34.29](/Users/ju/Desktop/스크린샷 2020-12-23 오후 8.34.29.png)

```
Union.java:6: warning: [unchecked] unchecked call to
addAll(Collection<? extends E>) as a member of raw type Set
result.addAll(s2);
						 ^
```



모두 RawType을 사용하고 있어 위와 같은 경고 메시지를 보여주는 것이죠.



### 핵심

warings를 제거하고, method를 type safe하기 위해 3가지 선언을 유심히 봐야 합니다.

input parameter에 해당하는 s1,s2 그리고 output parameter에 해당하는 result죠. 이 세가지는 RawType으로 선언되있기 때문에 type safe하지 않습니다.



### 문법(syntax)

type parameter 선언 위치는 method의 `modifier`와 `return type` 사이에 두어야 합니다.

```
public <E> Set<E> union...
```

처럼 말이죠!



### Generic화

앞서 말씀드린 RawType으로 선언된 3가지가 문제이므로, 해당 RawType을 E로 제너릭화 해주면 됩니다. 따라서 아래와 같이 변경할 수 있죠.

```java
// Generic method
public static <E> Set<E> union(Set<E> s1, Set<E> s2) {
  Set<E> result = new HashSet<>(s1);
  result.addAll(s2);
  return result;
}
```



이제 이 method는 어떤 경고와 에러를 출력하지 않습니다.

```java
public static void main(String[] args) {
  Set<String> guys = Set.of("Tom", "Dick", "Harry");
  Set<String> stooges = Set.of("Larry", "Moe", "Curly");
  Set<String> aflCio = union(guys, stooges);
  System.out.println(aflCio);
}
```

그리고 casting 또한 필요없게 됬죠.



### 한계점

위 method는 3가지 타입들의 Set이 동일한 타입이여야만 합니다. 따라서 이러한 제한사항을 완화하기 위해 ***bounded wildcard types***를 적용할 수 있죠(Item-31)



# generic singleton factory

때때로 immutable 객체에 대해 여러 다른 타입을 적용해야할 때가 있습니다.

이는 generic의 타입이 제거 되므로 어떤 타입으로 매개변수화가 가능합니다. 그리고 이를 위해 요청 타입에 맞춰 바꿔줄 수 있는 static factory method도 선언되어야 하죠.

이런 패턴을 ***generic singleton factory***라 부릅니다.



예:)

```
Collections.reverseOrder, Collections.emptySet
```



### 예제 - identity function dispenser

* identity function은 stateless이기 때문에 한 번만 생성되도록 합니다.

  만약에 Generic이 reifiable하다면, type별로 identity function이 필요하겠지만 타입이 지워져서 singleton으로도 충분합니다.

```java
//Generic singleton factory pattern
private static UnaryOperator<Object> IDENTITY_FN = (t) -> t;

@SuppressWarnings("unchecked")
public static <T> UnaryOperator<T> identityFunction() {
  return (UnaryOperator<T>) IDENTITY_FN;
}
```

casting하면 unchecked warnings가 발생합니다. 

#### 증명

identity function은 argument가 수정되지 않고 반환되는 것을 알고 있습니다. 따라서 T 타입을 받으면 T 타입으로 반환되리라 확신할 수 있죠. 따라서 `@SuppressWarnings("unchecked")`을 달아주도록 합시다.



#### 이용

```java
    public static void main(String[] args) {
        String[] strings = { "jute", "hemp", "nylon" };
        UnaryOperator<String> sameString = identityFunction();
        for (String s : strings)
            System.out.println(sameString.apply(s));

        Number[] numbers = { 1, 2.0, 3L };
        UnaryOperator<Number> sameNumber = identityFunction();
        for (Number n : numbers)
            System.out.println(sameNumber.apply(n));
    }
```

casting이 없고, errors와 warnings없이 compile이 가능합니다!



# recursive type bound

드물게, 선언한 type parameter로 type parameter의 경계를 제한해야할 때가 있습니다. 이러한 방법을 recursive type bound라 부르죠.



### 예제 - Comparable interface

자연 순서가 있을 경우 비교 가능하도록 해주는 interface입니다.

```java
public interface Comparable<T> {
  int compareTo(T o);
}
```

T의 비교대상은 `Comparable<T>`를 구현한 타입 T죠.

보통 동일 타입에 대해서 비교합니다. String은 `Comparable<String>`, Integer은 `Comparable<Integer>`가 되겠습니다.



#### Collection 내 원소들의 비교

* 많은 메서드들이 정렬하고, 최대 최소 등을 구하기 위해 Comparable을 구현한 원소를 지닌 Collection을 받습니다. 
* collection내 원소들은 모두 서로 비교가능해야 합니다. 다시 말해서 mutually comparable 해야죠.



이러한 제약 사항을 다음과 같이 표현할 수 있습니다.

```java
//Using a recursive type bound to express mutual comparability
public static <E extends Comparable<E>> E max(Collection<E> c);
```

`<E extends Comparable<E>>`:  모든 타입 E는 자기 자신과 비교 가능해야 한다! 라고 해석 할 수 있습니다.

mutually comparability와 딱 들어맞는 notion이라 할 수 있죠.



#### 적용

```java
// Returns max value in a collection - uses recursive type bound
public static <E extends Comparable<E>> E max(Collection<E> c) {
  if (c.isEmpty())
    throw new IllegalArgumentException("Empty collection");
  E result = null;
  for (E e : c)
    if (result == null || e.compareTo(result) > 0)
      result = Objects.requireNonNull(e);
  return result;
   }
```

> 이 예제는 비어있을 경우 exception을 던지기 때문에 Optional<E>를 반환하도록 대체할 수 있습니다.(Item-55)



Recursive type bound는 복잡하지만, 사용하는 경우가 드뭅니다. 앞서 배운 simulated self-type idiom(item-02), 지금 배우는 내용 그리고 wildcard variant(Item-31)을 안다면 실전은 거의 정복했다고 볼 수 있습니다.

