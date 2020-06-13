# Object prototypes

#### 정의

프로토타입은 JavaScript의 object가 다른 object에게 properties를 물려받는 메카니즘을 말한다.

#### 학습 목표

* prototype chains가 어떻게 작동하는지 알기
* prototype property가 이미 존재하는 constructor에 메소드를 추가하기 위해 어떻게 사용되는지 



## A prototype-based language?

Javascript는 prototype-based lanugage라고 부름. 그 이유는 prototype은 상속이라는 기능을 제공하기 위한 것.

objects들은 prototype 이라는 object를 가지고 있음. 이것은 template object(다른 object로부터 method와 properties를 상속받는)처럼 행동함.

#### prototype chain

objects의 prototype object는 또한 prototype object를 가지고 있음.이 오브젝트 또한 다른 오브젝트로부터 상속받음.  이러한 연쇄를 프로토타입 체인이라 부름.

!!**정확히 object의 속성은 object 객체 그 자체가 아닌, 해당 object의 생성자 함수가 지닌 prototype property에 해당 properties와 methods가 정의된다.**!!

```
Well, to be exact, the properties and methods are defined on the `prototype` property on the Objects' constructor functions, not the object instances themselves.
```



여기서 생성자 함수는 위에서 언급한 constructor function (function Car() {this.p = ~~~})



javascript에서는 object instance와  그것의 prototype(\__proto__) property사이에 연결관계가 형성됨.



**Note!**

object's의 prototype과 constructor function의 prototype property는 다르다.

전자는 instance의 property이며 후자는 constructor의 property를 의미.



## Understanding prototype objects

![](https://mdn.mozillademos.org/files/13853/object-available-members.png)

```js
let person1 = new Person('Bob', 'Smith', 32, 'male', ['music', 'skiing']);
```

위와 같이 생성했을 때 나오는 property들.

1. person1's constructor에서 정의된 members.(name,age, ...., greeting)

2. Person()'s constructor's의 prototype object(Object 객체)에 정의된 members. (toString, valueOf ...)

**어떻게 person1이 valueOf method를 가지고 있을까?**

1. person1의 constructor인 Person()에 valueOf가 정의되었는지 확인. (즉, 위에서 언급한 Person()과 person1의 관계처럼, person1의 생성자인 Person에 있는지 확인함)
2. 없다면 Person() constructor의 prototype object인 Object에 valueOf()가 있는지 확인. 있다면 잘 작동!

아래는 매우 중요한 말.

```
Note: We want to reiterate that the methods and properties are not copied from one object to another in the prototype chain. They are accessed by walking up the chain as described above.
```

> 다시 말해, 포인터가 없는 언어에서 tree를 만들 때 사용하는 방법이라고 보시면 됩니다. 파이썬과 같은 언어에서는 self.root 에 Node()라는 객체를 만들고, 해당 node의 왼쪽 오른쪽 변수에 또 Node()를 담도록 합니다. 그렇게 계속 객체를 찾아갈 수 있도록 할 수 있습니다.  자바스크립트도 이와 유사하게 상속을 구현한 것이죠.
>
> 생성자 함수를 통해 객체를 만듭니다. 그리고 그 객체는 constructor와 연결되있습니다. 그래서 constructor prototype이라는 property(변수, 객체)를 가지는데 여기에 자신의 상위 Object에 대한 데이터가 담겨 있습니다. 따라서 해당 Object를 찾아가는 것이지요.
>
> 따라서 prototype을 단지 상위 객체를 담는 변수라봐도 무방할 것 같습니다. 그러면 왜 prototype(원형)이라고 정의했는지도 이해가 됩니다. (트리에서 상위 노드는 부모노드를 의미하며 이를 끝까지 따라가면 root노드가 나옵니다. root는 근원이라는 의미를 가지기도 하니까요!)



## The prototype property: Where inherited members are defined

#### 의문점

상속받은 properties 와 method는 어디에 정의될까? docs에서 Object를 보면 properties, methods가 많은데 모두 상속받는 것은 아니다. 왜그럴까?



결론부터 말하자면 Object.prototype. 과 object. 의 차이이다.



prototype의 value는 object이다. 즉. 해당 object의 properties와 methods를 저장하는 bucket이라 보면 됨. 따라서 prototype chain을 통해 해당 bucket에 담긴 내용을 이용할 수 있게 되는 것이다. 그런데 prototype에 정의하지 않았으므로 해당 값을 이용할 수 없는 것임.

즉, Object.is() , Object.keys() 같은 것은 prototype이라는 bucket에 담지 않았으므로 이 메서드는 상속받은 객체가 사용할 수 없는 것. 단지 Object() constructor 자체가 사용할 수 있는 methods/properties들임.



## Revisiting create()

var obj2 = Object.create(obj1)에서 작동방식은 obj1의 prototype을 사용해서 obj2 prototype을 정해줌. 따라서 obj1과 obj2는 동일하다!



## The constructor property

Constructor Function의 prototype속성에 contructor 존재 이 constructor은 constructor function의 origin을 의미한다.

prototype에 정의되어 있으므로 instance 또한 constructor이용할 수 있게 된다.

따라서 person1.constructor 사용 가능 이는 Person() constructor 반환 함.

이 생성자로 다른 객체를 생성하기 위해 이용. 생성자 함수 또한 결국 함수이기에 괄호를 통해 이용할 수 있음. 

따라서 function을 생성자로 만들어주기 위해 new키워드를 붙이면 객체 생성가능!

```js
let person3 = new person1.constructor('Karen', 'Stephenson', 26, 'female', ['playing drums', 'mountain climbing']);
```

위 방법은 객체를 생성하고 싶으나, 모종의 이유로 constructor function이 존재하지 않을 때 이용하면 유용함.

```js
person1.constructor.name
```

또는 생성자 함수의 이름을 알기 위해 사용 가능



## Modifying prototypes

#### 수행할 내용

Person()으로 찍어낸 객체들은 모두 Person()의 prototype을 참조하므로 해당 프로토타입 수정.



절차

1. Person으로 person1 객체 생성
2. Person.prototype.farewell = function() {}; 입력
3. person1객체에서 farewell 실행



person1에서 잘 작동하게 된다. person1이 Person과 연결되어 있고 Person의 prototype 중 farewell을 실행하게 되므로.



하지만 여기에 변수를 선언하는 것은 어려움. scope가 window가 되기 때문

```js
Person.prototype.fareWell = this.name + "good bye";
```

이처럼 하면 여기서 this는 window가 된다. 따라서 이렇게 사용하면 안됨. constant를 넣더라도 clean code 관점에서는 객체 선언시 넣을 것.

즉, **clean code 관점**.

1. properties는 constructor function에 넣어준다.
2. method는 생성자 함수를 정의 한 후에 생성자 함수의 prototype에 넣어준다.

