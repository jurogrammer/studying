



## INTRODUCTION

#### 용어정리

#### client, user 특정 클래스나 객체를 사용하는 객체,함수,클래스 등



### ISP란?

Interface Segeregation Principle의 약자로, 인터페이스를 분리해야한다는 원칙입니다.



### 문제점

이 원칙이 지켜지지 않았을 경우엔 뚱뚱한 인터페이스(또는 오염된 인터페이스)가 만들어집니다. 이 인터페이스는 대게 응집성이 좋지 않습니다. 다시말해 연관성이 떨어지는 함수가 한 인터페이스에 집중되어 있다는 뜻입니다.



### 목표

이 fat 인터페이스는 ISP에 따라 분리되어야 하는데, 이 인터페이스를 사용하는 클라이언트는 단일 클래스로 볼것이 아니라, 응집성있는 인터페이스인 추상화된 베이스 클래스를 알아야합니다.



### 앞으로 알아볼 내용

1. fat 또는 polluted의 단점

2. 어떻게 이 인터페이스가 생성되는지
3. 이를 방지하기 위해 어떻게 클래스를 디자인해야 하는지

예시를 통해 설명드리도록 하겠습니다.



## Interface Pollution

### 상황

 도어락이 있는 보안 시스템

**Security Door**

```c++
class Door{
    public:
    virtual void Lock() = 0;
    virtual void Unlock() = 0;
    virtual bool IsDoorOpen() = 0;
};
```



**Timer**

```c++
class Timer {
    public:
    void Register(int timeout, TimerClient* client);
};
```

```c++
class TimerClient {
    public:
    virtual void TimeOut() = 0;
};
```

Timer의 Register함수를 시간과 TimerClient포인터와 같이 넘겨주면, timeout변수 만큼 시간이 흐른 뒤에 TimerClient의 TimeOut()이 실행되어 경보가 울립니다.



### 문제: 어떻게 하면 타이머 기능을 가진 보안문을 만들까?

#### 일반적인 방법

대게는 아래와 같은 방법으로 구현합니다. (가정 TimerClient 스스로 Timer의 Register함수 기록 및 TimeOutMessage를 받음)

