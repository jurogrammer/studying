# Prefer interfaces to abstact classes

Java는 다중 구현을 허용하는 type을 정하기 위해 interface와 abstract 두 메커니즘을 제공합니다. 

java 8에서 interface에 default 메서드를 허용함으로써, 두 매커니즘 모두 인스턴스 메서드를 구현가능하게 되었습니다. 

둘 다 Functionality를 받을 수 있는 공통점이 있지만 극명한 차이점이 존재합니다.



# Abstract class와 interface class의 차이점

### Abstract class

#### 1. 기능을 물려 받기 위해서는 abstract class와 hierarcy관계가 되어야만 합니다.

#### 2. 자바에서 상속은 단일 상속만 허용하므로 한 클래스로부터만 기능을 물려받을 수 있죠.

#### 3. nonhierarcy를 만드려면 2^n만큼 클래스를 생성해주어야 합니다.

나타내야 할 n개의 속성이 있다면 n개 속성이 있는지 없는지로, 2^n개의 클래스를 생성해주어야 하지요. 이것은 combinatiorial explosion이라 불립니다. 그리고 메서드는 특정한 특징을 가진 클래스의 arguments만 달라질 수 있습니다. 공통 타입의 메서드를 만들 수 없으니까요.



이에 반면 interface class는 자유도가 높습니다.



### Interface class

#### 1. 기존 클래스에 쉽게 새로운 인터페이스를 구현해 넣을 수 있습니다.

단순히 implements 다음에 구현할 인터페이스를 서술하고, 해당 메서드를 구현하는 것으로 끝이죠.



#### 2. mixin class를 만들 때 유용합니다.

##### mixin 정의 

mixin is a type that a class can implement in addition to its "primary type" to declare that it provides some optional behavior.

즉, 주요 타입 이외에도 클래스가 구현할 수 있는 타입을 의미합니다.

예를 들어 Comparable이 mixin interface라 보시면 됩니다. 주요 기능 외에 비교가능한 타입을 추가하는 형태니까요.



### 3. nonhierarcy type framework를 만들 때 유용합니다.

Type의 계층은 조직을 구성할 때 매우 유용하지만 그렇지 않은 경우가 있습니다. 이때 interface를 쓰면 적절하죠.



interface의 이점은 이와 같습니다. 그리고 interface의 default method를 확용하는 방법을 설명드리겠습니다.



# default method

### 이점

Interface는 wrapper class 관점에서 안전하고 파워풀한 기능을 향상시킬 수 있습니다. default method 형태로 programmer에게 구현을 도와줄 수 있습니다.



### 제한 사항

1. Object class 인스턴스의 method들을 default method로 제공할 수 없습니다.
2. instance field나 non public static members를 제공할 수 없습니다.
3. interface를 생성하기 전에는 default method를 만들 수 없습니다.



하지만! 다음 기법을 사용하면 interface의 이점과 abstract의 이점 둘 다 챙길 수 있게 되지요.

# skeletal implementation class

interface와 함께 abstract skeletal implementation class를 제공해주면 됩니다!

interface로 type을 정해주고,

default method로 몇가지 기능을 제공해주며,

skeletal implementation class로 primitive interface method 위에 나머지 non-primitive interface method를 구현합니다.



그래서 interface를 구현한 것만으로 대부분 작업을 마칠 수 있습니다. (Template Method Pattern)



### Naming Convention

Abstraction*Interface* 라 불리며, *Interface*엔 구현하려는 interface이름을 정해주면 됩니다.

ex:)Collection framework의 AbstractionCollection, AbstractionSet, AbstractionList, AbstractionMap



추상의 의미보다는 뼈대를 의미하기 때문에 SkeletalCollection, SkeletalSet등으로 불리는 것이 의미상 맞긴한데, 이미 Abstraction으로 굳어버렸습니다. (Template)



### 예시 - intArrayAsList

method에서 List구현체를 반환시켜주어야 할 경우, 이 예시는 매우 유용할 수 있습니다.

