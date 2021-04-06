# Use bounded wildcards to increase API flexibility

### List와 불공변(invariant)

`List<Object>` `List<String>`을 보면 직관적으로는 공변이여야 할 것 같습니다. 하지만, 다음 예를 보시면 불공변이여야 함이 명확합니다.



`List<Object>`에 어떤 객체든지 넣을 수 있습니다. 이때, 공변이여야 한다면 Object의 하위 타입인 String의 List에 대해서도 동일하게 어떤 객체든지 넣을 수 있어야 겠지요? 왜냐하면 LSP를 따라야 하니까요.



하지만, `List<String>`엔 문자열만 넣을 수 있으므로 LSP를 위배하게 됩니다.



코드를 작성하다보면 직관적으로 떠올렸던 유연한 방식을 실행해 줄 무언가가 필요합니다.(불공변은 유연하지 못하다 말할 수 있습니다.) 다음 예를 보시죠.



# 예제 - Stack class

### 코드

 ```java
public class Stack<E> {
  public Stack();
  public void push(E e);
  public E pop();
  public boolean isEmpty();
}
 ```



### 문제점1. pushAll method

elements의 나열을 받아 stack에 모두 넣는 메서드를 생각해봅시다. 다음과 같이 코드를 작성해볼 수 있겠죠?

```java
public void pushAll(Iterable<E> src) {
  for (E e : src)
    push(e);
}
```

이 메서드는 다음 상황에서 문제가 발생하죠

```java
Stack<Number> numberStack = new Stack<>();
Iterable<Integer> integers = ...;
numberStack.pushAll(integers);
```

Stack에 Number type을 받을 수 있도록 선언했으니, Integer도 넣을 수 있어야 할 것 아닌가요? 

하지만, `Stack<Number>`가 지닌 pushAll method는 **invariable하므로 오로지 Number만** 받을 수 있습니다! 따라서 다음과 같은 경고를 출력하죠

```
StackTest.java:7: error: incompatible types: Iterable<Integer>
   cannot be converted to Iterable<Number>
           numberStack.pushAll(integers);
                               ^
```





### 해결

bounded wild card -> `<? extends E>`사용하면 됩니다.

해석은 다음과 같이 됩니다.`Iterable인데, E의 subtype을 받는다.` (`Iterable of some subtype of E`)

```java
public void pushAll(Iterable<? extends E> src) {
  for (E e : src)
    push(e);
}
```



> 아마 넣을 수 있는 이유는 내부적으로는 공변타입인 array로 구현되어 있기 때문에 서브클래스를 넣을 수 있지 않는가 합니다.



### 문제점2. popAll

stack에서 elements들을 일일이 빼내어 주어진 collection에 담는 method를 생각해봅시다. 그렇다면 또 다음과 같지 작성할 수 있을 겁니다.

```java
public void popAll(Collection<E> dst) {
  while (!isEmpty())
    dst.add(pop());
}
```



위와 비슷한 문제로, 동일한 Type의 Stack에서 collection에 넣는 과정은 문제가 없겠지만 collection에 넣는 타입이 달라지면 문제가 되죠. 아래 코드를 보세요

```java
Stack<Number> numberStack = new Stack<>();
Collection<Object> objects = ...;
numberStack.popAll(objects);
```

Collection이 Object 타입을 가지므로 하위타입인 Number를 넣을 수 있어야할 것 같지만, 역시 불공변이기 때문에 에러가 발생합니다.



### 해결 

bounded wild card -> `<? super E>`사용하면 됩니다. `E의 부모 타입을 가진 collection이다`라고 해석되죠.(collection of some supertype of E)

생각해보면 push와는 상황이 역전됬죠. Stack에 input parameter를 넣는게 아니고, stack에 있는 값들을 collection에 넣어줘야 하니까요.

그러니 Stack보다는 collection이 super type이어야 겠지요?



```java
public void popAll(Collection<? super E> dst) {
  while (!isEmpty())
    dst.add(pop());
}
```





결론은 다음과 같습니다. 

**유연성을 증대시키기 위해선, 생산자 또는 소비자를 나타내는 input parameter에 wild tpyes를 사용하라!**

다음과 같은 공식을 유도할 수 있습니다.

### 공식: PECS

**producer-extends, consumer-super**

* parameterized type T가 producer를 의미한다면, `<? extends T>`
* parameterized type T가 consumer를 의미한다면, `<? super T>`

를 작성해주면 됩니다!

> 여기서 T는 변경하기 전 T로 보시면 될 것 같습니다. <? extends T>에서 T는 Stack의 타입이 되는데, 여기서 Stack은 consumer역할이 되버리니까요. 
>
> 따라서 절차적으로 생각한 것 같습니다. Iterable<T> src => Iterable<? extends T> src



* pushAll에선 src 매개변수가 Stack이 사용할 E 인스턴스를 생산하니까 `Iterable<? extends E>`가 된 것이고,
* popAll에선 dst 매개변수가 Stack으로부터 E instance를 소비하므로 `Collection<? super E>`가 됩니다.





# 기존 코드 리팩토링

### 1. Chooser (Item-28)

