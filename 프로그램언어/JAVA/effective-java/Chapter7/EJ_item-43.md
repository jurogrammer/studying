# Prefer method references to lambdas

간결함 때문에 람다가 나왔지만 더 간결한 방법이 있습니다., 그것이 바로 메서드 참조(method references)입니다.





## Mapping exam

### map

임의의 key와 Integer를 맵핑하는 프로그램입니다. key의 값이 instance의 수를 의미한다면, multiset을 구현하는 것이죠

> multiset이란?
>
> 집합은 중복 원소를 허용하지 않는 것과 달리, 중복을 허용하는 집합



```java
map.merge(key, 1, (count, incr) -> count + incr);
```

이 코드는 키가 안에 없다면 해당 키를 1과 맵핑하고, 있다면 value에 1을 더하라는 코드입니다.



### 문제 - 파라미터가 거추장스럽다

기존 값과 더하라는 표현을 보면 거추장스럽게 보일 수 있습니다. 단순히 합을 하라는 뜻인데, 2개의 파라미터를 받도록 변수 명을 지어주었기 때문이죠.



### 해결은 메서드참조로

이 문제는 메서드 참조로 다음처럼 단순하게 나타낼 수 있습니다.

```java
map.merge(key, 1, Integer::sum);
```

파라미터를 없애서 더욱 간결해졌죠.

> 한편으로는, 파라미터로 의미를 분명히할 수 있기 때문에 때로는 람다로 표현하는 것이 가독성에 더 좋을 수 있습니다.



대부분의 경우, 람다는 메서드 참조로 치환될 수 있습니다. 그래서 람다로 쓴다음에, 메서드 참조로 변경하는 방식을 사용합니다. 

그렇기에 보통 IDE에서 lambda expression을 쓰면 메서드 참조를 추천해줍니다.



## 반대로 메서드 참조가 거추장스러울 때

클래스 내에서 해당 클래스의 메서드를 사용할 땐 메서드 참조가 거추장스러울 수 있습니다. 다음 예를 보시죠.'



### 예제 - service

```java
service.excute(GoshThisClassNameIsHumongous::action);
```

이는 다음으로 변환될 수 있습니다.

```java
service.excute(() -> action());
```

람다는 호출한 곳의 컨텍스트를 가지기 때문에 가능한 일이죠.



## method의 종류

앞선 내용은 static method입니다. method는 이외에도 4가지가 더 있죠.





### instance method

인스턴스 메서드엔 2가지 유형이 있습니다.

bound instance method와 unbound instance method가 존재합니다.

receiving object가 명시되느냐, 마느냐의 여부로 나뉩니다.

한정적 참조의 경우, static method 참조와 참조되는 메서드와 받는 인수가 모두 같죠.

비한정적 참조에서는  함수 객체를 적용하는 시점에 수신객체를 알려줍니다. 따라서 매개변수 목록의 첫번째에 수신 객체 전달용 매개변수가 추가되죠.





### class Constructor

클래스를 생성하는 메서드 참조입니다.

```java
TreeMap<K,V>::new
```



### Array Constructor

배열을 생성하는 메서드 참조입니다.

```java
int[]::new
```

