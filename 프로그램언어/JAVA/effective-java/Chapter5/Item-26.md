# Don't use raw types

### 용어정리

1. generic class or generic interface

   타입 파라미터를 정의한 클래스나 인터페이스

   ex:) List\<E\> (list of E 라 읽음)

2. generic types

   generic class, generic interfaces를 묶어 부르는 말

3. parameterized types

   각, generic type은 parameterized types를 정의합니다.

   class와 interface name 다음,  <>안에 actual type parameters가 따라 옵니다.

   ex:) List\<String\>

   List\<String\> : parameterized types

   String : actual type

   E : formal type

4. row type

   제너릭 타입에서 타입 매개변수를 사용하지 않았을 때.

   ex:) List\<E\>의 List

   타입이 지워진 것 처럼 작동하는데, 제너릭 전 코드와 하위호환성을 위해 지원



# 제너릭이 나오기 전 문제

```java
private final Collection stamps = ...;
//unchecked call 경고 뱉음
stamps.add(new Coin(...));

for (Iterator i = stamps.iterator(); i.hashNext();) {
  Stamp stamp = (Stamp) i.next();
  stamp.cancel;
}
```

Collection에 Coin을 넣든, stamp를 넣든 에러가 발생하지 않습니다.

그런데 사용하기 위해서 casting했을 때 ClassCashException이 발생하는 것이죠.



두번째로, 잘못된 type을 넣은 시점이 아닌, 형변환이 발생한 시점에 발생하므로 문제의 원인과 동떨어져 있습니다. 그래서 에러찾기가 어려워지죠.



# 개선

```java
private final Collection<Stamp> stamps = ...;
```

이렇게 선언해주면, 컴파일러에게 Collection에는 Stamp만이 들어가야함을 알려줄 수 있습니다. 따라서 컴파일러가 타입을 체크해주고, 경고가 없다면 문제가 없는 것이죠.



### 에러문구

```
Test.java:9: error: incompatible types: Coin cannot be converted to Stamp
```





# Raw 타입 쓰지 마시오

raw타입을 쓰면 제너릭이 주는 안전성과 표현력을 모두 잃죠.

#### raw타입 존재이유: 호환성

generic type을 늦게 받아서 이전 코드들이 제너릭없이 모두 짜였습니다.

그래서 제너릭으로 선언되었어도 작동되게 만들었어야 했죠. (그역도 포함) 따라서 raw 타입을 지원하고, 제너릭 구현에는 erasure를 지원하게 되었습니다.



### List와 List\<Object\>

Raw타입보다는 임의의 객체를 허용하는 매개변수화 타입은 괜찮습니다.



#### 차이점

간단히 말하자면 List는 제너릭과 전혀 관련성이 없고, List\<Object>는 모든 타입을 허용한다고 컴파일러에게 알려 준 것.

따라서 List에는 List\<String>을 넘겨줄 수 있지만,

List\<Object>에는 List\<String>을 넘겨줄 수 없습니다. 하위호환성에 위배되기 때문이죠.



따라서 로타입을 사용하면 타입 안전성을 잃는다고 말할 수 있습니다.



# Raw 대신 unbounded wildcard type

임의의 타입을 받고 싶다면 차라리 unbounded wildcard type인 ?을 사용하면 됩니다.



### 예시

Set<E>대신 Set<?>를 사용하면 됩니다. 어떤 타입이든 받을 수 있는 가장 범용적인 타입입니다.

```java
static int numElementsInCommon(Set<?> s1, Set<?> s2) { ... }
```



Raw type collection엔 어떤 타입이든 넣을 수 있어서 문제가 되지만 Collection<?>에는 null 외엔 어떤 원소도 들어갈 수 없죠. 따라서 다른 원소를 넣으려고 하면 다음과 같은 에러를 출력합니다.

```
WildCard.java:13: error: incompatible types: String cannot be converted to CAP#1
	c.add("verboten");
				^
 where Cap#1 is a fresh type-variable: CAP#1 extends Object from capture of ?

```

어떤 원소도 Collection<?>에 넣지 못하게 만들고, 컬렉션에서 꺼내는 객체의 타입도 전혀 알 수 없게 만들었습니다.



> 만약 제약을 피하고 싶다면, 제너릭 메서드 또는 bounded wildcard type를 사용하면 됩니다.



# RawType써야하는 예외들

### 1. class 리터럴

class 리터럴에는 Raw타입을 써야합니다. (+ 배열, 기본타입 허용)

허용: List.class, String[].class, int.class

금지: List\<String>.class, List<?>.class



### 2. instanceof 연산자

런타임 중에는 제너릭 타입 정보가 지워지므로 unbounded wildcard type 이외 매개변수화 타입은 적용할 수 없습니다.

Raw든, ?든 동일한 의미로 작동하죠. 따라서 ?는 안쓰는게 낫습니다.

#### 올바른 예

```java
if(o instanceof Set) {
  Set<?> s = (Set<?>) o;
}
```

Set인지 확인 후 Set<?>으로 캐스팅해주어야 합니다.

checked cast여서 컴파일러 경고가 발생하지 않습니다.

