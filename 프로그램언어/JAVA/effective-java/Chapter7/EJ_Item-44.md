# Favor the use of standard functional interfaces

lambdas가 추가되면서 template method pattern은 덜 사용하게 되었습니다. 현대적인 대안은 동일한 효과를 얻을 수 있는 function object를 static factory나 constructor에서 제공하는 것이지요. 다시 말해서 function을 파라미터로 받는 것입니다.



# 예제 - LinkedHashMap

### cache로써 사용하기

`removeEldestEntry`를 overriding함으로써, cache의 자료구조로 쓸 수 있죠. 

작동방식은 다음과 같습니다.

1. 새로운 값을 집어넣을 때마다 이 메서드가 실행되고 
2. true값을 반환하면, 가장 오래된 값을 삭제합니다.



이를 구현한 코드는 다음과 같습니다.

```java
protected boolean removeEldestEntry(Map.Entry<K,V> eldest) {
  return size() > 100;
}
```



### 위 메소드가 현대적으로 재작성된다면...?

현대적으로라면, 앞서 말했듯이 function object를 받는 static factory나 constructor를 이용할 수 있겠습니다. 하지만 이를 단순히 사용하기엔 어렵습니다.

1. size()는 instance method이기 때문에 가능했지만,
2. lambdas를 사용할 여지가 없지요. factory나 constructor가 생성되기 전에는 map이 존재하지 않으니까요.

따라서 위 부분을 고려하여 functional Interface를 작성하면 다음처럼 작성할 수 있습니다.

```java
// Unnecessary functional interface; use a standard one instead.
   @FunctionalInterface interface EldestEntryRemovalFunction<K,V>{
       boolean remove(Map<K,V> map, Map.Entry<K,V> eldest);
}
```

remove라는 instance method를 가진 Functional interface입니다. parameter로 초기화된 map과 오래된 entry를 받아서 삭제하는 기능을 가진 function을 선언할 수 있습니다.

### but, bad~

하지만~ 이 장의 제목에서 알 수 있듯이, 특수한 연산을 위해 위처럼 Function을 선언할 필요가 없습니다. 대신 `java.util.function` package에 있는 standard functional interfaces를 사용하시면 됩니다.



### standard interface를 사용해야 하는 이유

#### 1. 작성한 API를 다른 사람이 배우기 더 쉽습니다.

위 처럼 특수한 함수를 작성한 배경을 알 필요가 없어지기 때문입니다.

#### 2. 유용한 default method를 제공해줍니다.



### 개선

standard functional interface인 BiPredicate Functional interface를 통해서 아래처럼 간단히 작성할 수 있습니다.

```java
BiPredicate<Map<K,V>, Map.Entry<K,V>>
```

![스크린샷 2021-03-08 오후 10.13.12](/Users/ju/Library/Application Support/typora-user-images/스크린샷 2021-03-08 오후 10.13.12.png)



> 한편으로, funtion을 사용하는 것에  어색함을 계속 느꼈는데, 왜 그런지 이제야 알았습니다. 보통, class를 작성할 때 기능이 완성되는 반면에, lambdas를 받는다면 최종적인 구현은 paramter로 전달받은 lambdas 구현에 달려있습니다. 그래서 어색했던 것 같네요.



# standard interface의 종류

허허... 엄청 많이 있습니다.

![스크린샷 2021-03-08 오후 10.23.18](/Users/ju/Library/Application Support/typora-user-images/스크린샷 2021-03-08 오후 10.23.18.png)

### 1. primitive type

기본 타입인 int, long, double 각각 3개의 변형

ex:) Predicate -> IntPredicate

### 2. nine edditional variants of the Function interface

input, output의 타입이 동일한 function -> UnaryOperator

변형: SrcToResult형식 ex:)long->int면, LongToIntFunction

### 3. two-argument versions of three basic functional interfaces

인수 2개씩 받는 경우, 

그리고 2개씩 받고 다시 기본형을 반환하는 경우

### 4. BooleanSupplier interface

boolean 반환하는 함수



# 주의사항들

### 1. Boxed primitives를 쓰지마세요

Function들은 primitive type을 지원하므로 boxed primitives를 쓰지 않도록 합시다.

![스크린샷 2021-03-08 오후 10.43.52](/Users/ju/Library/Application Support/typora-user-images/스크린샷 2021-03-08 오후 10.43.52.png)

![스크린샷 2021-03-08 오후 10.44.05](/Users/ju/Library/Application Support/typora-user-images/스크린샷 2021-03-08 오후 10.44.05.png)



### 2. 동일한 Input, output을 가짐에도 standard functional interface대신 다른 인터페이스를 두는 경우

`Comparator<T>`의 경우, `ToIntBiFunction<T, T>` 와 동일한 구조를 지니고 있습니다. 하지만, Comparator를 사용하는 이유는 다음과 같습니다.

1. 이름이 매우 설명력이 있으므로
2. Comparator와 관련된 아주 강력한 규약이 존재하므로
3. 유용한 custom default method를 제공하므로



위의 경우가 아니라면 standard functional interface를 사용하시기 바랍니다.



### 3. @FunctionalInterface 를 달아주세요

`@Override` 와 동일한 이유입니다. FunctionalInterface 어노테이션을 달아줌으로써 관련된 규약을 지키고 있는지를 컴파일 타임에 알아차릴 수 있죠.



### 4. functional interface를 사용하는 API에서 이해하기 어려운 메서드를 오버로딩하지 마세요.

이해하기 어려운 메서드란, 파라미터의 순서쌍이 동일하면서 FunctionalInterface는 다른 경우를 말합니다. 이렇게 작성하면 클라이언트가 이해하기 어려우므로 지양하시길 바랍니다.