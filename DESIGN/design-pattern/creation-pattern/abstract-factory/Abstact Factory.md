# 출처

* https://refactoring.guru/design-patterns/abstract-factory



# 개요

### 분류

* creational design pattern



### 정의

* 구체적인 objects의 클래스없이, 연관된 objects의 집합을 생성하도록 하는 패턴

> Abstract Factory is a creational design pattern that lets you produce 1)**families of related objects** 2)**without specifying** their concrete classes.



### 비교 - factory method

factory method에서는 \'비즈니스 로직\'을 가진 클래스에서 객체 생성에 관한 로직을 decoupling해주는 패턴이였습니다. 즉, 비즈니스 로직이 주요 로직이라 볼 수 있지요. 

그런데 app이 점점 커짐에 따라 factory method를 여러 개 만들어야하는 상황에 맞닿게 될 수 있습니다. 이렇게 된다면 클래스가 비즈니스 로직, 생성 로직에 대한 두 개의 중요한 책임을 지니게 됩니다. 

따라서 생성 로직을 분리해주는 패턴으로 abstract factory pattern를 적용시켜줄 수 있습니다.



![](https://refactoring.guru/images/patterns/content/abstract-factory/abstract-factory-en-2x.png)



# 상황

### 프로그램 요구사항

* 가구 샵 시뮬레이터를 만드려 합니다.

* 프로그램의 코드가 아래 내용을 나타내는 클래스로 구성되어 있습니다.
  1. 연관된 생산품들의 집합 (ex:) Chair + Sofa + CoffeeTable
     * 가구 샵이다보니 Chair, Sofa, CoffeeTable이 연관된 생산품이라 볼 수 있겠습니다.
  2. 각 생산품들은 각기 다른 style를 지닙니다. (ex:) ArtDeco Chair, Victorian Chair, Modern Chair)

  <img src="https://refactoring.guru/images/patterns/diagrams/abstract-factory/problem-en-2x.png" style="zoom: 67%;" />



* 새로운 스타일(variant)의 가구 집합을 추가할 때 프로그램 수정을 하지 않습니다.

  * 새로운 가구 집합이란 entic Chair, entic Sofa, entic Coffee Table 같이 새로운 스타일의 products families를 의미합니다.



# Solution

### 핵심

1. product를 추상화시켜라!
2. 연관된 families of products를 생산해주는 factory class를 만들어라!
3. 이 factory class조차 추상화시켜라!



위 핵심을 바탕으로 어떻게 **다양한 스타일**의 **연관된 families of products**들을 생성할 수 있는지 방법을 살펴보겠습니다.



### 방법

1. Art Deco, Victorian, Modern Chair -> Chair란 interface로 추상화합니다. 즉, 각 product들의 style을 product로 추상화하는 것이죠.

<img src="https://refactoring.guru/images/patterns/diagrams/abstract-factory/solution1-2x.png" style="zoom:67%;" />





2. Chair, CoffeTable, Sofa를 생성하는 메서드를 한군대 묶어 interface를 선언합니다. 이것이 Abstract Factory가 됩니다.

   

3. 그리고 Victorian 가구를 만들고 싶다면 AbstractFactory를 구현하여 Victorian products를 생성할 수 있도록 합니다. 즉, 각 스타일 별로 새로운 Factory가 만들어지는 것이죠.

<img src="https://refactoring.guru/images/patterns/diagrams/abstract-factory/solution2-2x.png" style="zoom:67%;" />



이와 같이하면 Client코드는 abtract factory에 의존하기 때문에 어떤 factory class를 가지고 있는지 알 필요가 없습니다. 그리고 product의 Interface에 의존하기 때문에 특정 product에도 의존하지 않게 되지요. 

따라서 FurnitureFactory에 의존하는 Client code에  VictorianFurtinureFactory를 넣든, ModernFurnitureFactory를 넣든지 Client code는 변경할 필요가 없게 됩니다.



# Structure

<img src="https://refactoring.guru/images/patterns/diagrams/abstract-factory/structure-2x.png" style="zoom:67%;" />



### 1. Abstract Products

연관된 product들의 interface를 선언하는 부분입니다.

ex:) createProductA(), createProductB()

### 2. Concrete Products

abstract product를 구현하여 생성된 구분되는 style의 집합입니다.

### 3. Abstract Factory

abstract products를 생성할 수 있는 interface 선언하는 Abstract Class 이때, products들은 앞서 설명된 바와 같이 연관된 products들을 선언해주어야 합니다.

### 4. concrete Factories

abstract Factory의 creation method를 구현한 class. 각 concrete Factory는 각기 독특한 스타일을 맡습니다.

!! 아무리 concrete Factories가 특정한 product를 생성한다 하더라도 return 타입은 반드시 추상화된 Type을 따르도록 해야합니다. (ex:) ModernChair가 아닌, Chair)

