# Enforce noninstantiability with a private constructor



## 상황

단순히 class를 static method 와 static field의 Group을 만들고 싶은 상황입니다.

이는 객체지향언어에서 안 좋은 예시지만 실용적인 관점에선 괜찮을 수 있습니다. 

예를 들어서 java.lang.Math나 java.util.Arrays가 그렇지요![스크린샷 2020-11-16 오후 9.53.19](/Users/ju/Desktop/스크린샷 2020-11-16 오후 9.53.19.png)

### 문제

이러한 클래스들은 인스턴스화되면 안 되지요. 그렇지만 생성자를 작성하지 않으면 default 생성자를 compiler가 입력해주기 때문에 public API에서 인스턴스화되는 클래스들을 종종 볼 수 있습니다.



### bad case - abstract class로 선언

인스턴스화를 막기 위해 class를 abstract로 선언한들, 상속받는다면 생성할 수 있게 됩니다. 이렇게 설계한다면 사용자가 상속받아 사용하는것이라 잘못 이해할 수 있수도 있습니다.



## 해결 방법 - private constructor

```java
public class UtilityClass {
  private UtilityClass() {
    throw new AssertionError();
  }
}
```

이와 같이 한다면 다음과 같은 장점이 있습니다.

1. sub class를 생성할 수 없습니다.

   모든 sub class는 암시적으로든 명시적으로든 super class의 constructor를 실행해야 하는데, private로 선언되어 있기 때문에 불가능 합니다.

2. private로 선언되어 있기 때문에 외부에서 생성자에 접근할 수 없습니다.
3. 사이드 이펙트를 방지하기 위해 생성하려한다면 exception을 던지도록 할 수 있습니다.

