# 출처

* https://refactoring.guru/design-patterns/abstract-factory



# Abstract Factory란?

* 생성 디자인 패턴입니다.
* 구체적인 클래스없이, 연관된 objects의 집합(family)를 생성하도록 하는 패턴입니다.

**본래 영어**

> Abstract Factory is a creational design pattern that 1)**lets you produce** 2)**families** of related objects 3)**without specifying** their concrete classes.



1) **let you produce** : 즉, client가 의존하여 products를 생성합니다.

2) **families**: products들이 매우 끈끈한 관계를 가지고 있습니다.(families -> 가족)

3) **without specifiying**: 추상클래스에 의존합니다.



왜 Abstract로 Factory를 만들었는지는... 간략히 그림을 보시고 다음으로 설명드리겠습니다.

![](https://refactoring.guru/images/patterns/content/abstract-factory/abstract-factory-en-2x.png)



# 상황

### 프로그램 요구사항

* 가구 샵 시뮬레이터를 만드려 합니다.
* 프로그램의 코드가 아래 내용을 나타내는 클래스로 구성되어 있습니다.
  1. 연관된 생산품들의 집합 (ex:) Chair + Sofa + CoffeeTable
  2. 각 생산품들은 각기 다른 style를 지님 (ex:) Art Deco Chair, Victorian Chair, Modern Chair)

* 개개의 가구 objects를 만들 수 있는 방법이 필요합니다. 이때, 동일한 style을 지닌 가구를 만들어야 합니다. 그렇지 않으면 시뮬레이터션의 customer는 화를 냅니다.(ex:) Art Deco Chair, Victorian Sofa를 가지면 화냄)



### OOD관점 요구사항

* 새로운 스타일(variant)의 가구 집합을 추가할 때 프로그램 수정을 하지 않습니다.
  * 새로운 가구 집합이란 entic Chair, entic Sofa, entic Coffee Table 같이 새로운 스타일의 products families
* 가구 공급사는 카탈로그를 자주 바꿉니다.
* 바뀔 때마다 핵심 코드는 바뀌고 싶지 않습니다.



![](https://refactoring.guru/images/patterns/diagrams/abstract-factory/problem-en-2x.png)





# 해결책

기존에 배웠던 OOD 5원칙 관점에서 문제를 생각해보겠습니다.

### OOD 5원칙

#### DIP

#### 	1. 추상화

client가 products를 소비할 것입니다. 이때 구체적인 products들인 modern chair, modern sofa...등 구체적인 클래스에 의존한다면 문제가 되겠죠.

따라서 client는 각각을 추상화시킨 class에 의존해야 합니다.

#### 	2. high-level policy

그리고 이 문제에서 핵심은 client가 furniture을 사용합니다. 그런데 furniture의 style이 바뀌더라도 client가 furniture를 사용하는 로직은 변하지 않습니다. 즉, high-level policy라 볼 수 있죠. 따라서 client또한 furniture를 추상화시킨 클래스에 의존해야 OCP에 따를 수 있게 됩니다.

#### LSP

추상화시킬 때 그 추상 클래스는 서브클래스로 대체되어야 합니다. 따라서 furniture를 추상화할 때 동일한 행동(behavior)을 지닌 클래스를 묶어 추상화 시켜주어야겠지요.



그렇다면, Abstract Factory Pattern은 위 원칙을 어떻게 구현할까요?

### Abstract Factory Pattern

1. Art Deco, Victorian, Modern Chair -> Chair란 interface로 추상화합니다. 즉, 각 product들의 style을 product로 추상화하는 것이죠.

![](https://refactoring.guru/images/patterns/diagrams/abstract-factory/solution1-2x.png)





2. Chair, CoffeTable, Sofa를 생성하는 메서드를 인터페이스로 한군대 묶어 줍니다. 이것이 Abstract Factory가 됩니다.
3. 그리고 Victorian 가구를 만들고 싶다면 AbstractFactory를 구현하여 Victorian products를 생성할 수 있도록 합니다. 즉, 각 스타일 별로 새로운 Factory가 만들어지는 것이죠.

![](https://refactoring.guru/images/patterns/diagrams/abstract-factory/solution2-2x.png)





# Structrue

![](https://refactoring.guru/images/patterns/diagrams/abstract-factory/structure-2x.png)



* Abstract Products

  연관된 product들의 interface를 선언하는 부분

  ex:) createProductA(), createProductB()

* Concrete Products

  abstract product를 구현하여 생성된 구분되는 style의 집합

* Abstract Factory

  abstract products를 생성할 수 있는 interface 선언하는 Abstract Class 이때, products들은 앞서 설명된 바와 같이 연관된 products들을 선언해주어야 합니다.

* concrete Factories

  abstract Factory의 creation method를 구현한 class. 각 concrete Factory는 각기 독특한 스타일을 맡습니다.

  !! 아무리 concrete Factories가 특정한 product를 생성한다 하더라도 return 타입은 반드시 추상화된 Type을 따르도록 해야합니다. (ex:) ModernChair가 아닌, Chair)





# 또 다른 예

![](https://refactoring.guru/images/patterns/diagrams/abstract-factory/example-2x.png)

Application이 실행되는데, 해당 운영체제가 Mac이나 Win이냐에 맞추어 GUI를 구성하려고 합니다.

따라서 client에서는 Application에서 Os가 Mac인지 Win인지 판단하여 Mac이라면 MacFactory를 주입시켜줍니다. 따라서 Mac사용자는 Mac에 관한 UI를 사용할 수 있게 됩니다.



# 장, 단점

### 장점

1. concrete products와 client code의 상호의존성을 낮출 수 있습니다.
2. SRP를 따릅니다. product를 생성하는 로직을 한 클래스에 모아두었기 때문입니다.
3. OCP를 따릅니다



### 단점

1. 많은 style의 가구들이 만들어지면 설명해야할 interface가 많아지기 때문에 복잡해질 수 있습니다.



# 다른 Pattern과 장단점

1. 많은 디자인들은 Factory Method로 시작하여 상황이 복잡해지면 Abstract Factory로 발전합니다.

2. Abstract Factory는 Factory Method들의 Set이라 볼 수 있습니다.

3. 사견으로, Factory Method를 지닌 Class는 Business Logic을 포함하지만, Abstract Factory는 생성해야할 product가 많아짐에 따라 생성하는 책임만을 가지는 것 같습니다.