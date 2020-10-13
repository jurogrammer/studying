

# 참고 자료

* https://refactoring.guru/design-patterns/observer

* https://ko.wikipedia.org/wiki/%EC%98%B5%EC%84%9C%EB%B2%84_%ED%8C%A8%ED%84%B4



# Intent

### 분류

* behavioral design pattern
  * 그룹 내 object간 어떻게 소통할 지에 대해 관한 패턴

### 정의

* (guru) 여러 객체들이 관찰하고 있는 객체에 발생하는 이벤트를 알리기 위해 subscription 메커니즘을 정의하도록 하는 패턴
* (wiki) 객체의 상태 변화를 관찰하는 관찰자들, 즉 옵저버들의 목록을 객체에 등록하여 상태 변화가 있을 때마다 메서드 등을 통해 객체가 직접 목록의 각 옵저버에게 통지하도록 하는 디자인 패턴이다





<img src="https://refactoring.guru/images/patterns/content/observer/observer-2x.png" style="zoom:50%;" />



# Problem

### 상황 - 이벤트 알기

* `Customer`,`Store` 두 타입의 Object가 존재합니다.
* Customer는 Store에서 곧 판매될 iPhone 최신형 모델에 관심있습니다.



###  문제

* 어떻게 해야  매장에 최신형 아이폰이 나오자마자 고객이 물건을 살 수 있을까요?



