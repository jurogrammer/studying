# Prefer Interface to anonymous classes



## 옛날의 함수 타입 표현

### 1. function object

추상 메서드를 하나만 담은 인터페이스(or 추상 클래스)를 사용했습니다. 이것을 function object라고 부르죠.



### 2. anonymous class

두 문자열을 길이 순으로 정렬하는 예제입니다.

```java
Collections.sort(words, new Comparator<String>() {
  public int compare(String s1, String s2) {
    return Integer.compare(s1.length(), s2.length());
  }
});
```



이처럼 strategy pattern처럼 사용하였습니다.

strategy의 Interface는 comparator가 되며, 정렬을 구현하는 부분이 세부 전략을 의미하죠.



#### 문제

가독성이 너무 떨어졌습니다. 익명클래스를 사용하면 코드가 장황해지죠. 



## lambda expression

위에서 functional interface라 부르는 인터페이스의 instance를 lambda expression을 사용해 만들 수 있게 되었습니다.

다시 말해, lambda expression의 표현식을 작성하면 functional interface의 instance가 생성되는 것이죠.



#### 간결한 코드의 예

이 람다를 사용하면 가독성이 훨씬 좋아집니다. 위 코드는 아래처럼 변환할 수 있죠.

```java
Collections.sort(words,
(s1, s2) -> Integer.compare(s1.length(), s2.length()));
```



#### 타입

기본적으로, lambda expression의 타입은 컴파일러가 자동으로 추론해줍니다. parameter type, return 타입 모두 타입 을 추론해줍니다. 

> 이 타입추론은 이해하기 매우 어려우므로 넘어가도록 하겠습니다. 정 알고 싶으면 java specification 책을 보시면 됩니다.

만약에, 컴파일러가 타입을 제대로 추론하지 못할 경우에만 캐스팅해주도록 합니다.

> 한편으로, 컴파일러가 타입추론하므로, 컴파일 타임에 타입을 결정지어주는 제너릭을 잘 활용해야 합니다. 제너릭에 대해 설명했던 내용을 명심하시면 되겠습니다.



### 코드를 좀 더 간결하게,

#### comparator construction method 이용

```java
	Collections.sort(words, comparingInt(String::length));
```



#### List interface의 `.sort`이용

List interface의 sort method는 java 8에 추가되었습니다.

```java
words.sort(comparingInt(String::length));
```



#### 상수별 클래스를 간결하게

```java
// Enum type with constant-specific class bodies & data (Item 34)
public enum Operation {
    PLUS("+") {public double apply(double x, double y) { return x + y; }},
    MINUS("-") {public double apply(double x, double y) { return x - y; }},
    TIMES("*") {public double apply(double x, double y) { return x * y; }},
    DIVIDE("/") {public double apply(double x, double y) { return x / y; }};
  
    private final String symbol;
  
    Operation(String symbol) {
        this.symbol = symbol;
    }
    @Override
    public String toString() {
        return symbol;
    }

    public abstract double apply(double x, double y);
}
```

위 코드를 lambda expression을 사용하면 더 간단해집니다.



```java
// Enum with function object fields & constant-specific behavior
public enum Operation {
    PLUS("+", (x, y) -> x + y),
    MINUS("-", (x, y) -> x - y),
    TIMES("*", (x, y) -> x * y),
    DIVIDE("/", (x, y) -> x / y);
  
    private final String symbol;
  
    private final DoubleBinaryOperator op;

    Operation(String symbol, DoubleBinaryOperator op) {
        this.symbol = symbol;
        this.op = op;
    }

    @Override
    public String toString() {
        return symbol;
    }

    public double apply(double x, double y) {
        return op.applyAsDouble(x, y);
    }
}
```

1. 연산해주는 lambda expression을 받도록 해줍니다.

   lambda expression를 나타내는 표현식은 functional interface의 인스턴스라고 했죠? 따라서, ENUM 선언부에 각각에 맞는 lambda expression을 선언해줍니다.

2. Functional Interface 타입

   여기선 DoubleBinaryOperator라는 functional interface를 사용했습니다. 이 함수는 두 개의 double parameter를 받아 double타입을 반환해주는 함수입니다.

3. apply 구현부

   lambda expression을 통해 op intsance가 초기화되었습니다. 따라서 그 op instance의 applyAsDouble(x,y) method로 값을 반환해주는 부분을 표현해주는 것이죠.



## lambda expression의 한계점

### 1. 부수 표현

람다는 이름이 없고, 문서화도 못합니다. 따라서, 식으로 간결히 표현할 수 있는 경우가 아니라면 사용을 자제해야 하죠.

3줄을 초과하면 사용을 자제하도록 합시다.



### 2. 인스턴스 접근

열거 타입 생성자 안의 람다는 열거 타입의 인스턴스 멤버에 접근할 수 없습니다. (인스턴스는 런타임에 만들어지기 때문.)

lambda expression에서 인스턴스 필드나 메서드를 사용해야 한다면 상수별 클래스를 선언해야 합니다.



## anonymous class가 lambda expression보다 우위에 있는 부분

1. abstraction class의 instance를 만들 때 람다를 쓸 수 없어 anonymous class 사용.

2. method가 여러 개인 인스턴스 생성

3. lambda의 this

   lambda는 자신을 참조할 수 없습니다. this를 사용하면 바깥 인스턴스를 참조하죠. 따라서 자신을 참조해야 한다면 anonoymous class를 사용해야 합니다.



## 직렬화 지양

직렬화는 지양합시다!

직렬화는 구현 별로 다르므로(ex: JVM별로) 지양하도록 합시다. anonymous class도 해당합니다.

꼭 직렬화를 해야한다면, private static nested class의 인스턴스를 사용합시다.

