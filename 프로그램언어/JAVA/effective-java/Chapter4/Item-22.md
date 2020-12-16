# Use interfaces only to define types

interface는 Type 용도로써만 사용되어야 됩니다! 

(여기서 말하는 Type은 interface를 구현하는 class의 Instance를 참조하는데 사용되는 타입입니다.)

따라서 해당 인터페이스를 구현한 클래스의 인스턴스로 클라이언트가 무엇을 할 수 있는지 말해주어야 하죠.

이외 목적으로 인터페이스를 작성하면 안됩니다.



# Bad Case - Constant interface

```java
// Constant interface antipattern - do not use!
public interface PhysicalConstants {
    // Avogadro's number (1/mol)
    static final double AVOGADROS_NUMBER   = 6.022_140_857e23;

    // Boltzmann constant (J/K)
    static final double BOLTZMANN_CONSTANT = 1.380_648_52e-23;

    // Mass of the electron (kg)
    static final double ELECTRON_MASS      = 9.109_383_56e-31;
}
```

위 코드는 qualified name 사용을 피하기 위해서 종종 사용되는 방식입니다. 위 인터페이스를 구현한 클래스는 PhysicalConstants.ELECTRON_MASS로 쓰지 않고 ELECTRON_MASS로 쓰고 싶어서 구현했단 뜻이죠.

### 문제점

1. 일부 constant는 구현의 일부입니다.

   즉, 구현 상세 요소로써, client에게 비공개 되어야 하나 외부 노출되어 캡슐화로 인한 문제가 발생합니다.

2. ConstantInterface를 구현해도 아무 기능이 없기에 혼란을 줄 수 있습니다.
3. 추후에 해당 상수가 필요 없어짐에도 호환성 유지를 위해 반드시 구현해야만 합니다.
4. name space마저 오염될 수 있죠.



### java flatform에서 동일한 문제를 지닌 class

- java.io.ObjectStreamConstants



# ConstantInterface 대안

### 1. constant가 class나 interfcae에 밀접한 관계가 있는 경우

해당 class나 interface에 집어넣으세요.

ex:) Integer, Double => MIN_VALUE, MAX_VALUE



### 2. Enumerated type에게 어울릴 경우

enum type으로 선언



### 3. 그 외의 경우는 utility class로 선언

```java
// Constant utility class (Page 108)
public class PhysicalConstants {
  private PhysicalConstants() { }  // Prevents instantiation

  // Avogadro's number (1/mol)
  public static final double AVOGADROS_NUMBER = 6.022_140_857e23;

  // Boltzmann constant (J/K)
  public static final double BOLTZMANN_CONST  = 1.380_648_52e-23;

  // Mass of the electron (kg)
  public static final double ELECTRON_MASS    = 9.109_383_56e-31;
}
```

대게, qualified name이 필요하지만, static import를 한다면 필요없으니 좋은 대안이 될 수 있습니다.

> 그건 그렇고~ 상수표현 주목
>
> 6.022_140_857e23; 보자! 
>
> _는 literal 값에 영향을 안미치면서 가독성을 높혀준다. 5자 이상이면 적용해보도록 하자!



# 요약

interfaces는 constant를 나타내기 위해 사용되기 보다는 반드시 types를 정의하기 위해 사용되어야 합니다!