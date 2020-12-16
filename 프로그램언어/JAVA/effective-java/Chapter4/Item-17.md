# Minimize mutability

immutable class는 instances가 변경될 수 없는 클래스를 의미합니다.

그래서 object에 있는 정보들이 죽을 때까지 변경될 일이 없지요.

java library에서 제공하는 immutable class

1. String
2. boxed primitive classes
3. BigInteger, BigDecimal



Immutable class를 만드는 이유는 mutable class보다 디자인하기 쉽고, 구현하기 쉽고 사용하기 쉽기 때문입니다. 에러가 날 일이 거의 없고 보다 안전합니다.



# immutable class를 만드는 규칙

#### 1. object의 상태를 변경시키는 method를 제공하지 마라

#### 2. class를 상속받지 못하도록 하라

sub class에서 부주의하거나 나쁜 의도로 상태를 변경하는 것을 막아준다.

#### 3. 모든 필드는 final로 선언하라

시스템이 강제하는 수단을 사용해 설계자 의도 명확히 드러내는 방법.  생성된 객체를 동기화없이 다른 쓰레드에 보낼 때도 잘 작동하게끔 보장하는데도 필요

#### 4. 모든 필드를 private로 선언하라

​	client에서 필드를 직접 수정하는 것을 막아줌.

#### 5. mutable component에 접근할 수 없도록 한다.







# immutable class인 복소수 클래스 예제

```java
public final class Complex {
    private final double re;
    private final double im;

    public Complex(double re, double im) {
        this.re = re;
        this.im = im;
    }

    public double realPart() {
        return re;
    }

    public double imaginaryPart() {
        return im;
    }

    public Complex plus(Complex c) {
        return new Complex(re + c.re, im + c.im);
    }

    public Complex minus(Complex c) {
        return new Complex(re - c.re, im - c.im);
    }

    public Complex times(Complex c) {
        return new Complex(re * c.re - im * c.im,
                re * c.im + im * c.re);
    }

    public Complex dividedBy(Complex c) {
        double tmp = c.re * c.re + c.im * c.im;
        return new Complex((re * c.re + im * c.im) / tmp,
                (im * c.re - re * c.im) / tmp);
    }

    @Override
    public boolean equals(Object o) {
        if (o == this)
            return true;
        if (!(o instanceof Complex))
            return false;
        Complex c = (Complex) o;
        // See page 47 to find out why we use compare instead of == 
        return Double.compare(c.re, re) == 0 && Double.compare(c.im, im) == 0;
    }

    @Override
    public int hashCode() {
        return 31 * Double.hashCode(re) + Double.hashCode(im);
    }

    @Override
    public String toString() {
        return "(" + re + " + " + im + "i)";
    }
}
```

### 설명

* 이 클래스는 복소수를 표현한다.
* Object method를 오버라이드했고
* 실수부, 허수부 값을 반환하는 accessor 제공
* 사칙연산 메서드 정의



# Functional approach

이 클래스에서 주목할 부분은 사칙연산할 때 자신의 값을 수정하여 반환하기보다는 새로 객체를 생성하는 부분입니다. 이러한 방식은 functional 접근이라고 부릅니다.

이와 같은 방식은 object를 immutable하게 되는 비율을 높혀줍니다.



> functional하게 값을 반환한다는 것을 나타내려고 add라는 Verb대신 plus아는 prepositions를 사용했습니다. BigInteger나 BigDecimal은 이런 네이밍 컨벤션을 따르지 않아 수많은 사용 에러를 발생시킵니다.

# immutable의 장점과 단점

### 장점

#### 1. simple

생성 순간부터 값이 변하지 않기 때문에 다루기 쉽습니다. 반면, 가변 객체라면 상태값이 복잡한 임의의 상태에 남을 수 있기 때문에 어려워지죠.

#### 2. thread-safe

여러 쓰레드가 동시에 사용해도 문제가 없습니다. 

##### 재사용

따라서 Immutable class의 Instance는 재사용 되어야 합니다. 재사용하기 쉬운 방법으로는 static final constants로 선언하는 방법이 있습니다.



위 방법에서 더나아가 static facotries를 제공할 수 있습니다. 값을 보내기 전에 캐싱한 값을 보냄으로써 재사용하는 것이죠



불변 클래스에선 방어적 복사가 필요없게 되므로 clone이나 복사 생성자 제공할 필요가 없게 됩니다. String class의 복사 생성자는 이러한 특징을 잘 이해하지 못하여 복사 생성자를 만들었으니 사용하지 않도록 합니다.



