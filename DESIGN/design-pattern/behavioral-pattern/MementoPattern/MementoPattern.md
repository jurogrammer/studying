# 참고

* https://refactoring.guru/design-patterns/memento



memento: (사람 장소를 기억하기 위한) 기념품

# 정의

* behavioral deisign pattern

  object의 behavior을 캡슐화하고 요청을 object에 위임하는 패턴

  

* 세부 구현을 캡슐화하면서 이전 상태의 object를 저장하거나 복구하는 디자인 패턴

* Snapshot Pattern이라고도 불림



# 상황 - editor program 되돌리기 기능 구현

* editor 프로그램이 있다고 생각합시다
* 이 프로그램은 텍스트 편집 뿐만 아니라 텍스트를 꾸미고, 이미지를 삽입할 수도 있습니다.



<img src="https://refactoring.guru/images/patterns/diagrams/memento/problem1-en-2x.png" style="zoom:67%;" />

### 문제

* 어떻게 해야 되돌리기 기능을 구현할 수 있을까요?



### 되돌리기 기능을 구현하기 위해서...

1. operation을 수행 전 모든 objects의 상태를 저장하고 저장소에 넣습니다.
2. 후에 user가 revert를 결정하면 저장소에서 objects의 상태를 꺼냅니다.
3. 그 상태를 바탕으로 app의 현재 상태를 셋팅해줍니다.



이때, object의 상태를 읽을 때 어떻게 하는게 좋을까요?

### 안 좋은 접근 방법



#### 방법1 다른 object로 editor 상태값 접근하기

문제 : 값에 접근 못할 수 있습니다. 보통 class들은 자신의 상태 값을 private로 선언합니다.



#### 방법2 public으로 선언하기

문제: 추후 해당 클래스의 필드를 변경시 필드에 의존하는 클래스들이 에러날 수 있습니다.



#### 방법3 value타입의 컨테이너들의 리스트에 저장하기 

아무리 해당 field를 private로 막을 수 있다 하더라도 컨테이너가 public이냐에 따라서 결국 접근을 허용할 수 밖에 없습니다. 





어떻게하면 다른 객체에게 상태값을 캡슐화하면서 복사할 수 있을까요?

# Solution

### 복사되어질(originator) object가 상태값을 복사하라!

memento 패턴의 핵심 두가지입니다.

1. 프로토타입 패턴과 유사하게 데이터를 저장하는 주체가 복사대상이 하도록 합니다.

   그렇다면 private로 설정하더라도 값을 복사할 수 있죠.

2. 복사될 값을 memento라는 object에 담도록 합니다.

   저장하기 위해 자신의 객체를 생성하는 것이 아닌, originator의 값을 memento라는 object에 저장합니다. 이 또한 private로 선언되어 값에 접근 할 수 없도록 막습니다.



여기서 originator와 caretaker라는 용어를 사용할것입니다. originator는 복사될 대상을 의미하며, caretaker는 복사된 스냅샷을 사용하는 객체가 됩니다.



### 방법

##### 1. originator의 값을 저장할 memento 선언하기

originator object의 class 안에 memento라는 클래스를 선언합니다. 이렇게 함으로써 originator의 상태를 private로 선언하더라도 memento 내에 상태 값을 저장할 수 있게 되는 것이죠



##### 2. 타 object가 memento에도 접근하지 못하도록 memento 내 값을 private로 선언하기

originator와 더불어 스냅샷인 memento또한 다른 객체의 접근을 막아야 하기 때문입니다.



##### 3. 스냅샷이 필요할 경우 originator에서 값을 저장하여 memento를 출력해주기

caretaker가 스냅샷이 필요할 때 originator에게 부탁하여 받아오는 것이죠.



##### 4. 복구할 때는 스냅샷을 originator에게 건내주기

메멘토를 originator만 읽을 수 있도록 하였으니 결국 originator에게 이 스냅샷을 건내주면서 이대로 복구해줘 !라고 건내주는 형태가 됩니다.



##### 5. 메타데이터 저장

추가적으로 메멘토마다 이름 및 스냅샷 시간을 기록하기 위한 필드를 선언해주며, 다른 object는 이 정보를 바탕으로 스냅샷을 특정하게 됩니다. 따라서 메멘토의 인터페이스엔 getName, getSnapshotDate같은 메타데이터를 볼수 있는 메서드가 추가됩니다.





<img src="https://refactoring.guru/images/patterns/diagrams/memento/solution-en-2x.png" style="zoom: 50%;" />





# 구조

3가지 구조로 구현할 수 있는데 결국 핵심은 1가지 입니다. 어떻게 데이터를 캡슐화할 것인지를 보시면 됩니다.

### 1. Implementation based on nested classes

<img src="https://refactoring.guru/images/patterns/diagrams/memento/structure1-2x.png" style="zoom: 50%;" />

이 구조는 메멘토 클래스가 originator의 nested class가 됩니다. originator는 private 필드로 선언된 메멘토에 접근할 수 있는 반면, caretaker는 접근할 수 없게 됩니다.

#### 1. Originator

* 자신의 상태에 대한 snapshot을 남길 수 있고, 스냅샷의 정보를 이용해 복구까지 가능합니다.

#### 2. Memento

* originator 상태의 스냅샷에 대한 Value object
* 일반적으로 constructor를 통해 생성하고 immutable하게 해줍니다.

#### 3. Caretaker

* originator's state snapshot에 대한 정보를 알고 있습니다.(언제, 왜 캡쳐되었고, 언제 복구할 지도 알고 있습니다.)
* 보통 stack에 mementos를 저장함으로써 originator의 history를 추적할 수 있습니다.
* 복구해야한다면 stack에서 메멘토를 꺼내 originator에게 복구하도록 건내줍니다.





### 2. Implementation based on intermediate interface

<img src="https://refactoring.guru/images/patterns/diagrams/memento/structure2-2x.png" style="zoom:50%;" />

nested interface가 없는 경우에 이와 같은 구조를 적용합니다. (Ex PHP)

Caretaker에게는 Memento interface에 한정된 메서드를 제공하며, 

Originator는 ConcreteMemento를 이용하여 상태 정보를 얻을 수 있는 getState()메서드를 이용하도록 합니다.



### 3. Implementation with even stricter encapsulation

<img src="https://refactoring.guru/images/patterns/diagrams/memento/structure3-2x.png" style="zoom:50%;" />

memento를 통해 Originator의 상태를 변경할 수 있는 일말의 가능성도 차단하기 위해 이와 같은 구조로 구성합니다.



1. 이와 같은 구조는 다양한 타입의 originator와 memento를 허용하나, 각 originator와 상응하는 메멘토끼리만 작동(work)합니다.
2. Caretaker는 Memento Interface를 통해 작업하므로 state를 변화시키는데 제한이 생깁니다. 게다가 restore가 Memento에게 넘어갔으므로caretaker는 Originator와 독립적이게 됩니다.