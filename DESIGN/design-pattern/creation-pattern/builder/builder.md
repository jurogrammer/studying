# 출처

* https://refactoring.guru/design-patterns/builder (builder패턴 설명)
* https://projectlombok.org/features/Builder (lombok)
* Effetive Java 3/E Item-02



# Builder란?

* 생성 디자인 패턴
* 복잡한 objects를 하나씩 하나씩(step-by-step)생성할 수 있게 해주는 디자인 패턴입니다.
* 동일한 생성 코드로 다른 타입의 object를 만들 수 있도록 합니다.



<img src="https://refactoring.guru/images/patterns/content/builder/builder-en-2x.png" style="zoom:50%;" />



# 상황

* 많은 field와 nested objects를 하나하나 생성해야하는 **복잡한 object**를 만들어야 합니다.



### 권장하지 않는 방법1 - class 상속을 통해 구현

<img src="https://refactoring.guru/images/patterns/diagrams/builder/problem1-2x.png" style="zoom:50%;" />

#### 방법 설명

1. **기본 클래스 생성**

이 방법은 House라는 기본이되는 클래스를 만든다고 합시다. 이 클래스는 지붕 및 창문 외벽 등을 가지고 있습니다. 이때, 구체적인 필드 값을 가지도록 만들어줍니다. 다시 말해서 오두막집 클래스, 벽돌집 클래스를 만들어주는 겁니다. 예를 들어 오두막집 클래스의 외벽은 나무일 것이고 벽돌집 클래스의 외벽은 벽돌이 되겠지요.



2. **확장시 - 서브 클래스 생성**

오두막집에 창고를 둔 집을 만들고 싶다면? 오두막집을 상속받고, 창고를 추가해주면 됩니다.



#### 문제점

1. sub클래스가 무수히 많아집니다
   * 매 새로운 파라미터마다 서브클래스를 만들어주어야하기 때문입니다.
2. 계층이 깊어질 수 있습니다.
   * 상속은 계층적인 형태를 띕니다. 만약에 부속건물 확장이 아닌, 스타일(ex: modern)을 추가하여 확장을 한다면 한단계 깊게 만들어야겠죠.



### 권장하지 않는 방법2 - giant 생성자 (effective java에선 telescope 생성자)

<img src="https://refactoring.guru/images/patterns/diagrams/builder/problem2-2x.png" style="zoom:50%;" />

#### 방법 설명

가능한 모든 파라미터를 받는 생성자 작성



#### 문제점

1. 필요없는 파라미터를 고려하여 argument를 넣어야 합니다.
   * 위 그림의 왼쪽에서 보시듯, 창고만 달린 일반 집을 생성함에도 다른 옵션까지 고려하여 null로 넣어주어야 합니다.
2. 각 인자의 의미를 파악하기 어렵습니다.
   * 파라미터가 많아질 경우 몇 번째 인자가 어떤 의미를 가지는지 파악하기 어렵기 때문입니다.



### 권장하지 않는 방법3 - JavaBean pattern

#### 방법 설명

java의 javabean 규약에 따라 클래스를 정의한 후, 값을 설정해줍니다.

```java
public class NutritionFacts {
    // Parameters initialized to default values (if any)
    private int servingSize  = -1; // Required; no default value
    private int servings     = -1; // Required; no default value
    private int calories     = 0;
    private int fat          = 0;
    private int sodium       = 0;
    private int carbohydrate = 0;

    public NutritionFacts() { }
    // Setters
    public void setServingSize(int val)  { servingSize = val; }
    public void setServings(int val)     { servings = val; }
    public void setCalories(int val)     { calories = val; }
    public void setFat(int val)          { fat = val; }
    public void setSodium(int val)       { sodium = val; }
    public void setCarbohydrate(int val) { carbohydrate = val; }

    public static void main(String[] args) {
        NutritionFacts cocaCola = new NutritionFacts();
        cocaCola.setServingSize(240);
        cocaCola.setServings(8);
        cocaCola.setCalories(100);
        cocaCola.setSodium(35);
        cocaCola.setCarbohydrate(27);
    }
}
```

#### 문제점

여러 cocaCola를 여러 콜로 설정해주기 때문에 작성하는 코드에 따라 상태가 일정하지 않을 수 있습니다. 즉, 생성 중 다른 쓰레드가 접근하여 값을 변경할 수도 있다는 것이죠.



# 해결책 - Builder 패턴

Builder 패턴은 object의 생성코드를 생성하려는 클래스의 밖으로 꺼냅니다. 그리고 *builders*라는 개개의 오브젝트에게 그 생성 책임을 맡깁니다. 이 builder는,

1. 생성해야할 필드를 하나씩 정할 수 있도록 해줍니다.
2. 생성이 필요한 필드만 지정하여 필드를 정할 수 있습니다.

<img src="https://refactoring.guru/images/patterns/diagrams/builder/solution1-2x.png" style="zoom:50%;" />

[그림의 설명] *The Builder pattern lets you construct complex objects step by step. The Builder doesn’t allow other objects to access the product while it’s being built.*   



3. 그리고 객체를 만드는 동일한 행동으로 서로 다른 객체도 만들 수 있습니다.

<img src="https://refactoring.guru/images/patterns/content/builder/builder-comic-1-en-2x.png" style="zoom:50%;" />

​	이 그림은, 통나무집, 벽돌집, 보석집을 지으려고 하려고 합니다. 모두다 다르나, 외벽을 짓고, 지붕을 올리는 등 동일한 행동 패턴을 가지고 있기 때문에 동일한 행동패턴을 지닌 빌더로 다른 스타일의 집을 만들 수 있다는 그림입니다.



### Director

* builder가 특정한 절차를 따라서 만들 수 있도록 도와주는 class입니다. 

* 이 클래스의 용도는 자주 생성할 객체가 있다면 director에서 builder를 통해 생성할 수 있도록하는 것입니다. (재사용성)

* 따라서 빌더 패턴에서 이 클래스를 만드는 것은 선택사항입니다.
* 추가로, client에게 객체가 어떻게 생성되는지 숨길 수 있습니다.

<img src="https://refactoring.guru/images/patterns/content/builder/builder-comic-2-en-2x.png" style="zoom:50%;" />



# 구조

<img src="https://refactoring.guru/images/patterns/diagrams/builder/structure-2x.png" style="zoom:50%;" />

#### Builder Interface

* 이 인터페이스는 builder의 필드별 생성 메서드(step)를 지정해줍니다.

* 객체 초기화를 위해 reset()이라는 메서드를 작성합니다.



#### Concrete Builders

* 서로 다른 객체를 생성합니다. 다시 말해서, 객체를 생성하기 위한 행동(Step)이 동일하다면 Builder를 구현하면 됩니다.
* 그래서 생성된 객체가 타입이 불일치 할 수 있습니다.



#### Products

* concrete Builder에 의해 생성된 객체입니다



#### Director

* 자주 사용되는 builder를 구현합니다.
