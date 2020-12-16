# Favor composition over inheritance

상속은 코드 재사용성에서 강력한 방법이지만 항상 좋은 방법은 아닙니다. 잘못쓰면 고장나기 쉬운 소프트웨어를 만들죠.

상속을 하려면

1. package 내에서만 상속받도록 하거나

2. 상속을 고려한 class에 대해서만 상속을 하는 것이 좋습니다.



이번 아이템에서는 상속이 왜 문제가 되는지에 대해 얘기를 해보겠습니다.(interface 구현은 제외)



# 상속은 encapsulation을 위반합니다.

sub class의 기능이 super class의 구현에 의존하기에 encapsulation을 위반합니다. 매 릴리즈때마다 super class는 변경될 수 있으며 이때 sub class가 망가질 수 있죠. 



이를 자세히 설명하기 위해 HashSet 예제를 설명드리겠습니다.

### HashSet예제

성능 향상을 위해 elements 수를 count에 기록하고 이를 보여주는 methods를 만들겠습니다. 

HashSet class는 add, addAll이란 두 메서드를 가지고 있기에 여기에 오버라이드하여 구현해줍니다.

```java
// Broken - Inappropriate use of inheritance!
public class InstrumentedHashSet<E> extends HashSet<E> {
  // The number of attempted element insertions
  private int addCount = 0;
  public InstrumentedHashSet() {
  }
  public InstrumentedHashSet(int initCap, float loadFactor) {
    super(initCap, loadFactor);
  }
  @Override public boolean add(E e) {
    addCount++;
    return super.add(e);
  }
  @Override public boolean addAll(Collection<? extends E> c) {
    addCount += c.size();
    return super.addAll(c);
  }
  public int getAddCount() {
    return addCount;
  }
}
```

### 문제

딱 보기엔 잘 작동할 것 같은데 문제가 있습니다. 다음 코드를 실행할 때 결과값을 생각해보세요

```java
InstrumentedHashSet<String> s = new InstrumentedHashSet<>();
s.addAll(List.of("Snap", "Crackle", "Pop"));
```

getAddCount() 실행시 3이 나와야할 것 같죠? 원소 3개를 가진 리스트를 집어 넣었으니까요.

하지만 결과는 6이 나옵니다.

내부 구현에서 HashSet addAll은 add를 호출하기 때문이지요. 그래서 중복해서 더해졌던 것입니다.



### side-step

이 문제를 약간 비껴가서 풀어보겠습니다.

#### 1. addAll method의 오버라이드 하지 않기

addAll이 add를 사용하는 것은(self use) 세부 구현 중 하나이므로 언제든지 변경될 수 있습니다. 따라서 fragile하다 볼 수 있죠



#### 2. addAll method에서 add를 iterate하기

각 elements에서 add를 호출하도록 overriding하는 것입니다. 이렇게 하면 첫번째 경우처럼 HashSet의 addAll구현에 종속되지 않죠.

하지만 결국 수퍼 클래스와 같이 어렵고, 시간이 많이 걸리고, 오류가 발생하기 쉽고, 성능 저하될 수 있는 self use를 재구성한것 뿐입니다. 

일부는 sub class가 접근할 수 없는 private field가 있기에 구현할 수 없을 수 있습니다.



#### 관련 문제: super class에서 new method를 생성하는 경우

super class에서 특정 elements에 대해서 collection에 넣는 것을 생각해봅시다. 여기에 타입 체크를 해주는 메서드를  collection에 추가하는 작업을 수행했습니다. 

차후 릴리즈에 super class에서 새로운 메서드로 인해 illegal한 원소가 될 수 있습니다. sub class에선 이를 오버라이딩 하지 않았기 때문이지요.

실제로 hashTable과 Vector를 Collection frame work로 들여오기 위해 리폼할 때 이러한 보안 구멍을 고쳐야 했습니다.



이러한 문제들은 methods를 overrding함으로써 발생하죠. 그렇다면 overiding을 하지 않으면 괜찮을까요?

### overriding을 하지 않고도 문제되는 케이스

sub class가 새로운 메서드를 정의했다고 합시다. 그런데 차후 super class에서 동일한 signature를 만들었는데  return type이 다르다면?

compile error가 발생하게 되죠. 

그리고 return type이 아무리 동일하다 하더라도 super class의 기능과 동일하게 작동하리란 보장이 없습니다.



# composition을 이용한 해결

상속하는 것보다 composition을 이용해서 해결할 수 있습니다.



### composition 구현

기존에 있는 클래스를 private field reference로 두어서 구현할 수 있지요.



### forwarding

새로운 클래스의 instance method는 기존에 정의된 instance의 method들을 실행하고 해당 결과를 반환하는 형태가 됩니다. 이는 ***forwarding***이라 부르며 새로운 class의 method를 ***forwarding method***라 부릅니다.



### 이점

기존 클래스의 구현 세부사항에 의존하지 않을 수 있게 됩니다. 새로운 클래스에서 새로운 method를 추가하더라도 문제가 없죠!





