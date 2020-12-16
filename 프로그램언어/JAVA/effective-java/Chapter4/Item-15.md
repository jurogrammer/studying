# Minimize the accessibility of classes and members



# 개요

잘 디자인된 컴포넌트와 잘 되지 않은 컴포넌트를 구분 짓는 중요한 요소 중 하나는 바로 encapsulation입니다.



# encapsulation로 인한 decoupling 장점들

encapsulation을 적용하면 컴포넌트간 decoupling을 할 수 있습니다. 이는 독립된 환경에서 developed, tested, optimized, used, understood, and modified를 적용할 수 있게 됩니다.

이러한 decoupling 장점은 다음과 같습니다.

1. system 개발의 속도를 높힐 수 있습니다.

   components들이 병렬적으로 개발되기 때문입니다.

2. 유지보수의 부담을 덜어줍니다.

   컴포넌트를 보다 쉽게 이해할 수 있고 쉽게 디버깅할 수 있으며 문제되는 컴포넌트를 쉽게 교체할 수 있기 때문입니다.

3. encapsulation 그 자체가 성능향상에 도움주진 않지만 도움을 줄 수 있습니다. 

   효율적인 성능 튜닝을 통해서 퍼포먼스 문제가 되는요소를 쉽게 진단할 수 있습니다. 그리고 다른 요소에 영향을 주지 않고 최적화 될 수 있죠.

4. 소프트웨어의 재사용성을 증가시킵니다.

   컴포넌트가 강하게 결합되어 있지 않기 때문이죠.

5. 큰 시스템을 개발할 때 위험을 줄일 수 있습니다.

   시스템은 그렇지 않더라도 개별적인 컴포넌트는 잘 작동되기 때문이죠.



# encapsulation을 위한 접근제어자

자바는 encapsulation을 돕기위한 도구들을 제공하고 있습니다. 이 access control 메커니즘은 class, interface, members의 접근권한을 결정합니다.

그리고 선언을 통해 결정되죠.

그러면, encapsulation을 위한 적절한 사용법을 알아보겠습니다.



#### rule

각각의 클래스와 멤버는 최소한의 접근 권한만을 가지도록 설정해주는 것입니다.



### top-level class,interface의 접근권한

top-level Class는 nested되지 않은 클래스를 의미합니다.

```java
public Foo { // => top level class
  private int a;
  private int b;
}
```



#### 접근권한 종류

package-private과 public만 존재합니다.



#### 선언 방법

public modifier로 선언했다면 public,

package-private으로 선언했다면 package-private이 될 것입니다.



#### 사용 예

package-private

public API가 아닌, 구현 클래스일 경우에 적용합니다. 이를 통해 다음 릴리즈에 삭제한다고할 시엔 기존 client를 신경쓰지 않고 변경가능하게 되죠.

public으로 선언했다면 평생 호환성을 신경쓰며 유지보수할 책임이 뒤따릅니다.



단순히 한 곳에서만 package-private class나 interface를 사용한다면, 사용하는 클래스의 nested class로 만드는 것을 고려해도 좋습니다.

이를 함으로써 다른 곳에서 접근가능성을 줄일 수 있으며, 더 중요한 것은 ... (이해되지 않습니다.)

```
But it is far more important to reduce the accessibility of a gratuitously public class than of a package-private top-level class: the public class is part of the package’s API, while the package-private top- level class is already part of its implementation.
```



이제 top-level class가 가진 member에 대한 접근 권한을 설명드리겠습니다.



### member에 대한 4가지 access level 설명

#### private

해당 멤버는 멤버가 선언된 top-level class에서만 접근 가능합니다.



#### package-private

member가 선언된 package내에서 모두 접근 가능합니다. *default* access라고도 불리죠



#### protected

member가 선언된 subclass와 package내에서 접근 가능합니다.



#### public

어디서든지 접근가능합니다.



### public API 접근제어

public API를 만들땐 모든 멤버는 private로 선언해줍니다. 

만약에~~ 다른 클래스에 정말 접근을 원한다면 package-private으로 바꿔줍시다. 

#### 자주 바꿔주고 있다면?

decoupling할 여지가 있는지 살펴봐야 합니다. 왜냐하면 private와 package-private는 구현의 일부이기 때문에 공개 API에 영향을 주면 안되기 때문이지요.

#### Serializable

serializable을 적용하면 private를 선언했더라도 field값이 노출될 수 있습니다.



### public class의 protected

public class의 접근권한이 엄청 커지는 때가 있습니다. 그건 바로 package-private에서 protected로 변경될 떄이죠.

protected 멤버가 public API class의 일부분이고 영원히 유지보수 해줘야 합니다. 또한 public class의 구현의 일부분이 됩니다.

따라서 protected를 사용하는 일은 드물어야 합니다.



### method 접근제어에 대한 규칙

super class의 method를 오버라이딩한다면 super class의 접근 권한보다 더 큰 권한을 가질 수 없습니다. 

이는 LSP를 지키기 위해 존재합니다. 따라서 이를 위반하면 컴파일러가 경고를 줄 것입니다.



### testing관점에서 접근제어자 설정

테스트를 유용하게 하기 위해 접근 권한을 테스트환경이 아닌 때보다 높게 설정할 수 있습니다. 이는 오로지 테스트를 하기 위해 접근 권한을 높혀야하는 것이지, 마구잡이로 높히면 안됩니다.

```
그런데 보통 신경쓸 필요가 없는게, test package에서 작업하기 때문입니다. ...?
```



### field는 public으로 거의 선언하지 말 것

instance field가 nonfinal이거나 mutable object인데 public으로 만든다면 불변값으로 만들 수 없습니다.

따라서 thread-safe를 구현할 수 없죠.



이는 static field에서도 동일하게 적용됩니다만, 한가지 예외가 있습니다. 이는 상수를 노출할 경우입니다.  static final을 이용하여 값을 노출시킬 수 있으며, 컨벤션을 따라 대문자와 underscore를 이용하여 표현해줍니다.



한편으로, final로 선언하더라도 mutable한 케이스가 있으니 이를 조심해야 합니다.

### array는 항상 mutable하니 조심

길이가 0이 아닌 array는 항상 mutable 합니다! 따라서 array는 public static final로 선언하거나 해당 Field를 반환시키는 accessor를 만드는건 잘못됩니다.

```java
 // Potential security hole!
public static final Thing[] VALUES =  { ... };
```



#### 해결방법

1) 실제 값은 private로 감추고immutable list 반환하기

```java
private static final Thing[] PRIVATE_VALUES = { ... };
   public static final List<Thing> VALUES =
       Collections.unmodifiableList(Arrays.asList(PRIVATE_VALUES));

```



2) 단순히 copy해서 보내기

```java
private static final Thing[] PRIVATE_VALUES = { ... };
public static final Thing[] values() {
  return PRIVATE_VALUES.clone();
}
```



#### 선택기준

1. 클라이언트가 어떤 결과를 더 편하게 생각할지
2. 성능이 더 좋은 방법이 무엇인지



# Java 9의 모듈 시스템

