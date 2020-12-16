# Avoid creating unnecessary objects

## 개요

필요할 때마다 기능적으로 동일한 새 objects를 생성하는 것보다 기존에 생성한 objects를 재사용하는 것이 대게 적절합니다. 재사용하는 것은 빠르고 더 스타일리쉬하니까요. 

만약에 object가 immutable하다면 항상 재사용할 수 있습니다.



아무래도 효율적인 코드를 작성하는 것이 이 책의 목표이므로 프로그래머가 흔히 실수하는 예시와 생각하지 못한 부분들도 언급하겠습니다.



## 예시1 - string

### 나쁜 예

```java
String s = new String("bikini");
```

이 statement는 실행될 때마다 새로운 string instance를 생성합니다. 

이 예제는 매우 안 좋은 예입니다. 

`"bikini"`argument는 스스로 string instance일 뿐더러 constructor에 의해 생성된 object와 기능적으로 동일합니다

만약 반복문을 돌리면, 수백만개의 동일한 "bikini" object가 생성되죠.



따라서 이는 다음처럼 개선할 수 있습니다.

### 좋은 예

```java
String s = "bikini";
```

1. 이 방법은 단지 단 하나의 String instance를 사용합니다. 게다가 이는 동일한 JVM환경에 있는 다른 코드가 object가 재사용할것이라 보장할 수 있습니다.

#### static method 사용

생성자보다 static method를 사용해서 필요없는 생성을 피할 수 있습니다.

**good**

```java
Boolean.valueOf(String);
```

**bad**

```java
new Boolean(String);
```



추가로 불변객체 뿐만 아니라 변경되지 않을 것이라고 생각되는 변경가능한 객체도 object를 재사용할 수 있습니다.



## 예시2 - 매우 비싼 생성비용

### 나쁜 예

```java
static boolean isRomanNumeral(String s) {
  return s.matches("불라불라불라")
}
```



비록, string matches method는 문자처리에 좋은 방법이지만, 성능이 중요한 환경에서 반복된 사용은 적절하지 않습니다. 문제는 바로 내부적으로 정규표현식을 위해 Pattern instance를 생성합니다. 그리고 한 번만 사용된 후에 garbage collection의 대상이 됩니다.

Pattern instace를 생성하는 것은 매우 비쌉니다. 왜냐하면 정규표현식을 finite state machine으로 바꾸기 때문이지요!



### 좋은 예

성능을 개선하기 위해선 regular expression을 Pattern instance로 Compile하여 캐싱(immutable)합니다 .그리고 isRomanNumeral을 호출할 때마다 이를 재사용하는 것이죠.

따라서 다음처럼 개선할 수 있습니다.

```java
public class RomanNumerals {
  private static final Pattern ROMAN = Pattern.compile("불라불라불라");
  
  static boolean isRomanNumeral(String s) {
    return ROMAN.matcher(s).matches();
  }
}
```

부수적인 효과는 argument가 깔끔해지고, 이름을 부여함으로써 읽기 좋아졌습니다.



### LazyLoading?

static으로 선언되어 있으므로 한 번도 사용되지 않는다면 lazyLoading을 고려할 수 있겠으나, **추천드리지 않습니다.**

보통 lazyloading을 구현하면 성능이 아주 미미하게 증가하거나 오히려 느려질 수 있습니다.



## 예시3 - 이게 immutable하다니...

immutable하다면 항상 재사용할 수 있다고 말씀드렸습니다. 그런데 직관적으로 Immutable하다고 생각하기 어려운 예가 있습니다. 바로 adapter pattern이지요.

adapter는 user interface로 전달받은 요청을 object에게 delegate(위임)하는 형태를 취합니다. 이때! **adapter가 유지하는 상태정보는 없지요.**

따라서 adapter pattern은 재사용이 가능합니다.



#### adapter exam - Map::keySet method

Map의 keySet method는 Map object의 Map의 key값이 들어있는 set view를 반환합니다.

직관적으로 생각하면 매번 매소드를 호출할 때마다 새로운 view를 반환할 것 같은데, 동일한 Set instance를 반환합니다.



## 예시4 - autoboxing

autoboxing은 프로그래머가 primitive type과 boxing type을 번갈아쓸 때 자동으로 상호변환시켜주는 기술입니다.

autoboxing은 경계를 흐려주지만 두 개의 구분을 없애주는 것이 아닙니다! 즉, 변환이 필요하다는 뜻이죠.

따라서 다음 예는 끔찍한 성능저하를 일으킵니다.

```java
private static long sum() {
  Long sum = 0L;
  for (long i = 0; i <= Integer.MAX_VALUE; i++)
    sum += i;
  
  return sum;
}
```

sum은 boxing타입으로 선언된 반면, i는 primitive 타입입니다. 따라서 매 반복마다 sum + i의 값을 박싱형변환한 객체가 생성됩니다. 이를 개선한다면 6.3sec -> 0.59sec 까지 처리시간을 줄일 수 있지요.

따라서 여기서 얻을 교훈은 boxing보단 primitive타입을 사용하고, 의도치 않은 autoboxing을 예의주시하면 되겠습니다.



## 재사용보다 생성이 더 나은 경우

1. 생성 비용이 매우 작고 
2. 재사용보다는 생성하는 것이 간결해질 경우

이때는 생성하는 것이 낫습니다. JVM성능이 매우 좋아졌기 때문에 퍼포먼스에 큰 영향이 없습니다.



## object pool을 지양하라

object pool은 매우 무겁고, 코드를 지저분하게 만듭니다. 그리고 메모리사용량을 늘리고 성능에 악영향을 끼치죠.



## 마지막으로...

마지막 즈음 이번 아이템과 반대되는 말을 드렸습니다. 재사용보다는 생성을 하라구요. 이는 Item 50에 언급할 내용입니다.

프로그래머는 [생성]과 [재사용] 두 가지 선택지를 잘 고려하여 판단해야 합니다.