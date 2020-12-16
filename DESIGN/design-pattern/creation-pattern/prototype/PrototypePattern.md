# 출처

* https://refactoring.guru/design-patterns/prototype



# 프로토타입 패턴이란?

* 생성 디자인 패턴
* 생성할 object의 클래스에 의존하지 않고 이미 생성된 object를 통해 동일한 object를 생성할 수 있는 디자인 패턴입니다.



<img src="https://refactoring.guru/images/patterns/content/prototype/prototype-2x.png" style="zoom:50%;" />



### 프로토타입?

앞으로 설명드릴 프로토타입이란 용어와 일상생활에서 쓰이는 용어와 차이점이 있습니다. 제가 이 패턴을 처음 접했을 때 가장 헷갈려서 개념을 받아들이기 어려웠기 때문에 차이점을 먼저 짚어보겠습니다.



#### 일상생활에서 쓰이는 프로토타입 용어

* 이 프로토타입은 대량생산 전 성능을 검증하고 개선하기 위해 핵심기능만 넣어서 제작한 모델을 프로토타입이라 부릅니다.
* 또는 게임의 본격적인 개발에 앞서 재미요소나 구현 가능성을 검증하기 위해 제작하는 시제품을 의미하지요.

아마 이 두 뜻이 일반적으로 알고 있는 내용이라 생각이 듭니다. 그렇기 때문에 이 정의에 맞추어 프로토타입 패턴을 받아들이려고 하면 어려움이 뒤따를 수 밖에 없습니다. 프로토타입 패턴에서 프로토타입은 다음과 같습니다.

#### 프로토타입 패턴에서 프로토타입 용어

* **자기 자신을 복제하는 기능**을 지원하는 **객체**를 프로토타입이라고 부릅니다.  

  `An object that supports cloning is called a prototype.`



**자기 자신을 생성한다**는 면에서 큰 차이점이 있습니다. 따라서 이 프로토타입은 오히려 자기복제하는 아메바와 비슷한 의미하는 것이지요.

<img src="https://refactoring.guru/images/patterns/content/prototype/prototype-comic-3-en-2x.png" style="zoom: 50%;" />

그래도 두 용어의 어원은 '원초적 형태'라는 의미를 가지고 있긴 합니다.



# 상황

* object를 똑같이 복제하려 합니다.



### 방법 - object의 클래스를 이용

1. object의 클래스에서 새로운 object를 생성합니다.
2. 복제하고 싶은 object의 모든 필드를 그대로 새로운 object로 카피하여 옮깁니다.



#### 문제점

1. 필드가 private로 선언된 경우 object의 field값에 접근못할 수 있습니다.
   * 이 때문에 런타임 중 object를 복제하지 못합니다.
2. concrete class에 의존하게 됩니다.
   * concrete class를 이용하여 생성하기 때문입니다.
3. object의 인터페이스만 알고 있는 경우 생성할 수 없습니다.
   * 다른 interface를 통해서 객체를 받은 경우 concrete  class를 모를 수 있습니다.



# 해결방법

#### **복제하는 책임을 class에서 복제하려는 object에게 넘깁니다!**

1. concrete class를 찾아 생성할 필요가 없어집니다.

2. object 자신은 자신의 field에 접근할 수 있기 때문에 private로 선언된 문제도 해결할 수 있습니다.



#### **복제하려는 objects들의 interface를 선언합니다.**

1. 생성한 object를 concrete class로 받을 필요가 없어집니다.
2. 보통 이 interface는 자기 자신을 복제하는 clone() 메서드를 선언합니다.



# 구조

### 1. Basic implementation

<img src="https://refactoring.guru/images/patterns/diagrams/prototype/structure-indexed-2x.png" style="zoom: 67%;" />

#### 1. Prototype

프로토타입을 만드려는 객체 클래스들의 interface입니다. (다시 한번 프로토타입을 말하자면 자가 복제 기능을 가진 객체!!)

이 인터페이스를 통해서 clone를 상속받고, 프로토타입 객체들을 이 공통의 타입으로 받을 수 있게 되지요. (다형성)

```java
public interface Prototype {
    public Prototype clone();
}
```





#### 2. ConcretePrototype

프로토타입의 인터페이스를 구현합니다. 따라서 이 클래스는 **clone()**메서드를 가지고 있습니다.

```java
public class Circle implements Prototype {
    private int x;
    private int y;

    public Circle(Circle prototype) {
        this.x = prototype.x;
        this.y = prototype.y;
    }

    public Circle(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public Prototype clone() {
        return new Circle(this);
    }
}
```





#### clone()

그리고 clone()을 다음과 같은 방식으로 구현합니다.

1. 생성자에 자신의 타입을 가진 객체를 넘길 수 있도록 합니다.

2. 초기화를 위해 파라미터로 받는 생성자를 만들어줍니다.

   * 복제하기 위해 자신의 객체를 넣어주어야 하는데 이 부분이 없으면 자신의 객체를 만들 수가 없기 때문입니다.

   



#### sub-class

1. super(prototype)를 이용하여 상위 class에 값을 전달해줍니다.

```java
public class RedCircle extends Circle {
    private String color;
		
    public RedCircle(RedCircle prototype) {
        super(prototype);
        this.color = prototype.color;
    }
  
    //javascript와 비슷한 방식
    public RedCircle(Circle circle, String color) {
        super(circle);
        this.color = color;
    }
  
    public RedCircle(int x, int y, String color) {
        super(x, y);
        this.color = color;
    }

    public Prototype clone() {
        return new RedCircle(this);
    }
}
```



#### 3. Client

1. Prototype interface를 통해 객체를 생성할 수 있습니다.

   ```java
   public class Client {
       Prototype circle = new Circle(3, 5);
       Prototype redCircle1 = new RedCircle(3, 5, "red");
       Prototype redCircle2 = new RedCircle((Circle) circle, "red");
   
       Prototype newCircle = circle.clone();
       Prototype newRedCircle = redCircle1.clone();
   }
   ```

   



### 2.Prototype registry implementation

프로토타입들을 콜렉터를 통해 관리할 수 있도록 구현 합니다. 따라서 클라이언트에게 어떻게 생성하는지는 숨길 수 있고, 클라이언트는 이 저장소를 통해 값을 가져올 수 있습니다.



여기서 클라이언트는 값을 제공해주고 빼내오는 클래스로 1. 초기화하여 레지스트리에 값을 저장하려는 클래스, 2. 레지스트리에 접근하여 값을 가져오려는 클래스 두 가지로 봐도 될 것 같습니다.



<img src="https://refactoring.guru/images/patterns/diagrams/prototype/structure-prototype-cache-indexed-2x.png" style="zoom: 67%;" />


