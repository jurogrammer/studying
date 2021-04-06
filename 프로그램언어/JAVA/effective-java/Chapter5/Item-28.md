# Prefer lists to arrays

List와 array는 타입에 관해 차이점이 존재합니다. 그리고 이 차이점에서 list가 type safe합니다. 따라서 이번 아이템에서는 list와 array의 차이점을 알아보고, array를 list로 변환하는 과정을 소개하겠습니다.



# 차이점

### 1. array는 covariant입니다.

covariant란, 만약에 Sub가 Super의 서브타입이라면, Sub[] 또한 Super[]의 Sub type이라는 뜻입니다.

이에 반면, Generic은 incovariant라고 부르죠. Type1과 Type2가 있다면, List\<Type1> List\<Type2>는 어떤 관계를 가지지 않습니다.

이 차이로 인해 각각 런타임, 컴파일에 타입 체크를 합니다.



#### array

runtime에 TypeCheck

```java
Object[] objectArray = new Long[1];
ObjectArray[0] = "I don't fir in";
```



#### List

compileTime에 TypeCheck

```java
//Won't compile!
List<Object> ol = new ArrayList<Long>();
ol.add("I don't fit in");
```



### 2. array는 reified합니다.

reified란, array는 런타임 중에 자신의 타임을 알고 그 타입을 강제하는 것을 의미합니다.

> reified: <추상 개념 등을> 구체화하다, 구체화하여 생각하다.



#### array

```java
Object[] objectArray = new Long[1];
ObjectArray[0] = "I don't fir in";
```

이 예제에서 보면, ObjectArray[0]은 자신의 타입이 Long이라는 것을 알기 때문에 런타임 중에  string을 집어넣으려고 하면 에러를 발생시키죠.



#### List

그에 반면, Generics는 런타임 중 자신의 타입을 지워버립니다! 런타임 중 자신의 타입을 기억하는 array와 매우 대조적이죠. 따라서 Generics는 타입 안정성을 컴파일 타임에 체크합니다.



# generic을 array로 선언 금지

위 두 중대한 차이점 때문에 섞어쓰면 문제가 됩니다.

```java
new List<E>[], new List<String>[], new E[]
```

따라서 같은 것들을 사용할 수 없게 막아놨습니다. 이들은 컴파일 타임에 error를 발생시키죠.



### 컴파일 타임에 막아놓은 이유

간단히 말해서 typesafe하지 않기 때문입니다.

다음 예를 보면 절실히 드러나죠.

```java
List<String>[] stringLists = new List<String>[1]; // (1)
List<Integer> intList = List.of(42); // (2)
Object[] objects = stringLists; // (3)
objects[0] = intList; // (4)
String s = stringLists[0].get(0); // (5)
```



 문제 되는 부분은 바로 (4)입니다.

objects는 array의 covariant성격 때문에  (3)에서 `List<String>`이 되었는데, generic은 런타임 중 parameterized type을 erase하니까 `List`가 되어 `List<Integer>`가 이상없이 담기게 됩니다.

결국 런타임 중 (5)에서 ClassCastException이 발생합니다. 따라서 이를 막기 위해선 제너릭 array를 선언하지 못하도록 해야죠.



### non-reifiable types

따라서 generics 애들은 실행중 타입이 지워지므로, 정보를 덜 가지고 있게 되죠. 오직 unbounded wildcard types만이 reifiable합니다. ex:)`List<?>` , `Map<?,?>`

unbounded wildcard types는 사용할 일이 거의 없습니다.



### generic을 array로 선언 할 수 없는 문제에서 따라오는 번거로움

1. 일반적으로 generic collection은 자신의 element에 대한 array를 반환하는 것이 어렵습니다.

2. varargs method와 같이 사용하면 혼동됩니다.

   varargs method를 호출하면 가변인수 매개변수를 받을 배열이 선언되는데 여기에 non-refiable 타입이면 경고가 발생하죠. (`@SafeVarargs`로 대체 가능합니다.)



# array를 List로 변경하기

배열로 형변환시 `generic array creation`에러나 `unchecked cast`경고가 뜬다면 `E[]`보다는 `List<E>`를 사용하는게 좋습니다.

비록 코드가 복잡해지고 성능이 좀 나빠지지만 타입 안전성와 interoperability는 좋아지니까요.



### 예시 - Chooser

```java
public class Chooser {
  private final Object[] choiceArray;
  
  public Chooser(Collection choices) {
    choiceArray = choices.toArray();
  }
  
  public Object choose() {
    Random rnd = ThreadLocalRandom.current();
    return choiceArray[rnd.nextInt(choiceArray.length)];
  }
}
```



#### 문제점

1. 매 method 호출시 casting을 해주어야 합니다.
2. 잘못된 타입을 넣을 경우 `ClassCastingException`이 발생하죠.



따라서 다음처럼 Generic으로 바꾸어 보겠습니다.

#### 수정 1. - Generic으로 변경

```java
public class Chooser<T> {
  private final T[] choiceArray;
  
  public Chooser(Collection<T> choices) {
    choiceArray = choices.toArray();
  }
  
  // choose method unchanged
}
```





```java
choiceArray = choices.toArray();
														 ^
java: incompatible types: java.lang.Object[] cannot be converted to T[]
```

와 같은 에러가 발생합니다. 이는 단순히 다음과 같이 casting해주면 해결 됩니다.



#### 수정2. - casting

```java
public class Chooser<T> {
  private final T[] choiceArray;
  
  public Chooser(Collection<T> choices) {
    choiceArray = (T[]) choices.toArray();
  }
  
  // choose method unchanged
}
```

이와 같이 캐스팅하면 Type이 안전하지 않다는 경고가 발생합니다. T가 제너릭 타입이므로 런타임시 원소 타입이 지워지니까요.



비검사 형변환 경고를 제거해주기 위해선, compile time에 Type을 check해주는 List를 써주면 됩니다. array쓰지 마시구요. 따라서 다음과 같이 코드를 변경할 수 있습니다.



#### 수정3. - array to List

```java
public class Chooser<T> {
  private final List<T> choiceArray;
  
  public Chooser(Collection<T> choices) {
    choiceArray = new ArrayList<>(choices);
  }
 
  public T choose() {
    Random rnd = ThreadLocalRAndom.current();
    choiceArray.get(rnd.nextInt(choiceList.size()));
  }
}
```



코드 양이 늘었고, 조금 더 느리지만, 런타임 중 ClassCastException을 발생시키지 않으므로 가치가 있는 코드라 할 수 있습니다.