```java
public class Chooser<T> {
	private final T[] choiceArray;
	public Chooser(Collection<T> choices) { 
    choiceArray = choices.toArray();
	}
       // choose method unchanged
}
```

여기서 Chooser constructor에 있는 choices는 type T인 값을 공급해주고 있습니다. 따라서 다음과 같이 Chooser가 개선되야겠지요.

```java
public Chooser(Collection<? extends T> choices)
```

 



### 2. Set (Item-30)

```java
public static Set<E> union(Set<E> s1, Set<E> s2) {
       Set<E> result = new HashSet(s1);
       result.addAll(s2);
       return result;
}
```

s1 과 d2가 E를 생산하므로 코드는 다음과 같이 변경되어야 합니다.

```java
public static Set<E> union(Set<? extends E> s1, Set<? extends E> s2)
```



#### 주의사항

##### 반환 타입에는 bounded wild card 사용 금지

와일드 카드를 적용하면 유연성은 고사하고 client코드에서 wildcard types로 캐스팅 해주어야 합니다.



### 3. max (Item-30)

```java
public static <E extends Comparable<E>> E max(List<E> c) {
  if (c.isEmpty())
    throw new IllegalArgumentException("Empty collection");

  E result = null;
  for (E e : c)
    if (result == null || e.compareTo(result) > 0)
      result = Objects.requireNonNull(e);
  return result;
}
```

위 코드는 유연성을 위해 다음처럼 수정해야 합니다.

```java
public static <E extends Comparable<? super E>> E max(List<? extends E> list)
```

1. list에서 타입 E인 value를 생산하므로 extends로 설정합니다.

2. 그리고 Comparable의 타입 E를 instance를 소비하여 순서를 나타내는 integers를 반환하죠. (compareTo) 따라서 super로 정해주어야 합니다.

   > Comparable은 항상 consumer 입장이기에 일반적으로 <? super T>를 작성해주는 것이 좋습니다.



#### 복잡한 max method형태로 사용해야 하는 이유

다음 케이스를 고려하면 반드시 고려해야만 합니다.

```java
List<ScheduledFuture<?>> scheduledFutures = ... ;
```

`ScheduledFuture`가 `Comparable<ScheduledFuture>`를 구현할 수 없는 상황이 있기 때문입니다.

![comparable](/Users/ju/Downloads/comparable.png)

```java
public interface Comparable<E>
public interface Delayed extends Comparable<Delayed>
public interface ScheduledFutrue<V> extends Delayed, Future<V>
```

위 예제를 보면 이미 Delayed에서 Comparable을 구현했기 때문에 Scheduled는 또 Comparable을 구현할 수 없습니다.

결국 Delayed instance와 비교해야만 하죠.

일반화하여 말하자면, Comparable을 해당 타입을 이용하여 직접적으로 구현하지 않은 경우 와일드카드가 필요하게 됩니다.







# 타입 매개변수 vs 와일드 카드

메서드를 정의할 때 둘 중 어느 것을 선택해도 문제없는 상황이 있습니다. 

```java
public static <E> void swap(List<E> list, int i, int j);
public static void swap(List<?> list, int i, int j);
```

public API를 만들꺼면 간단하게 2번째를 선택하는게 좋다.



### 기본 규칙

메서드 선언에 타입 매개변수가 한 번만 나오면 와일드카드로 대체하면 됩니다.

unbounded type parameter라면 unboundded wildcard로, bounded type parameter는 bounded wildcard로 바꿔주면 됩니다.



#### 2번째 방식의 문제

다음과 같이 swap할 경우 문제가 발생합니다.

```java
public static void swap(List<?> list, int i, int j) {
       list.set(i, list.set(j, list.get(i)));
}
```

> list.set(i,val)의 반환 값은 i번째 값(바뀌기 전의 값)을 반환해줍니다.



이를 컴파일하면 다음과 같은 에러 문구가 발생하죠.

```
Swap.java:5: error: incompatible types: Object cannot be
   converted to CAP#1
           list.set(i, list.set(j, list.get(i)));
                                           ^
     where CAP#1 is a fresh type-variable:
       CAP#1 extends Object from capture of ?
```



#### 문제의 원인 - List<?>

`List<?>`엔 null만 넣을 수 있습니다. 



#### 해결

타입을 알려줄 수 있는 swapHelper를 이용해서 다음처럼 변경해주면 됩니다.

```java
 public static void swap(List<?> list, int i, int j) {
       swapHelper(list, i, j);
}
   // Private helper method for wildcard capture
private static <E> void swapHelper(List<E> list, int i, int j) { list.set(i, list.set(j, list.get(i)));
}
```



타입 추론으로 swapHelper에서 타입을 정할 수 있게 됩니다. 따라서  `List<E>`타입인 list에 값을 넣을 수 있게 되는 것이죠!



이와같이 구현하면 내부는 복잡해졌으나, 와일드 카드로 간단한 선언을 유지할 수 있게 됩니다. 다시 말해서 client는 복잡한 swapHelper의 구현을 모른 채 swap을 할 수 있게 되는 것이죠





# 정리

복잡하더라도 와일드 카드를 적용하면 API가 훨씬 유연해집니다. 그리고 작성할 땐 PECS공식을 기억하도록 합시다.