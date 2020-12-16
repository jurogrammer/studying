





# Design and document for inheritance or else prohibit it

Item 18에서 상속하도록 디자인되고 문서화되지 않은 foregin class를 상속받는 것은 위험하다고 했습니다. 

그렇다면 상속을 위한 디자인과 문서는 무엇을 의미할까요?



# overridable methods의 self-use (문서화)

자기 사용법을 문서화해야 합니다.

1. 클래스의 API로 공개된 메서드에서 호출하는 메서드가 overridable method일 경우, 이를 명시해주어야 합니다.
2. 어떤 순서로, 각각의 호출 결과가 이어지는 처리에 어떤 영향을 주는지도 담아야 합니다.

이 둘을 일반화하면 overridable method를 호출하는 모든 상황을 문서로 남겨주어야 합니다.

> 엄청 위험한 놈이니까 계속 주의 준다고 볼 수 있겠네요.



### 메서드 내부 동작 방식 서술

java docs에서 Implementation Requirements로 표현되는 곳은 내부 동작 방식을 설명하는 부분이라고 보시면 됩니다. 



### 예시 - AbstractCollection

![스크린샷 2020-12-07 오후 9.30.50](/Users/ju/Desktop/스크린샷 2020-12-07 오후 9.30.50.png)



iterator method를 재정의하면 remove method 동작에 영향 줄 수 있는 것, 그리고 어떤 영향이 미치는지도 잘 설명해주고 있습니다.

HashSet의 add와 addAll과는 대조적이죠.



### API설명 한계

좋은 API문서는 어떻게 동작하는지 설명하는 것보다 무엇을 설명하는지가 주된 내용이어야 합니다. 위 방식은 위 말과 대치가 되죠.

그런데 어쩔 수 없습니다. 상속은 캡슐화를 해치니까요.

> 책에선 @impleSpec이라 적는다는데 코드엔 없네요?



# hook으로 선별 (디자인)

따라서 문서화를 잘 하는것만이 능사가 아니라 hook을 잘 선별하여 protected로 제공하는 것도 중요합니다.



### 예시 - AbstractList

![스크린샷 2020-12-07 오후 9.38.51](/Users/ju/Desktop/스크린샷 2020-12-07 오후 9.38.51.png)



![스크린샷 2020-12-07 오후 9.40.43](/Users/ju/Desktop/스크린샷 2020-12-07 오후 9.40.43.png)





![스크린샷 2020-12-07 오후 9.39.19](/Users/ju/Desktop/스크린샷 2020-12-07 오후 9.39.19.png)



### 잘 선별한 점

List 구현체 최종 사용자는 removeRange 관심없습니다. 어떤 영향도 주지 않죠. 하지만!

clear method 최적화하고 싶은 사람에겐 관심이 가게 됩니다. clear method를 최적화하고 싶다면 removeRange를 오버라이딩하여 구현하는 것이지요.

오버라이딩하여 구현하도록 하지 않았다면, 위 매커니즘을 바닥부터 구현해야 했을 것 입니다.



### protected method 구현방법

"there is no bullet"

왕도는 없으며, 실제 하위 클래스를 만들어보고 테스트해보는 것이 가장 좋은 방법입니다.

protected method가 너무 많으면 내부 구현을 많이 노출시키는 것이며, 너무 적으면 상속의 이점이 없어집니다.

protected 멤버를 놓치면 서브 클래스를 작성할 때 빈자리가 느껴질 것이며, 반대로 protected로 선언했지만 전혀 신경쓰이지 않았다면 private로 선언해두어야했던 method인 것입니다.



### 구현시 주의점

#### 1. 유지보수 고려

영원히 유지보수해줘야 하므로 신중해야 합니다. 따라서 상속용으로 설계한 클래스는 반드시 서브 클래스를 만들어서 검증해봐야죠.

### 2. 상속용 클래스의 생성자에서 override method 호출 금지

이를 어기면 프로그램이 오작동합니다. 

1. 상위 클래스의 생성자가 하위 클래스의 생성자보다 먼저 실행됨
2. 그러므로 하위 클래스에서 override한 메서드가 먼저 호출됨
3. 호출된 method가 하위 클래스 생성자에서 초기화하는 값에 의존하면 문제 발생

```java
// Class whose constructor invokes an overridable method. NEVER DO THIS! (Page 95)
public class Super {
    // Broken - constructor invokes an overridable method
    public Super() {
        overrideMe();
    }

    public void overrideMe() {
    }
}
```

```java
// Demonstration of what can go wrong when you override a method  called from constructor (Page 96)
public final class Sub extends Super {
    // Blank final, set by constructor
    private final Instant instant;

    Sub() {
        instant = Instant.now();
    }

    // Overriding method invoked by superclass constructor
    @Override public void overrideMe() {
        System.out.println(instant);
    }

    public static void main(String[] args) {
        Sub sub = new Sub();
        sub.overrideMe();
    }
}
```



### 3. Cloneable, Serializable 상속 자제

clone, readObject는 생성자와 비슷한 효과 발생하여 생성자와 비슷한 제약을 가집니다.

#### clone

 method에서 overridable method를 호출하면 복제본의 상태를 모두 복사하기 전에 오버라이드한 메서드를 호출하게 됨

#### readObject

하위 클래스의 상태가 역직렬화가 다 되기 전에 오버라이드한 메서드부터 호출하게 됨

#### readSolve, writeReplace

protected로 선언해줄 것. private하면 상속 불가능하므로.



# 어지간하면 상속하지 마세요

### 버그

상속용으로 설계되지도 않고 문서화되지 않은 class를 상속하여 사용하다가 버그 리포트 올리는 일이 적지 않다. 따라서 그대로 두면 안되고 상속을 못하도록 강제해야 한다.



### 상속 금지 방법 두가지

1. class를 final 선언
2. 생성자를 private로 선언하고 객체 생성은 static method로 제공



### 상속 안하고도 잘 사용함

Set, List, Map의 경우 핵심 기능을 interface로 제공하고 구현하여 사용하도록 개발하였습니다. 이렇게 하면 상속을 금지해도 좋지요.



### 표준 인터페이스를 구현하지 않고선 상속금지하면 어려워짐.(??)

오버라이딩 가능한 메서드를 없애고 문서화하기.



### overridable method를 제거하는 기계적인 방법

overridable method의 코드를 private helper method로 옮기기

이 helper method를 호출하도록 수정