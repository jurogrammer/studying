# 출처

* https://refactoring.guru/design-patterns/factory-method



# Factory Method란?

### 분류

생성 디자인 패턴 (creational design pattern)

### 정의

super class에서 object를 생성할 수 있는 interface를 제공하고, sub class에서는 생성되는 object의 타입을 바꿀 수 있도록 하는 패턴입니다.



# 상황

![logisImages](https://refactoring.guru/images/patterns/diagrams/factory-method/problem1-en-2x.png)



* 트럭을 이용한 기존 물류 앱이 있습니다.
* 이 사업이 번창하여 앱에 배(Ship)을 추가하여 해상 물류 서비스도 지원하려고 합니다.



### 문제점

Truck이 전체 시스템과 강하게 **Coupling**되어 있어 Ship을 추가하기 어렵게 됩니다.

* 시스템에서 `new Truck()` 과 같은 코드는 concrete한 class에 의존하게 만들기 때문에 강하게 결합되었다 말할 수 있습니다.



### 해결책

#### 분석

1. 시스템이 truck이라는 구체적인 클래스에 생성 및 사용을 함으로써 의존하고 있습니다.
2. 어떤 물류 수단이 오더라도 비즈니스 로직은 동일합니다.
   * 트럭으로 운송하든, 배로 운송하든지 간에 물건을 싣고, 그 물건을 전달해준다는 로직은 동일하죠.

#### 방안

1. 어떤 물류 수단이든, 공통 비즈니스 로직인 부분은 absract class에 둡니다. 여기선 아래 그림에서 보이는 planDelivery가 해당 로직이 됩니다.

2. client에서 직접적으로 truck을 생성하는 call(new Truck)을 factory method로 대체합니다. 

![](https://refactoring.guru/images/patterns/diagrams/factory-method/solution1-2x.png)



3. 그리고 Truck과 Ship은 추상화시켜 Transport라는 인터페이스를 구현하도록 합니다.
   * 특정 class와 결합이 생기면 안되니까요.

![](https://refactoring.guru/images/patterns/diagrams/factory-method/solution2-en-2x.png)



truck을 생성할 지, ship을 생성할 지는 factory method를 오버라이딩 함으로써 구현할 수 있습니다.



다시 한 번 요약하여 설명드리자면,다음과 같습니다.

1. 물류 수단을 통해 비즈니스 로직을 작성해야 합니다.

2. 그런데  강하게 결함되면 안되므로 factory method로 생성을 하고, Transport라는 인터페이스에 의존하도록 하는 것이죠.
3. 결국 비즈니스 로직은 factory method로 받은 Transport 타입인 object를 이용하여 비즈니스 로직을 수행하는 형태가 됩니다.



# 구조

> **[용어 정리]** object를 생성해주는 method를 **factory method**라 부르고, 이 method로 인해 생성되는 object를 **product**(truck,ship)라 합니다.

![](https://refactoring.guru/images/patterns/diagrams/factory-method/structure-2x.png)



### Product

* interface로 선언 합니다.



### Concrete Products

* product에 대해 서로 다르게 구현합니다.



### Creator

* factory method를 선언합니다.
* facory method의 **Return type**을 지정하는 것이 중요합니다. 다시 말해 Products의 추상화된 type을 지정하는 것이 중요한 것이죠.
* **이름과 다르게, 이 클래스의 주요 책임은 객체를 생성하는 것이 아닌, products와 관련된 business logic 또한 가지고** 있습니다. 
* 단지 factory method를 이용하여 생성 로직과 비즈니스 로직이 분리되는 것을 돕는 것뿐입니다.



### Concrete Creators

* 서로 다른 타입의 product를 반환할 수 있도록 factory method를 오버라이드합니다.
* **반드시 새로운 instance를 반환하는 것이 아닙니다**. 이미 생성된 instance를 반환할 수 있습니다.
  * 싱글톤, 캐싱, object pool 등과 같은 전략을 취할 수 있습니다.

