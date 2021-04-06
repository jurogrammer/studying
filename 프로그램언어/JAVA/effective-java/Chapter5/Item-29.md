# Favor generic types

generic types를 작성하는 것은 좀 어렵지만, 사용 방법을 배울 가치가 있습니다.

Item-7에서 봤던 class를 generic으로 바꾸는 예제를 고려해보겠습니다.



# 예제 - Stack

### Stack class code

```java
import java.util.Arrays;

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
        Object result = elements[--size];
        elements[size] = null;
        return result;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    private void ensureCapacity() {
        if (elements.length == size)
            elements = Arrays.copyOf(elements, 2 * size + 1);
    }
```

generic이 매우 시급한 class라 보시면 됩니다. client가 pop한 object를 사용하려면 반드시 캐스팅을 해주어야 하기 때문이지요. 이는 런타임 중에 에러를 일으킬 수 있습니다.

따라서 차근차근 generic화 시켜보겠습니다.



### 1. type parameters 선언 및 대체

첫번째 단계는 type parameters를 선언해주고, 해당 변수명으로 바꿔주면 됩니다. 여기선 Stack의 elements만 고려해주면 되겠죠? 

네이밍 컨벤션으로 type parameter E를 선언해줍니다. 그리고 elements의 타입인 Object를 E로 대체해주죠.

잘 따라오셨다면 아래의 코드와 같아지겠죠?

 ```java
public class Stack<E> {
    private E[] elements;
    private int size = 0;
    private static final int DEFAULT_INITIAL_CAPACITY = 16;

    public Stack() {
        elements = new E[DEFAULT_INITIAL_CAPACITY];
    }

    public void push(E e) {
        ensureCapacity();
        elements[size++] = e;
    }

    public E pop() {
        if (size == 0)
            throw new EmptyStackException();
        E result = elements[--size];
        elements[size] = null; // Eliminate obsolete reference return result;
    }
       ... // no changes in isEmpty or ensureCapacity
}
 ```



### 2. error 및 warning처리

위를 그대로 컴파일하려고 한다면, error와 warning이 발생합니다. error는 다음과 같죠

```
Stack.java:8: generic array creation
elements = new E[DEFAULT_INITIAL_CAPACITY];
					 ^
```

generic type(non-reifiable type)으로 배열을 생성할 수 없기 때문에 위와 같은 에러가 발생하죠.



따라서 이를 해결 하는 방법은 2가지로 나뉩니다.



#### 방법1 E[]로 캐스팅

Object 배열을 생성한 뒤에 E[]로 캐스팅하면 됩니다. 그런데, 제너릭은 런타임 중에 타입이 지워지니 또 warning이 뜨긴 하겠죠. 컴파일러가 보장할 수 없으니까요.

따라서 SuppressWarnings을 달아줘야 하는데 타입이 안전하다는 근거는 다음과 같이 말할 수 있습니다.

1. elements가 private로 선언되고 메서드를 통해서라도 client에게 값이 전달될 일이 없다.
2. elements는 오직 push method를 통해서 값이 들어가는데, 여기에 E말고는 다른 타입이 들어올 일은 없습니다.

이와 같이 명시하면 되겠죠?

그리고 위치는 가장 좁게 한정해줘야 하는데, 생성자가 elements에 대입하는 연산만 가지고 있으므로 가독성을 위해 construction위에 `SuppressWarnings("unchecked")`를 달아주면 됩니다.

```java
import java.util.Arrays;

// Generic stack using E[] (Pages 130-3)
public class Stack<E> {
    private E[] elements;
    private int size = 0;
    private static final int DEFAULT_INITIAL_CAPACITY = 16;

    // The elements array will contain only E instances from push(E).
    // This is sufficient to ensure type safety, but the runtime
    // type of the array won't be E[]; it will always be Object[]!
    @SuppressWarnings("unchecked")
    public Stack() {
        elements = (E[]) new Object[DEFAULT_INITIAL_CAPACITY];
    }

    public void push(E e) {
        ensureCapacity();
        elements[size++] = e;
    }

    public E pop() {
        if (size == 0)
            throw new EmptyStackException();
        E result = elements[--size];
        elements[size] = null; // Eliminate obsolete reference
        return result;
    }
}
```



### 방법2 Object[]를 그대로 선언하고, 문제되는 부분만 수정

