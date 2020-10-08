# 참고자료

* https://refactoring.guru/design-patterns/mediator



# 정의

* behavioral design pattern
  * 그룹 내 object간 어떻게 소통할 지에 대해 관한 패턴

* 객체간 직접적으로 소통(communication)하는 것을 제한하고 mediator란 객체로 소통(collaboration)하도록 강제하는 디자인 패턴

<img src="https://refactoring.guru/images/patterns/content/mediator/mediator-2x.png" style="zoom:50%;" />



# 상황 - Dialog 내 Component간 소통

* 고객의 profile을 생성하고 편집하는 dialog를 생각해봅시다

* 이 dialog엔 다양한 form controll이 존재합니다.

  ex:) text fields, checkboxes, buttons



<img src="https://refactoring.guru/images/patterns/diagrams/mediator/problem1-en-2x.png" style="zoom: 50%;" />

### 핵심 포인트

form내 component간 어떻게 소통해야 좋을까요? 

* component간 상호작용 예시
  1. [submit 버튼]을 누르면 [text field]를 검사하여 유효성을 검사할 수 있습니다
  2. i have a dog라는 글씨가 있는 [check box] 클릭시 강아지 이름을 입력하도록 숨겨져있던 [text field]가 드러날 수 있습니다.





# 안 좋은 접근 - form controll간 직접 소통

<img src="https://refactoring.guru/images/patterns/diagrams/mediator/problem2-2x.png" style="zoom:67%;" />

예를 들어 [checkbox 버튼]에서 직접적으로 [text field]를 조작한다고 봅시다. 이렇게 된다면 [checkbox 버튼]이 [text field]에 의존할 수 밖에 없습니다.

그러면 다음과 같은 문제가 발생하죠.



### 문제 - 재사용 불가

다른 dialog에서 체크 박스를 다른 form에서 재사용하고 싶지만 이미 dog에 대한 text field와 강하게 결합되어 있어 재사용하기 어려워지죠.



# 해결 방법 - mediator를 두어라!

communication간 직접 소통을 줄이기 위해 중재자를 둡니다. 그리고 이 중재자를 통해 모든 소통이 가능하도록 하는 것이죠. 이 예제에서는 이미 모든 Component를 알고 있는 Dialog가 Mediator가 될 수 있습니다.



### Component(button, checkbox...)

* [checkBox button]이 자기가 체크되었다고 Mediator에게 알려줍니다.(notify 메서드 이용)
* [text field]는 Mediator에 의해 동작합니다.

### Mediator(dialog)

* 어떤 component가 noti를 알렸는지 notify메서드를 통해 알아냅니다.  여기선 checkBox button가 클릭되었다는 notification을 받겠습니다.
* 그리고 dialog의 textField reference를 통해 text field를 띄울 것을 위임하거나 직접 수행합니다.



### 이점

1. object는 알려주기면 하면 된다!

   checkBox button은 이전엔 text field를 띄워야하는 작업까지 해주었지만 이번엔 단순히 Mediator에게 알려주기만 하면 됩니다.

2. 다양한 dialog에서 사용할 수 있다!

   추가적으로 dialog의 추상화된 interface를 선언함으로써 다양한 dialog에 사용할 수 있습니다.

3. 관계를 캡슐화할 수 있다!

   복잡한 object간 관계를 mediator를 통해 숨길 수 있습니다.



=> 이렇게 함으로써 component끼리는 의존하지 않고 dialog에만 의존하기 때문에 다양한 맥락에서 재사용하기 수월해질 수 있습니다.

<img src="https://refactoring.guru/images/patterns/diagrams/mediator/solution1-en-2x.png" style="zoom:67%;" />





# 구조



<img src="https://refactoring.guru/images/patterns/diagrams/mediator/structure-2x.png" style="zoom: 67%;" />



### 1. Component

* 자신의 business logic이 들어있습니다.
* Mediator에게 알리기 위해 Mediator interface field가 존재합니다.
  * 이로 인해 다양한 mediator에서 재사용할 수 있게 됩니다.



### 2. Mediator

* component간 소통할 method를 선언 합니다.
  * 이것은 단순히 단일 notification method를 선언하는 형태로 구현됩니다.
  * component들은 자신과, 그리고 문맥에 따른 argument를 메서드에 넘겨줄 것입니다
    * 예를 들어 자기자신이 클릭이 됬을 때 `m.notifiy(this, "click")`라 보낼 수 있죠.
  * 이렇게 함으로써 sender와 receiver component간 의존성이 사라지게 되죠



### 3. Concrete Mediator

* component간 관계를 캡슐화합니다.
* 보통 모든 component들에 대해 reference를 지니고 management합니다. 때때로 자기 자신의 life cycle까지 management합니다.



#### 주요 사항 정리

* component는 반드시 다른 component를 몰라야 합니다. 이벤트가 발생하면 단지 mediator에게 알려주기만 할 뿐이죠.
* mediator는 알림을 받으면 sender를 식별합니다. 이를 통해 쉽게 어떤 component가 trigger되야할 지 알 수 있죠.
* component관점에서 black box와 유사합니다. sender는 누가 요청을 받을 지 알 수 없으며 receiver는 누가 요청을 보냈는지 알 수 없기 때문이죠.