#### 5. immutable instance는 자유롭게 공유할 수 있고, 불변 객체끼리는 내부 데이터를 공유할 수 있음.

#### 6. Immutable objects는 다른 objects에게 좋은 구성요소가 된다.

구조가 복잡하더라도 불변식을 유지하기 쉬워짐.

Map과 Set의 원소로 사용하기에 좋음. 안에 담긴 값이 허물어지면 안되므로.

#### 7. 실패 원자성을 보장함

exception이 발생해도 값이 변하지 않음을 보장한다는 의미입니다.



### 단점

#### 다른 값마다 새로운 객체를 생성해야 합니다.

주로 문제되는 부분이 multistep operation입니다. 중간에 만들어진 값은 모두 버려지면 성능 문제가 더욱 심각해지죠.

#### 해결 방법

* 이는 다단계 연산을 예측하는 mutable Companion class를 package-private으로 둠으로써 해결할 수 있습니다. BigInteger는 이러한 클래스를 두고 있습니다. (String에선 StringBuilder)

* 만약에 다단계 연산을 예측할 수 없다면 public으로 두는 것이 최선의 방법입니다.



# immutable 구현

구현시 주의점: immutable class를 보장하기 위해선, 해당 클래스를 상속받을 수 없도록 만드는 것이 핵심입니다. 



### 상속 방지

### 1. final로 선언하기

강경한 방법.

### 2. private이나 package-private으로 선언하기

final보다는 생성자를 private이나 package-private으로 선언하고, 생성은 static factory가 맡도록 하는 것이죠.

#### 예시

```java
public class Complex {
  private final double re;
  private final double im;
  private Complex(double re, double im) {
    this.re = re;
    this.im = im;
  }
  public static Complex valueOf(double re, double im) { 
    return new Complex(re, im);
  }
       ... // Remainder unchanged
}
```

#### 장점

이 방법은 package-private 구현 클래스를 사용할 수 있도록 해주며, client에겐 생성할 수 없으니 사실상 final class로 보이게 된다.

또한 캐싱하여 값을 보낼 수 있기 때문에 추후 성능향상을 시킬 수도 있다.



#### 잘못된 예 - BigInteger와 BigDecimal

초기에 final로 선언되어야 한다는 것을 몰라서 메서드들이 오버라이드 가능하게 선언되었다. 하위 호환성 때문에 아직까지도 고쳐지지 않았다.

따라서 BigInteger나 BigDecimal의 값을 client로부터 받는다면 정말 해당 클래스인지 반드시 검증하는 과정이 필요하다. 만약에 잘못된 객체라면 방어적 복사를 실행해야 한다.

```java
public static BigInteger safeInstance(BigInteger val) {
       return val.getClass() == BigInteger.class ?
               val : new BigInteger(val.toByteArray());
}
```



# 완화된 immutable 생성 Rule

모두 final로 선언하라는 것은 오바임. 퍼포먼스 향상 위해서는 완화시킬 필요가 있음.

완화된 룰 -> 어떤 메서드도 객체의 상태 중 외부에서 비치는 값을 변경할 수 없다. (no method may produce an externally visible change in the object's state.)



### 룰을 완화한 이유

nonfinal을 선언함으로써 caching할 수 있음.



### 예시 - PhoneNumber

처음 불릴 때 hashCode값을 생성후 캐싱하여 해당 값을 전달해줄 수 있음.

String에서도 이러한 lazyloading방식을 사용함.



# Getter Setter

mutable로 만드는 합리적인 이유가 있지 않다면 getter 만들었다고 setter만들지 마라.  setter는 클래스를 변경시키기 때문이다.

자바 라이브러리 중 java.util.Date, java.awt.Point는 불변이여야 하나 가변으로 잘못만드러졌다.

String이나 BigInteger처럼 무거운 클래스도 불변으로 제공할 수 있는지 생각해보고 없다면 가변 companion 클래스를 제공해주자.



# immutability가 비실용적인 경우

### 대처 방법

1. class가 immutable을 만들 수 없다면, mutablility를 최소한으로 하세요.
2. construtor는 모든 불변 값을 초기화시켜야 합니다.

3. 다른 이유가 없다면 constructor와 static factory 외에는 초기화 메서드를 public으로 제공해서는 안된다.



### 잘 적용된 예 - CountDownLatch

가변 클래스이나 변경가능한 상태를 많이 가지지 않는다. 

그리고 인스턴스를 생성하여 한 번 사용하면 그걸로 끝이 된다.



# 마지막으로

Complex class는 비실용적인 클래스니까 참고만 하라.