```java
// Concrete implementation built atop skeletal implementation (Page 101)
public class IntArrays {
    static List<Integer> intArrayAsList(int[] a) {
        Objects.requireNonNull(a);

        // The diamond operator is only legal here in Java 9 and later
        // If you're using an earlier release, specify <Integer>
        return new AbstractList<>() {
            @Override public Integer get(int i) {
                return a[i];  // Autoboxing (Item 6)
            }

            @Override public Integer set(int i, Integer val) {
                int oldVal = a[i];
                a[i] = val;     // Auto-unboxing
                return oldVal;  // Autoboxing
            }

            @Override public int size() {
                return a.length;
            }
        };
    }

    public static void main(String[] args) {
        int[] a = new int[10];
        for (int i = 0; i < a.length; i++)
            a[i] = i;

        List<Integer> list = intArrayAsList(a);
        Collections.shuffle(list);
        System.out.println(list);
    }
}
```

주목할 사항은 다음과 같습니다.

1. Integet instance를 array로 반환시켜주는 Adapter
2. anonymous class 형태로 구현하였습니다.



결국, interface의 이점, abstract의 이점 둘 다 챙길 수 있는 형태라고 보시면 됩니다. 



그리고 default method로 skeletal implementation class를 제공하지 못하더라도 여전히 skeletal class는 이점이 있습니다!



### simulated multiple inheritance

private inner class로 skeletal implementation class를 작성합니다. 그리고 top class의 instance로 method를 호출하면 inner class의 instance에게 위임하는 식으로 사용할 수 있습니다. 이러한 방식을 simulated multiple inheritance라고 부릅니다.



### skeletal implementation class 작성법

#### 용어 정리

primitive class - 기반 클래스

=> top class로 기본이 되는 클래스라 보면 됩니다.



1. 다른 메서드들의 구현에 사용되는 기반 메서드 선정

   이 기반 메서드들이 골격 구현에서는 추상 메서드가 될 것.

2. 기반 메서드를 사용해 직접 구현할 수 있는 메서드들을 모두 default method로 제공

   equals, hashCode등은 제외

3-1. 만약 이 인터페이스의 메서드가 모두 기반 메서드와 디폴트 메서드가 된다면 골격 구현 클래스를 만들 필요가 없다.

3-2. 만약 기반 메서드나 디폴트 메서드로 만들지 못한 메서드가 남아있다면 이 인터페이스를 구현하는 골격 구현 클래스를 하나 만들고 남은 메서드들을 작성해 넣는다.

​	이떄 골격 구현 클래스에는 public이 아닌 필드나 method를 추가해도 된다.



### 예시 - Map.Entry interface

```java
// Skeletal implementation class (Pages 102-3)
public abstract class AbstractMapEntry<K,V>
        implements Map.Entry<K,V> {
    // Entries in a modifiable map must override this method
    @Override public V setValue(V value) {
        throw new UnsupportedOperationException();
    }
    
    // Implements the general contract of Map.Entry.equals
    @Override public boolean equals(Object o) {
        if (o == this)
            return true;
        if (!(o instanceof Map.Entry))
            return false;
        Map.Entry<?,?> e = (Map.Entry) o;
        return Objects.equals(e.getKey(),   getKey())
                && Objects.equals(e.getValue(), getValue());
    }

    // Implements the general contract of Map.Entry.hashCode
    @Override public int hashCode() {
        return Objects.hashCode(getKey())
                ^ Objects.hashCode(getValue());
    }

    @Override public String toString() {
        return getKey() + "=" + getValue();
    }
}
```

Map.Entry 인터페이스나 이 인터페이스의 하위 인터페이스로는 이 skeletal implemenation class를 제공할 수 없습니다. equals, hashCode, toString같은 Object의 메서드를 오버라이딩 할 수 없기 때문이죠.



### 문서화

*  skeletal implementation은 상속을 가정하므로 상속의 규약을 따라야 합니다.
* 동작 방식을 잘 정리하여 문서로 남겨두어야 합니다.



### simple implementation

* skeletal implementation의 작은 변종입니다.

* 상속을 위해 인터페이스를 구현했으나, **추상 클래스가 아닙니다.**

  즉, 동작하는 가장 단순한 클래스

* 그대로 써도 되고, 필요에 맞게 확장해도 됩니다.



#### 예시 - SimpleEntry

AbstractMap의 static class로 정의되어 있습니다. 보시다시피 abstract class도 아니고, interface도 아닌 일반 class입니다.

### ![스크린샷 2020-12-10 오후 7.59.12](/Users/ju/Desktop/스크린샷 2020-12-10 오후 7.59.12.png)