

# Object간 관계에 대하여

> 깨알 용어정리
>
> 1. 부분 = part
> 2. 전체 = whole



## 1. Association

### 정의

두 객체간 약한 관계를 의미합니다.





### 특징

1. 하나의 객체가 사라진다고해서 다른 객체가 파괴되진 않습니다.
2. 하나의 객체는 다른 객체에 속하지 않습니다.





### UML 다이어그램

![](https://postfiles.pstatic.net/MjAyMDA5MTRfMjkz/MDAxNjAwMDgyODE1OTQw.4W4y-v-gKpdR5SuWXWBy18PeN-LwFrmlzQCDNbAMlnUg.S2lrSSndhbTyzzOcpGwHdYuiqp6LIf-VV6EjPCTjUNog.JPEG.study_ju/association.jpeg?type=w966)

우측의 `0..*`의 의미는 Person이 Hotel을 0개에서 복수개와 연관있을 수 있다는 의미입니다. 그 반대로, 좌측의 `0..*`의 의미는 Hotel이 Person과 0개에서 다수개와 연관있을 수 있다는 의미입니다.





### 코드

```java
public class Student {
  public void play (Sport sport) {
    excute.play(sport);
  }
}
```

이와 같이 Student-Sport간 객체 관계는 단순히 소비하는 관계가 됩니다.





## 2. Aggregation

### 정의

has-a relationship을 의미합니다. 다시말해, 전체가 부분을 가지며, 그 부분은 전체에 속합니다.





### 특징

1. 관계가 약한 편에 속합니다.

   부분이 전체에 속하더라도 전체에 독립적으로 존재할 수 있기 때문입니다.

   승무원과 여객기를 예를 들면, 승무원이 없어도 서비스를 제공 못할 지언정, 여객기는 있을 수 있고, 여객기가 없어도 승무원은 있을 수 있습니다.





### UML 다이어그램

![](https://postfiles.pstatic.net/MjAyMDA5MTRfMjQg/MDAxNjAwMDgyODIzMzYz._XR4OLMi9z7uF-RLtD0Tb3ToOx4WHxEd1HgbrnpyhTQg.y_qDjkRNwbYP7e31vyPoNMTawMUwwtTCLbqlMQhHIFsg.JPEG.study_ju/aggregation.jpeg?type=w966)

1. 죄측의 비어있는 다이아몬드는 Airliner가 전체라는 것을 의미합니다.
2. `0..*`는 위와 해석이 동일합니다. Airliner 객체는 Crew가 없을수도 있고, 많을 수도 있습니다. 반대 또한 성립합니다.



### 코드

```java
public class Airliner {
  private ArrayList<CrewMember> crew;
  
  public Airliner() {
    crew = new ArrayList<CrewMember>();
  }
  
  public void add(CrewMember crewMember) {
    
  }
}
```

1. 이 코드를 잘 보시면 Airliner가 초기화될 당시 crew는 비어있습니다. 즉, 없어도 Airliner가 존재할 수 있다는 것을 의미하지요.
2. 하지만 필드에 crew가 선언되어 있는 것을 보면 Airliner가 전체, crew가 부분이라고 보시면 됩니다.





## 3. Composition

### 정의

1. 두 object간 아주 강한 관계를 의미합니다. strong has-a 관계라고도 불립니다.

   전체는 부분이 없으면 존재할 수 없고, 부분 또한 전체가 없으면 존재할 수 없습니다.





### 특징

1. part는 whole을 통해서만 접근이 가능합니다.
2. 속한 부분은 전체에 대해 exclusive합니다.
   * 아마... 이 부분의 의미는 부분은 전체에 대해 소유하지 않고, 로직 또한 수행하지 않는다는 의미 같습니다.  AdapterPattern에서 Service가 Adapter에 대해 모른다는 의미와 일맥상통하는 것 같습니다.





### UML 다이어그램

![](https://postfiles.pstatic.net/MjAyMDA5MTRfNzYg/MDAxNjAwMDgyODI4MTkx.r62YQJMLe9QKz3VYLmQwvBTzStpm0pQ8QI6N0QCbGRsg.wRHiKoy2ymprKbX61YKdb5rIeKPk1rYujFMuulzgRf4g.JPEG.study_ju/composition.jpeg?type=w966)

1. 좌측의 채워진 다이아몬드는 2가지 의미를 가집니다.
   * House가 전체이다 (전체)
   * strong has-a 관계를 가진다. (채워짐)

2. 우측의 `1..*`의 의미는 House는 Room을 반드시 1개이상 가진다는 의미입니다.
3. 좌측에 아무런 숫자가 없는 이유는 Room은 House와 exclusive하기 때문이지요.



### 코드

```java
public class House {
  private Room room;
  
  public House() {
    room = new Room();
  }
}
```

1. House 생성 동시에 room이 생성됩니다.  반드시 room을 1개 가지고 있어야하기 때문이지요.
2. 필드로 Room을 가지고 있는 것을 보시면, House가 전체인 것을 알 수 있습니다.
3. room을 조작하려면 House내에서만, room의 메서드를 사용해야만 하겠지요.