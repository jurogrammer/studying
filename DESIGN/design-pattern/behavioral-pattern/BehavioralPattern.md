# 참고자료

* GOF 도서



# Behavioral Patterns이란?

## 정의 및 특징

### 정의

알고리즘과 objects간 알고리즘과 책임 할당에 대한 패턴을 설명합니다.

### 특징

object나 class간 커뮤니케이션 패턴에 대해 설명합니다.

이러한 패턴의 특징은 런타임 중 따라가기 어려운 복잡한 컨트롤에 대한 흐름에 있습니다.

여기서 설명된 패턴들은 컨트롤에 대한 흐름에서 벗어나 **object가 연결된 관계에 집중**하도록 합니다.



## 패턴의 종류와 설명

### 1. Behavioral class patterns

#### 개략

* Behavioral class 패턴은 클래스간 **행동(behavioral)을 분산**하기 위해 **상속**을 이용합니다.

#### 종류

##### 1. Template Method

##### 2. Interpreter



### 2. Behavioral object patterns

클래스처럼 상속보다는 object composition을 이용하여 설명합니다. 

그리고 이 패턴은 2개의 관심사로 나뉩니다. 

하나는 그룹 내 object간 어떻게 소통할지에 대한 것이며, 

다른 하나는 object의 behavior을 어떻게 캡슐화하고, 요청을 캡슐화한 object에게 넘길지(위임)에 대한 것입니다.





#### 1) 그룹 내 object간 어떻게 소통할 지에 대해 관한 패턴

#### **개략**

* 이 패턴은 한 객체 혼자서 할 수 없는 일을 어떻게 협력할 수 있을지에 대해 설명합니다.

* 이 패턴의 주요 관심사는 **서로 어떻게 알지**에 대한 것입니다.
  * 만약에 서로 참조를 명시한다면 **high coupling**이 될 것입니다.

#### 종류

##### 1. Mediator

##### 2. Chain of Responsibility

##### 3. Observer



#### 2) object의 behavior을 캡슐화하고 요청을 object에 위임하는 패턴

#### 종류

##### 1. Strategy

##### 2. Command

##### 3. State

##### 4. Visitor

##### 5. Iterator



앞으로 설명드릴 때 어떤 카테고리에 속하는 패턴인지 큰 틀에서 먼저 설명드리겠습니다.
