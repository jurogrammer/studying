# Override clone judiciously

## 개요

Cloneable interface는 cloning을 허용하는 것을 알리기 위해 만들어졌습니다. 하지만 다음과 같은 문제점들이 있지요.

1. 정작 Cloneable엔 clone 메서드가 없으며 Object에 protected로 clone이 제공되어 문제가 있습니다.

   따라서 Cloneable을 구현하는 것만으로는 clone이 작동하리라 보장할 수 없습니다.

2. 리플렉션을 이용해도 clone이 접근가능하게 선언되어있으리라 보장할 수 없어서 문제가 됩니다.

하지만 이러한 문제에도 불구하고 널리 사용되고 있습니다. 따라서 어떻게 clone을 구현해야 하는지, 언제 이렇게 하는 것이 적절한지, 그리고 대안을 말씀드리겠습니다.



**cloneable 미구현 실행**

![](https://postfiles.pstatic.net/MjAyMDExMzBfMTI5/MDAxNjA2NzAwNjcyNDM2.0-yhuRYhJcP_UIfmXicd4OE7bsN___VUcR6MBhqksR8g.nE5QmWK1LgOJw0Q87aQsF9cRQuBmbo2GR8nvZ2MiC60g.PNG.study_ju/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2020-11-30_%EC%98%A4%EC%A0%84_10.43.33.png?type=w966)



**cloneable구현 실행**

![](https://postfiles.pstatic.net/MjAyMDExMzBfMTYy/MDAxNjA2NzAwNjczNjc0.3n7Srg0CF6CZu8CxD-ispc_VnqZqlOFAt3N_DbaWCGYg.9I0c_WKj3WPyMWX2EK6yzeMm18f2OgOOFCxloxnvrqMg.PNG.study_ju/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2020-11-30_%EC%98%A4%EC%A0%84_10.43.55.png?type=w966)



## Cloneable 역할

아무런 메서드없는 cloneable은 clone의 작동방식을 결정합니다. 이를 구현한 클래스의 객체에서 clone을 실행하면 필드를 하나하나씩 복사하여 객체를 반환해줍니다. 그렇지 않으면 ClassNotSupportedException을 던지죠

인터페이스는 클래스의 행동을 정해야 하는데, 자기가 일을 하는 형태는 이례적이므로 이와같이 구현하면 안됩니다.



## Cloneable의 허술성

### 실무관점 문제

Cloneable을 구현하면 clone method를 적절하게 제공할 것처럼 예상되는데, 그렇지 못합니다. 이를 구현하려면 복잡한 규약을 지켜야합니다.

그런데 constructor를 사용하지 않았으므로 위험하고 깨지기 쉬운 프로그램이 되죠.



### 규약

규약은 강제성이 없습니다. 약한 편이죠.

https://docs.oracle.com/javase/7/docs/api/java/lang/Object.html (clone 참조)

그래서 clone method실행시 super.clone()을 해도 되고, 생성자로 만들어 반환시켜도 됩니다.

하지만! 생성자로 반환하도록 한다면, 이 클래스의 서브클래스에서 clone을 오버라이딩하여 super.clone()을 호출한다면 생성자로 인해 super class의 타입으로 반환되므로 문제가 됩니다.



## clone method 상속받아 Cloneable 구현하기

### 불변 객체 참조시 구현

불변 객체라면 복사하는 것이 무의미하긴 하지만, 이를 구현하면 다음과 같습니다.

#### 절차

##### 1. super.clone 호출

Object의 clone 메서드를 호출한다.



##### 2. PhoneNumber의 clone 메서드 구현

```java
@Override public PhoneNumber clone() {
       try {
           return (PhoneNumber) super.clone();
       } catch (CloneNotSupportedException e) {
           throw new AssertionError();  // Can't happen
       }
}

```

오버라이딩하여 clone을 구현한다. 클라이언트에서 캐스팅하지 않도록 PhoneNumber type으로 반환시켜준다. 자바는 공변타입을 지원하기에 가능하다.



super.clone()이 try-catch로 감싼 이유는 clone실행시 CloneNotSupprtedException이란 checked exception이 발생하기 때문이다.

그런데 cloneable을 구현해서 이미 잘 작동되리라 알고 있기 때문에 지저분해진 코드의 예시라 볼 수 있습니다.



##### 3. Cloneable 구현

clone메서드가 정상작동되기 위해 Cloneable을 구현하도록 한다.



### 가변객체 참조시 구현 (여러가지 해결 방법을 보여줌)

불변 객체를 clone할 시엔 문제가 없는데, 가변객체를 참조한다면 문제가 된다.

#### 문제되는 예시

```java
public class Stack {
	private Object[] elements;
	private int size = 0;
	private static final int DEFAULT_INITIAL_CAPACITY = 16;
	public Stack() {
		this.elements = new Object[DEFAULT_INITIAL_CAPACITY];
	}
  public void push(Object e) {
    ensureCapacity();
    elements[size++] = e;
	}
  public Object pop() {
    if (size == 0)
      throw new EmptyStackException();
    Object result = elements[--size];
    elements[size] = null; // Eliminate obsolete reference
    return result;
	}
  // Ensure space for at least one more element.
  private void ensureCapacity() {
    if (elements.length == size)
      elements = Arrays.copyOf(elements, 2 * size + 1);
	}
}
```

이놈을 보면 elements를 복사할 땐 안의 값들은 shallow copy가 된다. 따라서 Stack 객체를 생성하더라도 elements의 동일한 객체의 주소를 바라보기 때문에 문제가 된다.



만약에 clone method가 단일 constructor을 제공했다면 문제가 되지않았을 것이다. 다시 말해서 clone method는 origin object에 영향이 없고, 불변 객체를 적절하게 생성해야 한다.

이를 달성하기 위해선 stack의 내부 값을 복사하도록 하면 된다.

#### 해결 방법

```java
// Clone method for class with references to mutable state
@Override public Stack clone() {
  try {
      Stack result = (Stack) super.clone();
      result.elements = elements.clone();
      return result;
  } catch (CloneNotSupportedException e) {
	    throw new AssertionError();
  }
}
```

##### 주안점

1. elements의 compile time과 run time의 타입이 같기 때문에 캐스팅할 필요 없습니다.

   이 때문에 배열을 복사할 때는 clone메서드를 유일하게 사용하기 적합한 예라고 볼 수 있습니다.

2. elements는 가변객체이기에 일반 관례를 따른다면 final로 구현될 수도 있지만, 위처럼 복사하고 싶은 경우엔 제거하여 구현하면 된다.



#### 또 다른 문제

재귀 호출로만 충분하지 않은 예도 있습니다.

해쉬 테이블용 clone method를 예시로 들어보겠습니다.

```java
public class HashTable implements Cloneable {
    private Entry[] buckets = ...;

    private static class Entry {
        final Object key;
        Object value;
        Entry next;

        Entry(Object key, Object value, Entry next) {
            this.key = key;
            this.value = value;
            this.next = next;
        }
    }

    // Broken clone method - results in shared mutable state!
    @Override
    public HashTable clone() {
        try {
            HashTable result = (HashTable) super.clone();
            result.buckets = buckets.clone();
            return result;
        } catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }
    }
}
```



해쉬 테이블에 element로 linked-list가 들어가있는 형태를 봅시다. 이것이 버킷이 됩니다.

위처럼 clone을 한다면 내부가 또 리스트이기 때문에 결국 shallow copy를 할 수 밖에 없죠.



#### mutable object 구현 - recursion

 따라서 내부에 deepcopy를 구현해야 하죠.

```java
public class HashTable implements Cloneable {
    private Entry[] buckets = ...;

    private static class Entry {
        final Object key;
        Object value;
        Entry next;

        Entry(Object key, Object value, Entry next) {
            this.key = key;
            this.value = value;
            this.next = next;
        }

        // Recursively copy the linked list headed by this Entry
        Entry deepCopy() {
            return new Entry(key, value,
                    next == null ? null : next.deepCopy());
        }
    }

    @Override
    public HashTable clone() {
        try {
            HashTable result = (HashTable) super.clone();
            result.buckets = new Entry[buckets.length];
            for (int i = 0; i < buckets.length; i++)
                if (buckets[i] != null)
                    result.buckets[i] = buckets[i].deepCopy();
            return result;
        } catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }
    }
       ... // Remainder omitted
}
```

하지만 이와 같이 구현한다면 버킷이 길다면 stack overflow가 발생할 여지가 있습니다. 따라서 iteration을 통해 개선할 수 있죠.



#### mutable object 구현 - iteration

```java
Entry deepCopy() {
  Entry result = new Entry(key, value, next);
  for (Entry p = result; p.next != null; p = p.next)
		p.next = new Entry(p.next.key, p.next.value, p.next.next);
  return result;
}
```



#### mutable object 구현 - super.clone

고수준 API를 이용하여 clone을 구현하는 방법

1. super.clone으로 필드 초기화
2. put(key, value)같은 고수준 method를 통해 deep copy를 진행해줍니다.

매우 간단하게 만들어 주지만 속도가 느리고, cloneable이 field를 단계단계 생성해준다는 architecture에는 어울리지 않게 됩니다.



### 주의 사항

#### 1. clone은 overridable method를 호출하면 안됩니다.

하위 클래스에서 clone에서 호출했던 method를 오버라이딩한다면 꼬일 수 있겠죠. 따라서 supe.clone에서 put(key, value) method를 호출했다면 이것은 private이나 final로 선언하여 오버라이딩을 막아야 합니다.



#### 2. overriding method는 CloneNotSupportedException을 던지지 않도록 합니다.

Object에서는 clone not supportedException을 던지나, sub class에서는 public으로 선언하고 checked exception을 던지지 않도록 합니다. 사용의 편리성을 위해서지요.



#### 3. clone 상속 구현 방법

공통적으로 Cloneable을 구현하면 안됩니다.

##### 1) Object방식 모방

clone을 제대로 구현한 뒤 protected로 선언. 그리고 CloneNotSupprtedException을 던지도록 한다.

Object처럼 cloneable 구현여부를 sub class에서 선택할 수 있도록 함.



##### 2) clone 막기

final로 막고 에러를 던지도록 합니다.

```java
@Override
protected final Object clone() throws CloneNotSupportedException {
       throw new CloneNotSupportedException();
   }

```



#### 4. thread-safe class로 만들 것.

clone은 synchronized를 고려하지 않았기 때문에 이를 고려해주어야 한다.





## 이 복잡한 과정들이 모두 필요할까?

이러한 경우는 드뭅니다.

단지 cloneable을 확장한 클래스를 상속받는다면 어쩔수없이 clone을 구현해주어야 합니다.

이 외 대다수 경우의 접근은 copy constructor나 copy factory를 제공해주는 것입니다. (더 정확한 이름은 conversion constructor, conversion factory)

copy constructor는 단순히 자기 자신의 필드와 동일한 필드를 생성해주는 생성자를 의미합니다.

```java
// Copy constructor
   public Yum(Yum yum) { ... };
A copy factory is the static factory (Item 1) analogue of a copy constructor:
   // Copy factory
   public static Yum newInstance(Yum yum) { ... };

```



### 이점

1. 언어 모순적이고 위험천만한 객체 생성 매커니즘 사용 안함
2. 엉성한 문서 규약 기대지 않음
3. 정상적인 final field용법과 충돌되지 않음
4. 불필요한 checked exception을 던지지 않음
5. casting도 필요없음

6. interface 타입의 인스턴스를 인수로 받을 수 있다.

   이로 인해 HasSet 객체를 TreeSet으로 변환 가능

