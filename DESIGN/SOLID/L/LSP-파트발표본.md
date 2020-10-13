# 참고 자료

* https://en.wikipedia.org/wiki/Liskov_substitution_principle (wiki liskov-substitution-principle)
* http://www.butunclebob.com/ArticleS.UncleBob.PrinciplesOfOod (LSP article)
* https://en.wikipedia.org/wiki/Design_by_contract (wiki design_by_contract)



#  Introduction

앞서 OCP의 핵심 메커니즘은 추상화와 다형성을 이용하는 것이였습니다. 바로 상속을 이용하여 abstract base class로부터의 derived class를 생성할 수 있었습니다.

그렇다면 어떤 디자인 규칙(rule)이 이러한 특수한 상속을 이행(govern)시키는 걸까요?

가장 좋은 상속 계층(inheritance hierarchies)의 특징은 무엇일까요?

어떤 요소가 OCP에 부합하지 않는 계층 구조를 유발할까요?

이번 주제에서 해당 질문과 관련한 내용을 설명드리겠습니다.



<img src="https://postfiles.pstatic.net/MjAyMDA5MDRfNjIg/MDAxNTk5MTQ3NzgyMTkx.xsbCuCgJBzvpKSyViYDOKrfuYYOoz33a5zHQyQzyHAAg.xSrMD_SGvsrh_8VO6tNjDRG2jcZH-6KfbxZMgzL2v1sg.PNG.study_ju/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2020-09-03_%EC%98%A4%ED%9B%84_11.53.19.png?type=w966" style="zoom: 33%;" />



```cpp
class Reader {
  public:
   virtual int Read() = 0;
};

class Writer {
  public:
   virtual void Write(char) = 0;
};

void Copy(Reader& r, Writer& w) {
  int c;
  while((c=r.Read()) != EOF)
  w.Write(c); 
}
```



# Liskov Substitution Principle 정의

바로 Liskov가 했던 말을 소개하면 어렵게 와닿을 수 있기 때문에 로버트마틴이 의역한 LSP를 먼저 말씀드리겠습니다.



### 로버트 마틴이 말하는 LSP

***FUNCTIONS THAT USE POINTERS OR REFERENCES TO BASE CLASSES MUST BE ABLE TO USE OBJECTS OF DERIVED CLASSES WITHOUT KNOWING IT.***

=> 베이스 클래스를 참조하거나, 베이스 클래스의 포인터를 사용하는 함수는 반드시 베이스 클래스로부터 파생된 클래스에 대해 모르고도 파생 클래스를 사용할 수 있어야 한다.



### Liskov가 실제 했던 말