Object[] 선언을 그대로 가져가고, 문제가 되는 pop method에서 casting해주는 방법입니다.

캐스팅없이 실행한다면 방법1과는 다른 에러가 발생하죠.

```
Stack.java:19: incompatible types
   found: Object, required: E
           E result = elements[--size];
           										^
```

E가 필요한데 Object가 꺼내졌다고 나오네요. 따라서 Object를 E로 캐스팅 해주면 됩니다.

그렇다면 다음과 같은 경고로 바뀌죠

```
Stack.java:19: warning: [unchecked] unchecked cast
   found: Object, required: E
E result = (E) elements[--size];
											 ^
```

E가 non-reifiable type이기 때문에 컴파일러가 런타임 중 캐스트를 검사할 방법이 없다고 말하는 것 입니다. 또 다시 다음과 같은 근거로 SuppressWarnings를 달아주면 됩니다.

1. E만 push하니깐 pop한 것도 E다. 따라서 E로 캐스팅하는 것은 옳다!



```java
import java.util.Arrays;
import effectivejava.chapter5.item29.EmptyStackException;

// Generic stack using Object[] (Pages 130-3)
public class Stack<E> {
    private Object[] elements;
    private int size = 0;
    private static final int DEFAULT_INITIAL_CAPACITY = 16;
    
    public Stack() {
        elements = new Object[DEFAULT_INITIAL_CAPACITY];
    }

    public void push(E e) {
        ensureCapacity();
        elements[size++] = e;
    }

    // Appropriate suppression of unchecked warning
    public E pop() {
        if (size == 0)
            throw new EmptyStackException();

        // push requires elements to be of type E, so cast is correct
        @SuppressWarnings("unchecked") E result =
                (E) elements[--size];

        elements[size] = null; // Eliminate obsolete reference
        return result;
    }
}

```



### 장단점

#### 방법1

##### 장점

1. 가독성이 좋습니다.
2. casting을 construct부분에 한번만 해주면 됩니다.

이와 같은 이유로 방법1이 주로 사용됩니다.

##### 단점

1. 힙오염이 발생할 수 있습니다.



#### 방법2

##### 장점

1. 힙오염을 예방할 수 있습니다.

##### 단점

1. casting을 여러 번 해야 합니다.





### Generic을 사용한 ClientCode

```java
    // Little program to exercise our generic Stack
    public static void main(String[] args) {
        Stack<String> stack = new Stack<>();
        for (String arg : args)
            stack.push(arg);
        while (!stack.isEmpty())
            System.out.println(stack.pop().toUpperCase());
    }
}
```

방법1이나 방법2를 통해 Generic을 적용함으로써 casting없이 stack내 pop한 element에 대해 String의 toUpperCase method를 사용할 수 있게 되었습니다!



# Array대신 List쓰라며?

Item 28과 이번 아이템 내용은 매우 대조적이죠. Item28에서 쓰라던 List대신 Array를 쓰는 이유는 다음과 같습니다.

1. List를 쓰는 경우가 아예 불가능한 경우

   List는 java가 기본적으로 제공해주지 않습니다. 따라서 ArrayList 내부엔 array를 쓸 수 밖에 없습니다.

2. 성능 개선 목적으로

   List보다 Array가 빠릅니다. 따라서 HashMap같은 경우엔 array를 사용하죠.



# Type parameter 범위

primitive type 제외하고는 Type에 제한이 없습니다.

```java
Stack<Object>, Stack<int[]>, Stack<List<String>>
```

과 같은 type들은 허용하나

```java
Stack<int>, Stack<long>	
```

과 같은 타입은 허용하지 않는다는 뜻이죠. 대신, primitive type은 boxing type을 통해 우회할 수 있습니다.



### 범위 제한 설정

type parameter 범위를 제한할 수도 있습니다.

```java
class DelayQueue<E extends Delayed> implements BlockingQueue<E>
```

E는 Delayed의 하위클래스만 받는다라고 선언한것이죠. 

따라서 Casting할 필요도 없고, ClassCastException없이 DelayQueue나 DelayQueue를 사용하는 client는 형변환 필요없이 DelayQueue의 elements에서 Delayed emthod를 사용할 수 있게 됩니다.

이때, E는 ***bounded parameter***라고 불립니다.

한편으로, 자기 자신도 서브타입이기 때문에 `DelayQueue<Delayed>`도 허용합니다!

