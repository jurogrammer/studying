# Generic

### Generic 용도

1. 타입을 파라미터화 해준다! 어디서? class나 Interface, methods에서~!

2. formal parameter(method에서 넣는 파라미터)처럼 type parameters는 다른 Input에 대해 재사용할 수 있도록 도와줌.
3. formal parameters의 input은 value고, type parameters의 input은 type이라는 차이 뿐.



### 이점

1. compile time에 타입체크 가능
2. casting제거할 수 있음
3. programmers가 generic algorithm 수행 가능





# Gerneric Types

generic type은 types에 대해 파라미터화된 generic class나 interface임.



```java
public class Box {
    private Object object;

    public void set(Object object) { this.object = object; }
    public Object get() { return object; }
}
```

Box에 어떤 Object를 넣든지간에 compile time에 문제없게 됨. Integer가 들어간다면 이게 들어가길 바래야 함.

따라서 만약 String들어가면 런타임 에러발생



# A Generic Version of the Box Class

### 표현

formal parameter의 파라미터 범위를 ()로 정하는 것과 달리, type parameter는 class이름 다음에 <>를 통해 받음.

```java
class name<T1, T2, ..., Tn> { /* ... */ }
```

따라서 <>에 type variable T를 선언하면 class내 어디서나 사용 가능.



### Generic으로 변경

```java
public class Box<T> {
    // T stands for "Type"
    private T t;

    public void set(T t) { this.t = t; }
    public T get() { return t; }
}
```

1. 모든 Object를 T로 변경함. 
2. 이 T는 primitive type이 아닌 모든 type이 될 수 있음.

3. interface에서 동일하게 적용.



홀리 씻... Object엔 여러 type이 들어가지만, 여기선 T로 다 통일 되버린거구나. 위 예제에서는 set에 input타입이 Object니까 Integer, 필드의 타입이 Object니까 String이런거 넣을 수도 있지만,

gerneric에선 동일한 변수만을 넣어서 String이면 모두 String으로 바꿔버림. 오마이갓!! 

나는 T에 어떤 타입이 들어가든지간에 상관없으니까 똑같은거 아닌가 했는디...





### Invoking and Instantiating a Generic Type

generic type은 어떻게 호출하고 어떻게 인스턴트화할까??

#### Invocation GericType

```java
Box<Integer> integerBox;
```

T대신 원하는 Type넣으면 됨.



method invocation과 비슷한데, method에선 argument를 넣는대신 여기선 type argument를 넣어야 함.

다른 호출과 동일하게, 위와같이 작성하면 호출하는 것 아님. 참조만 가지고 있는 것.

읽는법 : Box of Integer

> Like any other variable declaration, this code does not actually create a new `Box` object. It simply declares that `integerBox` will hold a reference to a "`Box` of `Integer`", which is how `Box<Integer>` is read.



#### Instantiating

new 키워드 작성

```java
new Box<Integer>();
```



#### The Diamond

자바 7이후로 부터는 constructor를 호출할 때 <>로만 작성해도 됨. 이를 *diamond*라 부름

```java
Box<Integer> integerBox = new Box<>();
```



### Multiple Type Parameters

generic class는 type parameters를 여러개 가질 수 있음.

```java
public interface Pair<K, V> {
    public K getKey();
    public V getValue();
}

public class OrderedPair<K, V> implements Pair<K, V> {

    private K key;
    private V value;

    public OrderedPair(K key, V value) {
	this.key = key;
	this.value = value;
    }

    public K getKey()	{ return key; }
    public V getValue() { return value; }
}
```



## Multiple Bounds

모든 bounds의 sub타입임. class가 타입이면 반드시 맨 처음에 작성해주어야 함.