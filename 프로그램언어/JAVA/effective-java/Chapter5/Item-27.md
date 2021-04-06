# Eliminate unchecked warnings

generics로 프로그래밍할 때 다음과 같은 경고문들을 볼 수 있습니다.

* unchecked cast warnings
* unchecked method invocation warnings
* unchecked parameterized vararg type warnings
* unchecked conversion warnings



한 번에 깨끗하게 컴파일되길 기대하기 어렵습니다. 그런데, 대부분 컴파일러가 띄워준 경고를 보고 알려준대로만 수정한다면 경고가 사라지죠.

( `javac` 명령줄에 `-Xlint:uncheck` 인수를 추가해주면 컴파일러가 무엇이 잘못됬는지 알려줍니다.)

> lint: 소스 코드를 분석하여 프로그램 오류, 버그, 스타일 오류, 의심스러운 구조체에 표시(flag)를 달아놓기 위한 도구를 가리킨다. 이 용어는 C 언어 소스 코드를 검사하는 유닉스 유틸리티에서 기원한다. - wikipedia
>
> X:  The nonstandard options begin with `-X` . - docs.oragle 
>
> javax : java extention package



하지만, 비검사 경고를 제거하기 힘든 경우가 있지요. 이번 아이템에서는 그 예제를 들고 설명드리도록 하겠습니다.

모두 제거한다면, 타입 안전성을 보장해준다는 뜻이므로, 최대한 없애기 위해 노력해봅시다!



# @SuppressWarnings

### 사용하는 이유

이를 적용해서 덜 중요한 warnings은 가리고, 중요한 warnings를 볼 수 있도록 해야 합니다.



### 사용할 때

경고를 제거할 수 없다고 판단되나, 왜 typesafe 경고를 내뱉는지 증명할 수 있다면 `@suppressWarnings("unchecked")`를 써서 경고를 숨기도록 합시다.

증명을 하지 않는다면 런타임 중 `ClassCastException` 을 던질 수 있다고 볼 수 있죠.



### 선언 위치

개별 local variable 선언부터 class 전체까지 사용될 수 있습니다. 중요한 점은 항상 가장 좁게 scope를 한정 지어야 한다는 점입니다.(Always use the SuppressWarnings annotation on the smallest scope possible.)

따라서 클래스에 다는 것은 지향하도록 하고, 한줄이 넘는 메서드나 생성자에 달린 애너테이션은 지역변수 선언 쪽으로 옮기도록 합니다.



### 예 - toArray method

```java
public <T> T[] toArray(T[] a) {
       if (a.length < size)
return (T[]) Arrays.copyOf(elements, size, a.getClass()); System.arraycopy(elements, 0, a, 0, size);
if (a.length > size)
          a[size] = null;
       return a;
}
```

![스크린샷 2020-12-18 오전 10.57.26](/Users/ju/Library/Application Support/typora-user-images/스크린샷 2020-12-18 오전 10.57.26.png)



위 코드를 컴파일하려고 하면 아래와 같은 경고를 내뱉습니다.

```
ArrayList.java:305: warning: [unchecked] unchecked cast
return (T[]) Arrays.copyOf(elements, size, a.getClass());
									    	  ^
     required: T[]
     found:    Object[]
```



애너테이션은 선언문에만 달 수 있으므로 return에 달긴 어렵습니다. 그렇다고 메서드에 달지는 마시고 return 값을 담을 지역변수를 선언하여 그곳에 애너테이션을 달도록 합니다.

```java
public <T> T[] toArray(T[] a) {
    if (a.length < size) {
        @SuppressWarnings("unchecked") T[] result =
          (T[]) Arrays.copyOf(elements, size, a.getClass());
        return result;
    }
    System.arraycopy(elements, 0, a, 0, size);
    if (a.length > size)
        a[size] = null;
    return a;
}
```



### 주석

애너테이션을 달았다면 경고를 무시해도 되는 이유를 꼭 달아주도록 합시다.

1. 이 코드를 이해하는데 도움이 될 수 있습니다
2. 다른 사람이 잘못 수정해서 unsafe되는 것을 방지할 수 있습니다.





### 마지막으로

최대한 안전한 이유를 찾아서 주석을 달도록 합시다. 그 과정에서 결국 안전하지 않다는 것으로 이해할 수도 있기 때문이지요.