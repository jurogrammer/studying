# Spring Field Injection에 의한 순환 참조 오류

## 참고자료

* edwith 도비양말 리뷰어님
* https://www.mimul.com/blog/di-constructor-injection/ (DI가 필요한 이유)
* https://madplay.github.io/post/why-constructor-injection-is-better-than-field-injection (생성자 주입을 필드주입 보다 권장하는 이유)
* https://d2.naver.com/helloworld/1230 (JVM Internal)



## 개요

edwith 강의에서 필드 주입을 하는 방식으로 DI를 구현하여 프로젝트 제출시 Field Injection을 하여 제출하였습니다. 하지만 리뷰어님께서 Constructor Injection를 권장하셨습니다. 친절히 관련 자료 또한 첨부해주셨습니다. 다른 부분은 다 이해되었어도 왜 순환 참조 오류를 방지할 수 있는건지 이해가 안되어 정리하기로 하였습니다.





## 가정

class A가 class B 객체를 필요로 하고, class B가 class A 객체를 필요로 한다고 보겠습니다.



### Field Injection

```java
public class A {
    @Autowired
    private B b;
}
```

```java
public class B {
    @Autowired
    private A a;
}
```

### 

Constructor Injection

```java
public class A {
    private final B b; // private B b;로도 선언가능. 즉, 이점으로 final 선언 가능. 설명x
    
    @Autowired
    public A (B b){
		this.b = b;
    }
}
```

```java
public class B {
    private final A a;
    
    @Autowired
    public B (A a){
		this.a = a;
    }
}
```



## 클래스 로더

두 Injection의 차이점을 이해하기 위해선 JVM의 클래스 로더 작동방식에 대해 알아야 합니다.

JVM의 클래스 로더는 동적 클래스 로더입니다. 다시 말해서 컴파일 후 실행시점에 모든 클래스가 실행되는 것이 아니고, **런타임 중** 클래스가 필요하게 되는 시점에 해당 클래스 로더에게 요청을 하여 클래스를 생성(로드)하도록 합니다.

이 부분을 명심하시고 Field 선언과 Constructor 선언의 차이점에 대해 알아보겠습니다.



## Field 선언과 Constructor 선언의 차이

### Field 선언

Field 선언할 경우 A 클래스가 로드되었을 때 B class 타입의 b reference 변수만 가지고 있습니다. 즉, **클래스 A의 객체가 생성 되었을 시엔 b를 생성할 필요가 없습니다.**



### Constructor 선언

아시다시피 생성자로써, 객체가 생성될 때 실행되는 메서드입니다. 따라서 **객체 A가 생성될 때 객체 B를 생성하여 담습니다.**



바로! Spring FrameWork에서 이 두 차이점이 순환 참조 오류를 방지해줍니다.



## 순환 참조 오류를 방지 과정

Spring Framework를 구동시점과 엮어 순환참조 오류 방지 과정을 설명드리겠습니다.



1. DispaterServlet 및 ContextLoader가 생성되고, 설정을 읽습니다.
2. 설정을 바탕으로 **빈 객체를 생성**합니다.



바로 2번 과정에서 순환참조 오류를 방지할 수 있느냐 마느냐의 차이가 갈립니다.

Field Injection을 했다면 참조하는 객체를 선언하지 않았으므로 순환참조 오류가 없이 정상적으로 초기화가 완료될 것입니다. 하지만 아무문제없이 잘 작동되다가 class B 또는 class A 객체를 로드할 시점이 될 때 순환참조 에러를 발생시킬 겁니다.

이에 반면, Constructor Injection은 빈 객체를 생성 시점에 순환 참조 오류가 발생합니다. 따라서 Constructor Injection을 해야 서버를 운영하기 전에 순환참조 오류를 알아채릴 수 있습니다.

따라서 리뷰어님께서 Constructor Injection을 해야 순환 참조 오류를 방지할 수 있다는 말씀을 하셨던 겁니다!



## 마무리를 지으며...

이렇게 Constructor Injection을 해야하는 이유 1가지에 대해 알아보았습니다. 나머지 장점에 대한 부분은 상위 참고자료 2개에 잘 설명되어 있으므로 여기선 설명하지 않겠습니다. 

피같은 돈 21,000원을 내고 리뷰를 신청하였지만, 전혀 아깝지 않단 생각이 들었습니다! 혼자 프로젝트를 했다면 매우 늦게 깨달았겠지요. 더불어 일찍 알아차린 만큼 이를 숙달할 시간도 생겼습니다. 완죤 이득~!

한편으로 무엇이 클린 코드인가? 에 대해 또 다른 관점을 얻었습니다. 가독성을 더불어, 사전에 오류를 방지할 수 있는 코드! 이를 생각하며 작성해야겠습니다.

단순 코더가 아닌 잘하는 개발자가 되기 위해!