### 구현

InstrumentedHashSet로 예를 들어 구현해보겠습니다. 구현은 2가지로 나뉩니다. 하나는 InstrumentedHashSet그 자체이며, 다른 하나는 forwarding class를 구현해야하는 것입니다.

forwarding class는 forwarding method말고는 다른게 없습니다.

#### Wrapper class

```java
// Wrapper class - uses composition in place of inheritance
public class InstrumentedSet<E> extends ForwardingSet<E> {
  private int addCount = 0;
  public InstrumentedSet(Set<E> s) {
    super(s);
  }
  @Override public boolean add(E e) {
    addCount++;
    return super.add(e);
  }
  @Override public boolean addAll(Collection<? extends E> c) {
    addCount += c.size();
    return super.addAll(c);
  }
  public int getAddCount() {
    return addCount;
  }
}
```



#### forwarding class

```java
// Reusable forwarding class (Page 90)
public class ForwardingSet<E> implements Set<E> {
    private final Set<E> s;
    public ForwardingSet(Set<E> s) { this.s = s; }

    public void clear()               { s.clear();            }
    public boolean contains(Object o) { return s.contains(o); }
    public boolean isEmpty()          { return s.isEmpty();   }
    public int size()                 { return s.size();      }
    public Iterator<E> iterator()     { return s.iterator();  }
    public boolean add(E e)           { return s.add(e);      }
    public boolean remove(Object o)   { return s.remove(o);   }
    public boolean containsAll(Collection<?> c)
                                   { return s.containsAll(c); }
    public boolean addAll(Collection<? extends E> c)
                                   { return s.addAll(c);      }
    public boolean removeAll(Collection<?> c)
                                   { return s.removeAll(c);   }
    public boolean retainAll(Collection<?> c)
                                   { return s.retainAll(c);   }
    public Object[] toArray()          { return s.toArray();  }
    public <T> T[] toArray(T[] a)      { return s.toArray(a); }
    @Override public boolean equals(Object o)
                                       { return s.equals(o);  }
    @Override public int hashCode()    { return s.hashCode(); }
    @Override public String toString() { return s.toString(); }
}
```

이 구현은 InstrumentedSet class가 Set interface를 통해 가능하게 되었습니다. Set은 HashSet의 functionality를 가지고 있으니까요.



이 방법은 로버스트하고 유연합니다.

InstrumentedSet class는 Set interface를 구현했으며, 단일 constructor 또한 type이 Set인 것을 받을 수 있습니다. 

본질적으로 이 클래스는 하나의 set에서 다른 set으로 변경될수 있습니다.'



상속 기반 접근과 달리, single concrete class에 대해서만 작동할 것이며 wrapper class는 어떤 Set implementation을 사용할 수 있을 것입니다.

```java
Set<Instant> times = new InstrumentedSet<>(new TreeSet<>(cmp));
Set<E> s = new InstrumentedSet<>(new HashSet<>(INIT_CAPACITY));
```



```java
static void walk(Set<Dog> dogs) {
  InstrumentedSet<Dog> iDogs = new InstrumentedSet<>(dogs);
  ... // Within this method use iDogs instead of dogs
}
```

여기보면 Set타입의 dogs가  InstrucmentedSet타입의 iDogs가 된것으로, decorator pattern으로 볼 수도 있습니다.



# wrapper class 문제

callback framework에선 적합하지 않다.

(Self problem)



# composition 쓸 곳에 inheritance쓸 때 문제

필요없이 구현을 노출하게 됩니다. 따라서 Client가 이것을 사용해서 poerfeormance향상을 할 수 없게 됩니다. 더 심각한 경우에는 직접적으로 구현에 접근하는 것을 허용할 수 있습니다. 따라서 의미에 혼동을 줄 수 있죠.

#### 예시 - Properties class

변수 p가 Properties instance를 가리킬 때, p.getProperty(key)와 p.get(key)는 다른 결과를 부를 수 있습니다. 전자는 default이며, 후자는 Hashtable을 가져옵니다.

더 심각하게는 super class를 직접적으로 수정함으로써 sub class의 불변식을 망가뜨릴 수 있습니다.  
Properties에서 디자이너가 오직 하나의 string 값을 받도록 하였지만, Hashtable을 직접적으로 접근할수 있음에 따라 문제가 됩니다.



# Inheritance의 적합성 판단

1. 정말 subtype인가? 

   is-a 관계 및, LSP 준수 고려

2. API에 결점이 있고, 이것이 sub class에 전파되도 상관없는가?



# 요약

inhertance는 강력하지만 encapsulation 측면에서 문제가 많습니다.

사용할 때는 정말 subtype 관계인지 판단해야 하며, 판단 하더라도 동일 package 내에서 관리해주어야 합니다.

이러한 취약성을 피하기 위해선 composition and forwarding을 이용하는 것이 좋습니다. wrapper class의 적절한 interface가 있는 경우에요

이렇게하면 로버스트하며 파워풀해집니다.