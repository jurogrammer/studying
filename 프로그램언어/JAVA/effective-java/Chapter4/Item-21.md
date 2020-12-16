# Design interface for posterity

Java 8 이전에는 기존에의 구현을 변경시키지(breaking) 않고는 interface에 method를 추가하는 것이 불가능했습니다. 그래서 method를 interface에 추가하면 해당 인터페이스를 구현하고 있던 클래스에서 추가된 method를 구현하지 않았으니 compile time error가 발생했죠.

따라서 Java 8에서 기존 interface에 method를 추가하는 목적으로 default method를 추가하였습니다.

하지만, 기존 interface에 interface를 넣은 일은 위험한 일입니다.



# default method

### 사용 방식

default method를 선언하면 interface를 구현하는 모든 class는 해당 default method를 사용할 수 있습니다. default method를 구현한 class는 제외하구요.

### 문제

하지만 기존 구현대로 작동하리라 보장할 수 없습니다. Java 8이전엔 Interface에 method가 새로 추가될 것을 전혀 고려하지 않고 개발 되었으니 더더욱 그렇습니다.

### 예시 - Collection의 default method

Collection에 lambda를 사용할 수 있도록 default method가 추가 되었습니다. default는 범용적인 목적으로 만들어졌고 대부분 잘 작동합니다만, 항상 모든 것에 대해 invariant를 해치지지 않도록 만들진 못했습니다.



#### removeIf

```java
default boolean removeIf(Predicate<? super E> filter) {
        Objects.requireNonNull(filter);
        boolean removed = false;
        final Iterator<E> each = iterator();
        while (each.hasNext()) {
            if (filter.test(each.next())) {
                each.remove();
                removed = true;
            }
        }
        return removed;
    }
```

removeIf method의 범용적인 목적을 잘 달성할 수 있는 코드지만, 문제가 있을 수 있습니다.



#### apache에서 만든 SynchronizedCollection

이 collection은 Sync를 위해 Collection을 감싼(wrapper) 클래스입니다. Sync작업을 수행한 뒤 collection에게 위임하죠.

그런데, 위 removeIf라는 default method가 추가된 시점에서 SynchronizedCollection은 removeIf를 wrapping하지 못하고 있습니다.

따라서 SynchronizedCollection의 removeIf를 호출하면 Sync되지 않아 에러를 발생시킬 것입니다.

즉, 아무리 범용성 좋게 default method를 추가하더라도 문제가 될 수 있는 예시입니다.



따라서 이를 막기 위해 removeIf method를 반드시 overriding해야 합니다. 하지만, 기존 클래스들이 발빠르게 업데이트할 수 있는 건 아니지요.

컴파일에 성공하더라도 런타임 중에 에러가 날 수 있으니 쉬운 일이 아닙니다.



### 심사숙고

따라서 기존 Interface에 default method를 추가할 땐 심사숙고 해야 합니다. 하지만, 새로운 interface를 만들 땐 매우 좋은 도구가 될 수 있지요 (Item 20에서 설명)

 

### default method 추가를 피해야할 상황

1. interface로부터 method를 없애기 위해
2. 기존 method signature를 변경하기 위해



### Test

default method를 추가하면 예측하기 어려운 문제가 발생하기 때문에 release전 충분한 테스트를 거쳐야 합니다.

1. 다수의 프로그래머가 다른 방식으로 Interface를 구현해보고
2. 각각의 구현체를 여러 client가 사용해보도록 해야 합니다

