# 출처

* https://refactoring.guru/design-patterns/adapter



# Adapter pattern이란?

* 구조 패턴
* 두 인터페이스가 불일치할 때, 두 인터페이스가 상호작용할(collaborate) 수 있도록 해주는 디자인 패턴입니다.



<img src="https://refactoring.guru/images/patterns/content/adapter/adapter-en-2x.png" style="zoom:50%;" />



# 상황

<img src="https://refactoring.guru/images/patterns/diagrams/adapter/problem-en-2x.png" style="zoom:50%;" />

### 목표

주식 시장 모니터링 어플을 만드려고 합니다.

### 방법

2. stock data를 `XML` 포맷으로 받습니다.
3. Analytics Library를 통해 분석을 하고, 그래프를 보여주려고 합니다.

### 문제

그런데 **문제**가 있습니다. Analytics Library는 `JSON` 포맷으로 데이터를 받아 분석합니다. 즉, Stock데이터를 공급해주는 곳의 포맷과 데이터를 받아 분석하는 프로그램의 포맷이 불일치합니다.



### 서드 파티 라이브러리 코드를 변경하여 해결하려 한다면?

#### 문제

##### 1. 서드 파티 라이브러리의 의존성이 깨질 수 있습니다.

##### 2. 서드 파티 라이브러리 코드 접근조차 불가능 할 수 있습니다.



# 해결 방법

<img src="https://refactoring.guru/images/patterns/diagrams/adapter/solution-en-2x.png" style="zoom:50%;" />

### Adapter Pattern 이용!

1. 어댑터에서 `XML` -> `JSON`으로 변환과정을 거칩니다.
   * 이로 인해서 client는 단순히 Adapter에 `XML` 데이터를 넘겨주기만 하면 됩니다.
   * 또한 복잡한 변환 코드는 Adapter에 숨겨둘 수 있습니다.
2. 그리고 변환된  `JSON`을 Analytics Library에 넘겨줍니다.
   * 단지 Adapter에서 Analytics library를 호출함으로써, analytics library가 adapter의 존재를 알아차릴 수 없습니다. 다시말해, Adapter에 의존하지 않습니다.
3. 그리고 Analytics Library에 반환된 결과물을 Client에게 넘겨줍니다.







# 구조

### 1.Object Adapter

<img src="https://refactoring.guru/images/patterns/diagrams/adapter/structure-object-adapter-2x.png" style="zoom:50%;" />

#### 1. Client Intrface

1. Client Interface는 client가 Service를 사용하기 위한 인터페이스입니다.
2. client가 인터페이스에 종속하기 때문에 OCP를 따릅니다. 따라서 새로운 version의 Adaper로 교체하더라도 client 코드를 변경하지 않아도 됩니다.



#### 2. Adapter

1. Adapter는 client와 service간 코드를 작성할 수 있는 클래스.
2. 이고 client interface를 구현하고, service object를 wrapping합니다.
   * service를 언제 초기화할지는 2가지 방법이 있습니다.
     1. 생성자를 통해 주입받아서. (eager loading)
     2. 메서드 호출시. (lazy loading)
3. adapter interface를 통해 client의 요청을 받고, service에 맞는 포맷으로 변환한 뒤 wrapped service에게 데이터를 전송해줍니다.



#### 3. Service

1. 클라이언트에서 사용하려 하나, 포맷이 맞지 않은 Service를 의미합니다.



### 2.Class Adapter

<img src="https://refactoring.guru/images/patterns/diagrams/adapter/structure-class-adapter-2x.png" style="zoom:50%;" />

1. multiple inheritance를 구현해주는 언어에서만 사용가능합니다.
2. Existing Class란 현재 Client가 서비스 적용을 위해 사용하는 클래스라고 보면 됩니다.
3. Adapter는 Service 상속받기 때문에 Service를 Wrapping할 필요가 없으며, Client가 사용 중인 method를 오버라이딩해주면 client는 Adapter의 method를 사용할 수 있게 됩니다.



> 두 어원의 차이는 아마... Object Adapter는 서비스를 **객체**를 통해 사용하고, Class Adapter는 서비스 **클래스**를 상속받아 사용해서인 것 같습니다.

