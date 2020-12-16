# 참고 자료

* https://refactoring.guru/design-patterns/singleton
* https://en.wikipedia.org/wiki/Singleton_pattern
* https://jeong-pro.tistory.com/86



# 싱글톤 패턴이란?

* 생성 디자인 패턴
* 클래스가 하나의 object를 가지도록 하고, 이 인스턴스에 전역 접근을 허용하는 디자인



# 이 패턴은 언제 쓰일까?

1. DB접근처럼 하나의 인스턴스만 가지도록 하는 경우
   * dataSource
2. 하나의 인스턴스에 전역 접근 허용
   * 관련있는 instance들을 묶어놓은 클래스로 제공하기 위함.





# 구조

<img src="https://refactoring.guru/images/patterns/diagrams/singleton/structure-en-indexed-2x.png" style="zoom:50%;" />

1. client가 클래스를 통해 객체를 생성하지 못하도록 생성자를 private로 선언합니다.
2. 객체를 받을 수 있는 필드를 private로 선언 합니다.
3. static creation method를 public으로 만듭니다.(`getInstance()`) 그리고 client에서 이 메서드를 호출했을 때 생성된 객체가 없으면 생성하여 field에 저장한 뒤, 그 객체를 반환해줍니다. 객체가 있는 경우에도 마찬가지로 필드에 저장된 객체를 반환합니다.



# 구현

구현시 주의해야할 부분은 thread safe관점에서 instance를 중복하여 생성하는 것을 방지하는 것입니다.

### 관점 1 instance 중복 생성 방지

#### 구현 1 생성 부분에 block

```java
public class Singleton {
    private static Singleton instance;

    private Singleton(){}

    public static synchronized Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```

thread lock을 이용하여 instance를 중복하여 사용할 수 없도록 합니다.

하지만 이 방법을 쓰면 느립니다.



#### 구현 2 doublechecking

```java
public final class Singleton {

    private static volatile Singleton instance = null;

    private Singleton() {}

    public static Singleton getInstance() {
      //이미 인스턴스가 생성된 경우 빠르게 인스턴스 리턴.
        if (instance == null) {
          //생성이 안됬을 경우엔, 동시접근 제어
            synchronized(Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }

        return instance;
    }
}
```

* 구현1의 속도 개선 버전

####  

#### 구현 3 field eager loading

```java
public final class Singleton {
		//eager loading
    private static final Singleton INSTANCE = new Singleton();

    private Singleton() {}

    public static Singleton getInstance() {
        return INSTANCE;
    }
}
```

static으로 선언된 필드를 통해 클래스 생성시 객체 생성하도록 한다.



#### 구현 4

```java
public class Singleton {
    private Singleton() {
    }
 
    private static class LazyHolder {
        public static final Singleton INSTANCE = new Singleton();
    }
 
    public static Singleton getInstance() {
        return LazyHolder.INSTANCE;
    }
}
```

내부에 클래스를 선언하여 객체를 사용할 시점에 클래스 로딩하도록 합니다.





# 단점

* 테스트하기 어렵습니다.

  보통 TestFramework에서 unitTest를 할 땐 객체를 생성하여 테스트하나 싱글톤은 생성자가 private로 막아져 있기에 불가능합니다.



# 연관된 디자인 패턴

* Abstract Factories, Builders, Prototypes는 싱글톤으로 구현될 수 있습니다.