![Figure 1](https://postfiles.pstatic.net/MjAyMDA5MDJfMTU0/MDAxNTk5MDU4MzIyOTA2.daBokgN3M7J7KA2f5HVMkkyAzzrjWh_crNjWqsXmRcwg.LkMqU0qrHS7oCs83-mSoCuDWx2nFAxzAdkLmm-hlExAg.JPEG.study_ju/feature1.JPG?type=w966)

1. Door에 TimerClient기능이 필요하므로 Door가 TimerClient를 상속받습니다.
2. 그리고 타이머 기능일 지닌 보안문을 구현하기 위해 Door를 implement합니다.



#### 이 방법의 문제점

1. Door가 TimerClient에 의존하게 됩니다.
   * Door를 구현하는 모든 객체가 Timer가 필요한 것이 아님에도 Timer를 구현해야 합니다
   * 타이머를 구현하고 싶지 않다면 nil virtual function(c++)을 선언해야 하는데 이는 결국 LSP를 위반하게 됩니다.
2. 본래의 Door 클래스는 Timer와 전혀 관련이 없습니다.
   
* Timer와 관련이 없는 Door객체를 생성할 때도 반드시 TimerClient class를 import해줘야 합니다.
   
3. 합리적인 요구사항으로 수정함에도 불구하고 타이머가 필요없는 다른 파생클라스까지 모두 악영향을 끼치게 됩니다. (**한 파생클래스의 변경사항이 다른 파생 클래스에 악영향을 미치는 케이스**)

   **예**

   문이 열렸을 때 Timer가 동작한다고 가정합시다. 문을 열어서 타이머가 시작됬는데 타이머가 끝나기 전에 문을 닫고 다시 열었습니다. 그렇다면 이전에 작동한 타이머가 곧바로 울리게 되므로 설계미스가 됩니다. 

   따라서 이를 고치기 위해 timeOutId를 부여하여 이를 해결합니다.

   ```c++
   class Timer {
       public:
           void Regsiter(int timeout
                         int timeOutId,
   				      TimerClient* client);
   };
   
   class TimerClient {
       public:
       virtual void TimeOut(int timeOutId) = 0;
   };
   ```

   

   그런데, timeout을 추가한 것만으로 모든 파생 클래스를 수정해주어야 합니다. 인터페이스를 작성한것이기 때문에 timer와 연관된 파생 클래스는 수정하는 것이 합리적입니다. 하지만 문제는 **timer와 관련없는 파생클래스까지 영향을 미치기 때문에 예측하기 어려워 집니다.**

   

즉, Door 인터페이스는 **TimedDoor**를 만들기 위해 TimerClient를 상속받음으로써 **오염**되었습니다!

그리고 오염이 쌓이고 쌓이면 결국 **fat Interface**가 만들어지는 것이죠



## 해결하기

### KeyPoint

**TimedDoor을 사용하는 client가 분리되어 있기 때문에 반드시 TimedDoor을 분리해야 합니다.**

Timer는 TimeClient를 사용하고, Door는 door객체에게 사용됩니다. 분리해야하는 이유는  문제점 3처럼 한 클라이언트의 요구사항이 해당 클라이언트를 구현하지 않은 다른 파생 클래스에 악영향을 끼치기 때문입니다.



 두 개의 인터페이스를 하나의 객체에서 구현해야 합니다. 왜냐하면 두 인터페이스는 동일한 데이터(하나의 문)에 접근하기 때문이지요. 

객체를 이용하는 client는 객체의 interface에 접근한다기 보단, delegation이나 object의 base class에 접근함으로써 해당 객체에 접근이 가능해집니다.

### Separation through Delegation

![Figure 2](https://postfiles.pstatic.net/MjAyMDA5MDJfNTQg/MDAxNTk5MDU4MzIyOTAx._51wKK4xT3cSpJ4HaiU2YO-tTFOMh9f03NeVtRq68rog.68B0bsJdCqu48zG8tFtquCyPQtNL_0f3bjb_xrV5mFAg.JPEG.study_ju/feature2.JPG?type=w966)

```c++
class TimedDoor : public Door {
    public:
    	virtual void DoorTimeOut(int timeOutId);
    };

class DoorTimerAdapter : public TimerClient {
    public:
        DoorTimerAdapter(TimedDoor& theDoor)
        : itsTimedDoor(theDoor)
    	{}
	virtual void TimeOut(int timeOutId)
		{itsTimedDoor.DoorTimeOut(timeOutId);}
    private:
		TimedDoor& itsTimedDoor;
};
```





#### 방법

1. Door를 TimedDoor로 구현
2. TimerClient를 DoorTimerAdapter로 구현
3. TimedDoor은 DoorTimerAdapter를 생성하고, Timer를 넘김
4. Timer가 TimeOut을 실행하면 DoorTimerAdapter에게 전달
5. DoorTimerAdapter는 TimeOutMessage를 TimedDoor에게 전파(delegate)한다



#### 장점

1. Timer코드가 변경되더라도 Door의 파생 클래스는 전혀 영향 없음
2. TimedDoor는 TimerClient를 구현하지 않아도 됨!
3. DoorTimerAdapter가 Door에서 TimedDoor 인터페이스처럼 작동하도록 도와줌.



=> 매우 일반적인 목적의 방법

#### 단점

1. timeout를 입력하기 위해 매번 timer객체를 생성함
2. delegation은 약간의 메모리 사용
   * 임베디드 시스템에선 문제가 됨

### separation through multiple Inheritance

![Figure 3](https://postfiles.pstatic.net/MjAyMDA5MDJfMTE2/MDAxNTk5MDU4MzIyOTE0.D57govA-U7ISnWeUcIN2v9bLfnj5q0ceYDZp9WRPUr0g.Qa948zmN01mylhlYsVBIUAdP7HUQJcJev3Z49IGbgx0g.JPEG.study_ju/feature3.JPG?type=w966)



#### 방법

​	TimedDoor 클래스가 Door와 TimerClient 모두 구현.



#### 장점

1. Door파생 클래스, TimerClient도 TimedDoor사용 가능하나, 둘은 모두 TimedDoor에 의존하지 않게 됨.

   => 이로 인해 둘 모두 동일한 object를 사용할 수 있게 됨

2. 심플해서 좋다!



#### Adapter와 비교

로버트 마틴이 Adapter를 쓰는 유일한 이유는 Timer를 다르게 조정할 때 필요.(Timer를 매번 생성하고, )

