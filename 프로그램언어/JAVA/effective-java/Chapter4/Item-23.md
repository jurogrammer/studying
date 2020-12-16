# Prefer class hierarchies to tagged classes

때때로 태그를 사용하여 두 개의 인스턴스를 나타내는 클래스를 종종 볼 수 있을 것 입니다.

> 책에서 표현의 entity들을 favor라고 표현합니다.



### 예시 - Figure

이 예시는 원이나 직사각형을 나타내는 클래스입니다.

```java
// Tagged class - vastly inferior to a class hierarchy! (Page 109)
class Figure {
    enum Shape { RECTANGLE, CIRCLE };

    // Tag field - the shape of this figure
    final Shape shape;

    // These fields are used only if shape is RECTANGLE
    double length;
    double width;

    // This field is used only if shape is CIRCLE
    double radius;

    // Constructor for circle
    Figure(double radius) {
        shape = Shape.CIRCLE;
        this.radius = radius;
    }

    // Constructor for rectangle
    Figure(double length, double width) {
        shape = Shape.RECTANGLE;
        this.length = length;
        this.width = width;
    }

    double area() {
        switch(shape) {
            case RECTANGLE:
                return length * width;
            case CIRCLE:
                return Math.PI * (radius * radius);
            default:
                throw new AssertionError(shape);
        }
    }
}

```



### tagged class의 문제점

1. 코드가 지저분합니다.
   * 분기를 해야 하므로 enum declaration, tag fields, witch statement에 의해 코드가 지지분해지고 있습니다.
2. 가독성이 떨어집니다.
   * 여러 구현체들이 하나의 클래스에 존재하므로 읽기 어려워지죠
3. 메모리 낭비가 심해집니다.
   * 하나를 구현하려 해도 상관없는 다른 객체들을 구현해야 하기 때문입니다.
4. field를 final로 선언한다면, 쓰지않는 필드도 초기화해야 합니다.

5. compiler 어떤 도움을 줄 수 없습니다.
   * 런타임에서 확인이 될 뿐이죠
6. 소스를 수정하지 않는 한 추가 구현을 하기 어렵습니다.
7. 추가한다면 switch statments에 case를 추가해야만 합니다.
8. 데이터 타입이 어떠한 단서를 제공할 수 없습니다.

**=> tagged class는 장황하고, 에러가 발생하기 쉽고, 비효율적입니다.**



### 대안 - subtyping

object oriented languages에서 tagged class의 좋은 대안이 있습니다! 바로 서브타이핑이죠. **tagged class는 class hierarcy의 아류일 뿐입니다!**



# class hierarcy로 변환

### 방법

1. abstract  class를 정의하고, tag value에 의존적인 method들의 의미를 가진 abstract method를 가지도록 합니다.
   * 이 Figure 예제에선 area method가 존재하죠.
   * 이 abstract class는 class hierarcy의 root class입니다.

2. 만약 flag value에 의존하지 않는 method는 이 class에 넣도록 합니다.
   * 유사하게 모든 favor에 쓰이는 data field도 여기에 정의합니다. 
     * 이 Figure 예제에선 해당사항은 없네요.
3. 각각 original tagged class를 위해 root  class의 concrete sub class를 정의합니다.
   * circle과 rectangle이 되며 각각의 data fields에 radius, length, widthfmf sjgdjwnqslek.
   * abstract class의 method를 각각의 sub class method에 맞도록 구현해줍니다.



### 장점

tagged class의 모든 단점을 개선합니다.

1. 간단 명료합니다. 기존에 있던 장황한 코드를 찾을 수 없습니다.
   * 각 flavor 구현체들이 각자의 class로 구현되어 있고, 의미없는 데이터 필드 enum이 없습니다.
   * 모든 Field는 final이죠
2. 각 클래스의 생성자들이 모든 필드를 빠짐없이 초기화시킵니다. 그리고 추상 메서드를 모두 구현했는지 컴파일러가 확인해주죠.
3. 실수로 빼먹은 case때문에 에러 날 일이 없습니다.
4. 여러 프로그래머들이 root class 접근필요없이 hierarcy를 독립적으로 확장할 수 있습니다.

5. 타입이 각 flavor별로 분리되어 있어 특정 변수의 의미를 명시하거나 제한할 수 있고, 특정 의미만 매개변수로 받을 수도 있습니다.

6. 유연성을 증가시키고 컴파일 타임 검증을 가능하게 하면서, 타입 간 자연스러운 계층 관계 반영할 수 있습니다.

   ex:) hierarcy관계로 자연스럽게 반영하는 사례

   ```java
   class Square extends Rectangle {
     Square(double side) {
       super(side, side);
     }
   }
   ```

   