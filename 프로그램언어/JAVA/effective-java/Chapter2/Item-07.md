# Eliminate obsolete object references

## 개요

C++, C언어와 달리 Java에서는 자동으로 메모리를 해제해주는 garbage-collector라는 것이 있습니다. 하지만! garbage collector가 있다고 해서 메모리에 전혀 신경쓰지 않아도 된다는 뜻은 아닙니다.



예시로 설명드리겠습니다.



## 메모리 누수 예시 - Stack

```java
public class Stack {
  private Object[] elements;
  private int size = 0;
  private static final int DEFAULT_INITIAL_CAPACITY = 16;
  public Stack() {
    elements = new Object[DEFAULT_INITIAL_CAPACITY];
	}
  public void push(Object e) {
    ensureCapacity();
    elements[size++] = e;
	}
  public Object pop() {
    if (size == 0)
      throw new EmptyStackException();
    return elements[--size];
	}
  /**
        * Ensure space for at least one more element, roughly
        * doubling the capacity each time the array needs to grow.
        */
  private void ensureCapacity() {
    if (elements.length == size)
      elements = Arrays.copyOf(elements, 2 * size + 1);
	}
}
```

### 위 코드의 영향

겉보기에 전혀 문제없이 잘 작동해보입니다. 

하지만 이 프로그램은 시간이 지날수록 garbage collector의 활동이 증가하고, 메모리를 많이 차지하면서 점점 성능이 줄어들 것입니다. 최악의 경우엔 페이징이나 프로그램이 깨지면서 `OutOfMemoryError`  를 발생시킬 수 있죠.



### 메모리 누수의 위치

stack이 커지고 작아짐에 따라 pop된 Object로 인해 메모리 누수가 발생합니다. 아무리 프로그램이 해당 object의 참조가 없더라도 garbage collect 대상이 아니죠. 



### 누수의 원인

stack이 객체에 쓸모없는 참조(obsolete references)를 때문에 메모리 누수가 발생합니다. 

obsolete reference란 간단히 말해서 다시 역참조될 일이 없는 참조를 말합니다. 위 예제에선 size(active portion) 바깥의 element들이 쓸모없다고 말할 수 있습니다. 더이상 사용하지 않으니까요.



### 쓸모없는 Object의 악영향

메모리 누수(also, unintentional object retentions)는 서서히 문제가 됩니다. 위와 같은 object는 garbage collection 대상에 제외될 뿐더러, 이 쓸모없는 object로 인해 다른 object또한 참조하게 됩니다.

이렇기 때문에 매우 적은 쓸모없는 object가 참조되더라도 수많은 object가 garbage collect되지 않을 수 있습니다.



### 해결 방법 - null 사용

이와 같은 종류의 해결방법은 매우 간단합니다. object가 쓸모없어지게 된다면 null을 통해 참조를 해제하면 됩니다.

위 예제에서는 pop하였을 때 pop한 object는 쓸모가 없어지므로 해당 object참조하는 위치에 null을 할당해주면 됩니다.

```java
public Object pop() {
  if (size == 0)
		throw new EmptyStackException();
  Object result = elements[--size];
  elements[size] = null; // Eliminate obsolete reference return result;
  return result;
}
```

#### null의 또 다른 장점

null의 또다른 장점으로는 실수로 obsolete  references를 역참조하더라도, 프로그램은 NullPointException을 던질 것입니다. 잘못된 작업을 계속하기보다는 프로그램의 에러를 빨리 감지할 수 있기 때문에 항상 옳다고 볼 수 있죠.



#### 과도한 null사용은 자제!

프로그래머가 맨 처음에 이 문제를 맞닿는다면, 모든 object에 null처리를 할 것입니다. 이는 필요도 없고 좋은 방향도 아닙니다. 프로그램을 난잡하게 만들 뿐이죠.

Null처리는 일반적이라기보단 exception상황에 적용해야 합니다.

그래서, 가장 좋은 방법은 참조를 담은 변수를 범위 밖으로 밀어내는 것입니다! 최대한 변수의 scope를 좁게 정함으로써 달성할 수 있죠(Item-57)



#### 그렇다면 언제 null을 사용해야 할까?

Stack class의 어떤 면이 메모리 누수를 발생시키고 있는걸까요?

간단히 말해서, stack이 자기 자신의 메모리를 관리하고 있기 때문입니다.

storage pool(stack)은 elements array의 elements로 구성되어 있습니다. 다시말해서 object그 자체가 아닌, reference로써 가지고 있다는 뜻이죠.

active portion에 있는 elements들은 할당되고 array의 remainder에 있는 elementes는 해제됩니다. 

garbage collector를 이를 전혀 알 길이 없죠. garbage collector가 보기에는 모든 elements array가 타당하다고 봅니다. 프로그래머만 중요하지 않은 array를 알 뿐이죠.

따라서 programmers는 null처리를 하면서 garabage collector와 효과적으로 커뮤니케이션해야 합니다.



일반화시켜, 클래스가 자신의 메모리를 관리할 때마다 프로그래머는 반드시 메모리 누수를 경계해야 합니다.



## Cache에서의 메모리 누수

프로그래머는 object refenrece를 cache에 둘 때, 필요없어질 경우 해제하는 것을 까먹기 마련입니다. 따라서 메모리 누수가 발생하죠.



### 해결 방법

따라서 이 caching으로 인한 메모리 누수를 해결하는 몇가지 방법을 소개드리겠습니다.

#### 1. WeakHashMap이용

reference를 참조하는 동안한 사용한다면 WeakHashMap을 이용하면 됩니다. 담겨져있는 entry는 쓸모없어질 때마다 자동으로 제거될 것입니다.

명심해야할 사항은, cahce entries의 lifetime이 외부에서 value가 아닌, key에 대한 참조를 할 때한 유효하다는 것입니다.

#### 2. aging

보통 cache의 entry의 유효기간을 예측하기 어렵기 때문에 시간이 지날수록 entry의 가치를 떨어트리는 방법을 사용합니다. 백그라운드 쓰레드나(ex: ScheduledThreadPoolExcutor) 

cache를 새로운 entry에 추가시키는 것으로 가능합니다. (ex: LinkedHashMap)

좀 더 정교한 방법을 원한다면 java.lang.ref 를 사용하는 것이 좋습니다.



## Listeners와 Callbacks에서의 메모리 누수

callback을 저장하나, 삭제하지 않는 API를 구현한다면 문제가 되빈다.

이를 예방할 수 있는 방법은 callback에 대한 weak references를 WeakHashMap에 key로 저장하는 것입니다.



## 마무리

메모리 누수는 겉으로는 문제가 되지 않고 서서히 드러나기 때문에 system에 몇 년동안 남아있을 수 있습니다. 

메모리 누수는 정밀한 코드 조사와 heap profiler라는 debuging tool로만 찾아낼 수 있습니다.

그렇기 때문에 문제를 해결하는 방법에 집중하기보다는 메모리누수를 예방하는 것에 집중하는 것이 좋습니다.