![](https://refactoring.guru/images/patterns/content/observer/observer-comic-1-en.png)

### 

### 안 좋은 방법

#### [방법 1] 고객이 매일 방문

* 최신형 아이폰이 매장에 출시되었는지 알기 위해 고객이 매일매일 매장을 방문합니다.



##### 단점

1. 고객은 출시 되지 않았음에도 매장에 찾아갈 수 있으므로 쓸데없는 동선이 생깁니다. 다시말해서 Customer가 고생한다는거죠



#### [방법 2] Store가 모든 고객에게 알려주기

* 새로운 제품이 출시될 때마다 모든 고객에게 emails을 보내는 것입니다.
* 이 방법은 [방법 1]처럼 고객이 동선을 낭비하는 일이 없어집니다.



##### 단점

1. 새로운 제품에 관심이 없더라도 고객은 알림을 받아야 하므로 화나게 됩니다.
2. 매장의 자원이 낭비됩니다.



프로그래밍 관점에서 문제는 다음 2가지로 요약됩니다.

1. 고객이 새로운 제품이 출시되었는지 확인하느라 자원을 낭비하는 일이 없어야하며, 

2. 매장이 관심없는 고객에게 보내느라 자원을 낭비하는 일이 없어야 합니다.



어떻게 하면 이 상충되어보이는 문제를 해결할 수 있을까요?



# 해결책

### 방법

* 매장에서 새로운 아이폰 출시에 관심있는 고객에게만 emails를 보내주면 됩니다!



이 방법을 설명하기 위해 다음 용어를 소개시켜드리겠습니다.



### 용어

#### 1. publisher

흥미있는 상태를 가지는 객체로 *subject라고* 부르나, observer pattern에선 이 객체가 다른 objects들에게 자신의 상태를 알리므로 publisher라고 부릅니다.

#### 2. subscribers

publisher's 상태 변화를 추적(track,observe)하고 싶은 객체를 subscribers라고 부릅니다.



### Observer Pattern 적용

1. subscriber가 publisher로부터 발생하는 이벤트를 구독하고, 구독취소할 수 있도록 publisher class에 subscription mechanism을 추가하도록 합니다. (ex: addSubscriber, remoeSUbsciber....)

![](https://refactoring.guru/images/patterns/diagrams/observer/solution1-en.png)



2. publisher에서 중요한 이벤트 발생을 전달할 수 있도록 subscribers의 특별한 notification method를 부르도록 합니다.



3. 다음으로, publisher가 concrete한 subscriber에게 커플링되지 않도록 subscriber가 동일한 Interface를 구현하도록 합니다.
   * 이 인터페이스엔 어떤 이벤트가 발생했는지 알려주기 위해 context data를 넘겨줘야 합니다. 그래서 이 context data를 넘겨줄 수 있는 notification method를 선언합니다.



![](https://refactoring.guru/images/patterns/diagrams/observer/solution2-en.png)

4. 추가적으로 여러 publisher에게 subscriber를 등록하고 싶다면, detail publisher에 의존하지 않도록 publisher를 interface로 선언하도록 합니다.



### [고객 - 매장] 문제에 적용

* IPhone 출시에 관심있는 고객만 매장에서 등록합니다.

* 그리고 IPhone이 매장에서 출시되었을 때, 매장에서 구독한 고객에게 알려주는 형태가 됩니다.

  

# 구조

![](https://refactoring.guru/images/patterns/diagrams/observer/structure.png)

### 1. Publisher

다른 object에게 관심있는 event를 발행(issue)합니다.

이 이벤트는 다음 두 상황에서 발생합니다.

*  publisher의 상태가 변경되거나
*  특정 behaviors가 실행될 때  



publisher는 subscription에 대한 infrastructure를 가지고 있습니다. (정의된 Mechanism)

1. subscriber를 저장하는 container
2. subscriber를 추가하는 메서드
3. subscriber를 삭제하는 메서드



이벤트가 발생하면 Subscriber들을 일일이 확인하며(goes over) subscriber에 있는 notification method를 실행합니다.



### 2. Subscriber (interface)

* notification interface를 선언합니다.
* 보통 single update method를 지닙니다.
* 이 method는 contextural parameters를 받습니다. 이를 통해 publisher가 event detail을 넘겨줍니다.



### 3. Concrete Subscriber

* publisher에 의해 실행된 notification에 반응하여 특정 액션을 수행합니다.

  

### 4. Client

* publisher와 subscriber를 각각 생성하고 publisher에 subscriber를 등록합니다.





# 예제

### 구조

![](https://refactoring.guru/images/patterns/diagrams/observer/example.png)

이 예제는 publisher의 subscription Inftrastructure를 EventManager로 분리하였습니다. 따라서 훨씬 좋은 구조라 보기에 직접 예제를 작성하지 않고 소개시켜드립니다. 

### 1. Publisher -Basic publisher

```java
package refactoring_guru.observer.example.publisher;

import refactoring_guru.observer.example.listeners.EventListener;

import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class EventManager {
    Map<String, List<EventListener>> listeners = new HashMap<>();

    public EventManager(String... operations) {
        for (String operation : operations) {
            this.listeners.put(operation, new ArrayList<>());
        }
    }

    public void subscribe(String eventType, EventListener listener) {
        List<EventListener> users = listeners.get(eventType);
        users.add(listener);
    }

    public void unsubscribe(String eventType, EventListener listener) {
        List<EventListener> users = listeners.get(eventType);
        users.remove(listener);
    }

    public void notify(String eventType, File file) {
        List<EventListener> users = listeners.get(eventType);
        for (EventListener listener : users) {
            listener.update(eventType, file);
        }
    }
}
```



### 2. Editor - Concrete publisher, tracked by other objects

```java
package refactoring_guru.observer.example.editor;

import refactoring_guru.observer.example.publisher.EventManager;

import java.io.File;

public class Editor {
    public EventManager events;
    private File file;

    public Editor() {
        this.events = new EventManager("open", "save");
    }

    public void openFile(String filePath) {
        this.file = new File(filePath);
        events.notify("open", file);
    }

    public void saveFile() throws Exception {
        if (this.file != null) {
            events.notify("save", file);
        } else {
            throw new Exception("Please open a file first.");
        }
    }
}
```



### 3. Listeners

```java
package refactoring_guru.observer.example.listeners;

import java.io.File;

public interface EventListener {
    void update(String eventType, File file);
}
```



### 4. EmailNotificationListener

```java
package refactoring_guru.observer.example.listeners;

import java.io.File;

public class EmailNotificationListener implements EventListener {
    private String email;

    public EmailNotificationListener(String email) {
        this.email = email;
    }

    @Override
    public void update(String eventType, File file) {
        System.out.println("Email to " + email + ": Someone has performed " + eventType + " operation with the following file: " + file.getName());
    }
}
```



### 5. LogOpenListener

```java
package refactoring_guru.observer.example.listeners;

import java.io.File;

public class LogOpenListener implements EventListener {
    private File log;

    public LogOpenListener(String fileName) {
        this.log = new File(fileName);
    }

    @Override
    public void update(String eventType, File file) {
        System.out.println("Save to log " + log + ": Someone has performed " + eventType + " operation with the following file: " + file.getName());
    }
}
```



### 6. Demo

```java
package refactoring_guru.observer.example;

import refactoring_guru.observer.example.editor.Editor;
import refactoring_guru.observer.example.listeners.EmailNotificationListener;
import refactoring_guru.observer.example.listeners.LogOpenListener;

public class Demo {
    public static void main(String[] args) {
        Editor editor = new Editor();
        editor.events.subscribe("open", new LogOpenListener("/path/to/log/file.txt"));
        editor.events.subscribe("save", new EmailNotificationListener("admin@example.com"));

        try {
            editor.openFile("test.txt");
            editor.saveFile();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