![스크린샷 2020-09-02 07.04.31](https://postfiles.pstatic.net/MjAyMDA5MDJfMjk1/MDAxNTk4OTk4OTQ0MDUy.XlHbMCRWfJqg4YI52e0HcV6bKPX1tumIe1TlTuSwIWog.7hXnpasdQYnm3l2wR3aC9GP9t76IWB-2tOsOePJXuXEg.PNG.study_ju/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2020-09-02_07.04.31.png?type=w966)


$$
{\phi}(x)를~자료형T의~객체~x에~대해~증명할~수~있는~속성이라~하자.
$$

$$
~그렇다면 ~S가~T의~하위형이라면~	{\phi}(y)는~자료형S의~객체~y에~대해~증명할~수~있어야~한다.
$$





## 이 원칙이 중요한 이유

이 원칙이 위배되었을 때 상황을 떠올리면 쉽습니다. 만약에 LSP를 따르지 않는다고 봅시다. 베이스 클래스를 참조하거나 포인터를 사용하는 함수는 반드시 베이스 클래스로부터 파생되는 함수를 모두 다 알아야 합니다. 이렇게 된다면 OCP를 위반하게 되는것이죠. 파생된 클래스가 새로 생성될 때마다 해당 함수를 수정하게 되니까요.

LSP를 위반한 간단한 예제를 보여드리겠습니다.



### A Simple Example of a Violation of LSP

```c++
void DrawShape(const Shape& s) {
  if (typeid(s) == typeid(Square))
  	DrawSquare(static_cast<Square&>(s));
  else if (typeid(s) == typeid(Circle))
  	DrawCircle(static_cast<Circle&>(s));
}
```

shape라는 base클래스가 있고 이 shape를 상속받은 square, circle클래스가 있습니다. DrawShape라는 함수엔 base class reference를 가지고 있습니다. 

이 함수는 LSP를 위반하여 이 **shape reference가 square이냐, circle이냐를 일일이 확인해보고** 각자에 맞는 함수를 구현하도록 되는 것이죠.

> *[참고] 이러한 함수의 구조를 OOD의 저주라고 부릅니다(anathema to Object Oriented Design)* 



# Square and Rectacgle, a More Subtle Violation

#### 소개

앞서 소개드린 simple한 예제와 달리 이 예제는 아주~ 미묘하게 LSP를 위반합니다. 그만큼 볼 가치가 있는 예제이기 때문에 이 내용을 소개해드립니다.



#### 예제의 상황

직사각형 클래스를 가진 Application이 있습니다. 추후 사용자들이 정사각형도 그릴 수 있는 기능을 요구하였습니다.



#### Rectangle 코드

```cpp
class Rectangle {
  public:
  void SetWidth(double w) {itsWidth=w;}
  void SetHeight(double h) {itsHeight=w;}
  double GetHeight() const {return itsHeight;}
  double GetWidth() const {return itsWidth;}
  private:
  double itsWidth;
  double itsHeight;
};
```





### 접근 - 수학적 개념에 맞게 적용

![직사각형, 정사각형 관계](https://postfiles.pstatic.net/MjAyMDA5MDJfMjU4/MDAxNTk5MDAwNDUxMzEx.iwuo6kUsqAx7l1cLQi7qd_u2I0IqKlRRy7eqJgzsGMAg.Rb3x0FCHuON6VZI__TZ-sJkFkFjJA3NI8ogkhYtfOHog.PNG.study_ju/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2020-09-02_07.45.07.png?type=w966)

상속은 ISA관계입니다.  그리고 정사각형은 직사각형이다라고 말할 수 있으니 수학적으로도 의미가 맞습니다.

따라서 [Figure 1]에서 보이는대로 직사각형 클래스를 상속받아 정사각형 클래스를 구현하였습니다.

하지만! **이 생각이 미묘하지만 심각한 문제를 유발할 수 있습니다.**



#### 이 관계가 잘못된 이유

1. Square클래스는 itsHeight와 itsWidth 두 개는 필요없습니다. 정사각형 정의에 따라 변 한 개만 주어져도 됩니다.
   * 이는 메모리 낭비로 이어집니다.
2. 정사각형에서 w,h가 동일 하므로 SetWidth, SetHeight은 매우 부적절한 함수입니다.
   * Square클래스에 맞지 않는 함수가 있으므로 **잘못된 설계**입니다.



하지만 근본적인 문제를 해결하지 않고  문제를 조금 수정하여 해결하려고 노력해보도록 하겠습니다. (way to sidestep the problem)

### 비껴가기1 - Sqaure method 변경

1. 메모리는 충분하다 가정하여 1번 문제를 피해가고, 

2. Square의 setWith와 SetHeight를 다음과 같이 수정한다면 2번 문제까지 피해갈 수 있습니다.

```cpp
void Square::SetWidth(double w) {
  Rectangle::SetWidth(w);
  Rectangle::SetHeight(w);
}
void Square::SetHeight(double h) {
  Rectangle::SetHeight(h);
  Rectangle::SetWidth(h);
}
```

**수학적으로** 정사각형이라는 의미가 맞아 떨어지게 됩니다.



#### 이 방법이 잘못된 이유

```c++
void f(Rectangle& r) {
	r.SetWidth(32); // calls Rectangle::SetWidth
}
```

base class의 참조를 받아 조작하는 함수가 있습니다.
이 함수에서 r에 Square 객체의 포인터가 들어간다면 Square 객체는 width와 height가 달라지게 됩니다. (Rectangle의 SetWidth메소드 사용)
이것은 명백히 square의 수학적 정의가 틀리게 되죠.



한편으로 base class 메서드에서 virtual로 선언하지 않았기 때문이다, OCP를 위반했지만 어쩔 수 없는 설계 미스이므로 단순히 virtual로 바꿔주면 된다. 라고 말할 수 있습니다만, 이에 대해 로버트 마틴은 setWidth와 setHeight는 매우 기초적인 연산(operation)이므로 설계 미스라고 정당화하기 어렵다. 그리고 square의 존재가 없었으면 무엇을 근거로 virtual로 선언할 것인가?라고 말을 했습니다. 

다시말해서 복잡한 시스템이라면 예측이 어려워 설계미스가 날 수 있다만, 매우 간단한 연산이기에 예측하여 설계에 포함할 수 있어야 한다는 의미같습니다.

하지만, 위 의견을 받아들여 virtual로 선언하도록 하겠습니다.

### 비껴가기2 - virtual

단순히 Rectangle의 SetWidth와 SetHeight를 virtual로 바꾸면 방법2의 문제를 해결 할 수 있게 됩니다.

[최종 코드]

```c++
class Rectangle {
  public:
  virtual void SetWidth(double w) {itsWidth=w;}
  virtual void SetHeight(double h) {itsHeight=h;}
  double GetHeight() const {return itsHeight;}
  double GetWidth() const {return itsWidth;}
  
  private:
  double itsHeight;
  double itsWidth;
};

class Square : public Rectangle {
  public:
  virtual void SetWidth(double w);
  virtual void SetHeight(double h);
};
void Square::SetWidth(double w) {
  Rectangle::SetWidth(w);
  Rectangle::SetHeight(w);
}
void Square::SetHeight(double h) {
  Rectangle::SetHeight(h);
  Rectangle::SetWidth(h);
}
```

#### 이 코드가 맞아 보이는 부분

1. 수학적으로 맞는 직사각형 클래스로 조작할 수 있다.

2. 수학적으로 맞는 정사각형 클래스로 조작할 수 있다.

3. Rectangle을 참조하는 포인터를 사용하는 함수에 Square를 넘겨줄 수 있다.



하지만, 근본적인 문제는 모델 그 자체가 자신을 잘 설명하느냐가 아닌(자기서술적), 이를 **사용하는 유저**에게 달려있습니다. 



***여기서 잠깐!***

> **유저(client, user)의 의미**
>
> 코드 level에서 특정 변수,함수,객체 등을 사용하는 함수라고 볼 수 있습니다. 
>
> ```{cpp}
> void f(Rectangle& r) {
> 	r.SetWidth(32); // calls Rectangle::SetWidth
> }
> ```
>
> 이 코드에서 r이라는 reference의 유저는 함수 f가 됩니다.
>
>
> 그리고 이 함수 f는 결국 프로그래머가 작성하므로 작성한 프로그래머를 user라고 볼 수도 있지요.



## 근본적인 문제를 보여주는 코드

```c++
void g(Rectangle& r) {
  r.SetWidth(5);
  r.SetHeight(4);
  assert(r.GetWidth() * r.GetHeight()) == 20);
}
```

Rectangle을 사용하는 유저입장에서 생각해봅시다.

r은 직사각형이기 때문에 위처럼 Width를 5로 설정하고, Height를 4로 설정한다면 20이 나온다고 생각할 수 있습니다.

하지만! 정사각형이 들어가면 틀립니다.

유저는 Height가 4로 들어갈 때 width또한 4로 변경되기 때문이지요.



#### 유저가 잘못한 걸까?

유저가 잘못됬다고 보기 어렵죠. Rectangle 레퍼런스를 가지고 있기 때문에 Rectangle대로 메서드를 사용했던 것이니 합리적으로 사용했다고 볼 수 있습니다.



## 그러면 도대체 무엇이 잘못된걸까?

수학적으로 정사각형은 직사각형이 아니라서? 상속은 ISA관계가 아니라서?! 아닙니다! 

그런데 분명히 square object는 rectangle object가 아니에요. 왜냐구요? **행동적으로(Behaviroally), 정사각형은 직사각형이 아니기 때문이지요!** 그리고 소프트웨어에서 가장 중요한 것은 행동입니다. (it is *behavior* that software is really all about.)

결국 LSP에 따른다는 것은, 모든 파생 클래스는 유저가 사용하는 베이스 클래스의 행동을 따라야만 한다는 것을 의미합니다.





# Design by Contract

이 LSP문제는 Bertrand Meyer가 말했던 Design by Contract라는 개념과 아주 밀접한 관련이 있습니다. 이 관점에서 LSP를 설명드리겠습니다.



#### Design by Contract란?

소프트웨어 시스템의 각 구성요소들이 어떻게 협력할 지를 계약 관점에서 서술한 것을 의미합니다.

여기서 사용하는 용어가 존재하나, 이를 제외하고 예시를 들어 핵심만 간단히 설명드리도록 하겠습니다.



##### 계약 주체

계약은 user와 supplier 두 시스템 요소간 계약을 의미합니다.

```java
void f(Rectangle& r) {
  r.SetHeight(5);
	r.SetWidth(4);
}
```

이 코드에서 f는 유저, r은 supplier에 해당하겠습니다.



##### 의무와 댓가, precondition-postcondition

계약 관점에서 f가 계약서에 씌여진 의무를 수행하면 r은 그에 합당하는 댓가를 줘야죠.

 r이 적절한 값을 넘겨주는 것이 그 의무가 될 것이며 f가 rectangle의 width를 4로 설정하는 것이 그 댓가가 될 것입니다.



여기서, 의무는 다시말하여 method가 정상적으로 수행하기 위해 만족시켜야할 조건이라 할 수 있습니다. 이를 **precondition**(선행조건)이라 부릅니다.

그리고 의무가 다했을 때 method가 반드시 보장해줘야할 댓가를 **postcondtion**(후행조건)이라 부르죠



#### DbC관점에서 LSP설명

```cpp
void f(Rectangle& r) {
  r.SetHeight(5);
	r.SetWidth(4);
}
```

이 코드를 계속 살펴보겠습니다.

f가 r의 setWidth method에 precondition으로 적절히 4란 값을 넘겨주었습니다. 그렇다면 setWidth는 어떤 실행을 보장해주어야 할까요?

```cpp
assert((its Width == w) && (itsHeight == old.itsHeight));;
```

임을 보장해주어야 합니다. r은 Rectangle이니까요.



다시 말해서 **user는 base class의 precondition과 postcondtion만을 압니다.** 따라서 base class의 postcondition을 기대하여 r의 method를 사용하게 되는 것이죠.



그런데 만약에 square가 들어간다면 `(itsHeight == old.itsHeight)` 이 postcondition을 만족할 수 없게 됩니다. 그래서 LSP를 따르지 못한 문제가 발생했던 것이죠.



그렇기 때문에 반드시 모든 derived class는 base class의 postcondition을 만족하도록 해야 합니다.



## 결론 - LSP는 유저가 생각하는 클래스의 행동에 달려있다.

위 예제에서 볼 수 있듯이 LSP를 순응함에 있어 직사각형 클래스와 정사각형 클래스가 수학적으로 의미가 맞느냐가 중요한게 아니였습니다. 

**유저가 object를 사용하는 행태에 달려있었죠.**



그리고 그 [근본적인 문제를 보여주는 코드]에서 볼 수 있 듯, 

**유저가 생각하길, 파생 클래스는 베이스 클래스의 행동을 그대로 따를 것이라고 생각합니다.**

따라서 설계하는 사람은 이를 잘 고려해야만 LSP를 따르는 design을 만들 수 있습니다!

