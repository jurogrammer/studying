# Open-Closed Principle

클래스, 모듈, 함수 등은 확장에 대해선 열려있어야 하고, 수정에 대해선 닫혀있어야 한다.

*`- MEYER Bertrand(1988) Object-Oriented Software Construction`*



확장은 허용하고, 수정은 허용하면 안된다.



다시 말하자면, 클래스는 수정없이 확장 가능해야 한다.



## 원칙 구현 방법

방법은 두 가지가 있습니다. 두 방법은 일반화 방법을 사용하는 것이 공통적이나, 목표나 기술 그리고 결과에서 차이를 가집니다.



### 1. Meyer's open-closed principle

#### 방법

상속을 통하여 구현하라.

#### 설명

상속을 이용하면, 부모 클래스는 상속을 통하여 구현할 수 있으므로 open에 대해서는 개방적이고, 자식 클래스를 통해 부모 클래스를 접근하므로써 부모 클래스는 숨겨져 있기 때문에 수정에 대해선 닫혀있을 수 있다.



### 2. Polymorphic open-closed principle

#### 방법

추상 클래스나 interface를 이용하여 구현하라.

#### 설명

Meyer는 구체화된 모듈에 대해 상속을 말하는 반면,  로버트 마틴이 제시한 방법은 추상 클래스를 이용한다(또는 인터페이스 이용). 이렇다면 추상 클래스는 변경에 대해 닫혀있고, 구현체들로써 확장에 대한 열려 있을 수 있다.







## Robert C. Martin이 1996년도에 발표한 레포트

OOD 5원칙은 로버트 마틴에 의해 제시된 내용. 따라서 OCP가 최초로 소개된 문서를 바탕으로 이해해보려고 함.

 [Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin) ["The Open-Closed Principle", C++ Report, January 1996](https://docs.google.com/a/cleancoder.com/viewer?a=v&pid=explorer&chrome=true&srcid=0BwhCYaYDn8EgN2M5MTkwM2EtNWFkZC00ZTI3LWFjZTUtNTFhZGZiYmUzODc1&hl=en) [Archived](https://web.archive.org/web/20060822033314/http://www.objectmentor.com/resources/articles/ocp.pdf) August 22, 2006, at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine)



### 도입부



*모든 멤버 변수는 private로 선언하라!*

*전역 변수는 피해!!*

*run time type identification (RTTI)는 위험해!!*



**이 휴리스틱 방법들의 근본적인 이유(source)은 무엇일까?**

도대체 어떤 이유가 이것들이 맞고 틀리게 해주는 것일까?

**=> open-closed principle!**



변경이 필요할 때,이미 작동하고 있는 **이전의 코드를 수정하지 않더**라도 단지 모듈에 **새로운 코드를 추가함으로써 동작(behavior)의 확장**이 가능해진다.



### 설명

open-closed principle을 잘 지킨 모듈은 두가지 주요 특성을 가집니다.

1.They are "Open For Extention"

어플리케이션의 요구사항이 변경되거나, 새로운 어플리케이션의 요구 사항을 충족시키기 위해 모듈의 동작을 새롭고 다른 방식으로 만들 수 있는 것을 의미.

2.They are "Closed for Modification"

해당 모듈은 변경되어선 안된다(inviolate). 그 무엇도 이 코드를 변경시킬 수 없음.



이 두 가지가 상반되어 보일 수 있음.

1. 보통 모듈을 확장하기 위해서는 모듈을 수정해야 함.
2. 일반적으로 모듈을 바꿀 수 없다는 것은 해당 모듈이 고정된 동작을 가진 것을 의미한다.

어떻게 해결이 가능할까?



### Abstraction is the Key

1. 모듈이 **고정**된 abstraction에 의존함으로써 수정에 대해선 닫혀있고,
2. abstraction을 구현함으로써 모듈의 동작은 확장가능해질 수 있다.



#### 예제 1 Client-Server

client에서 server를 사용하고 있으므로 server를 바꿀 경우(확장)엔 client 코드에서 server의 이름을 바꿔줘야만 함.

하지만 Abstract Server에 의존한다면 Server바꾸기 가능.



#### 예제 2 Shape Abstraction

DrawAllShapes에서 원과 사각형을 그리기 위한 함수.

그런데 **새로운 도형이 추가**되면 DrawAllShapes가 만들어져야 함.

추상화가 핵심이므로 DrawAllShapes함수가 원과 사각형을 추상화 시킨 **Shape**에 의존하도록 한다.



### Strategic Closure

수정에 대해 닫혀있도록 하는 것을 반드시 피할 수 있는 것이 아님. 따라서 어떤 module을 수정에 대해 닫히게 할 지를 전략적으로 정해야 한다.

(내용 미완)





# 추가 사항

포인트 우선순위 테이블

