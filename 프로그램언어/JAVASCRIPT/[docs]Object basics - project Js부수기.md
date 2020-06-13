# Javascript 파괴하기 프로젝트 (Object)

출처 : https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/



앞으로 정리라고 붙인 내용은 참고한 내용을 알리는 느낌이 아닌 단순 정리를 합니다. 요약 정리 어투로 적을 것이며 이해 안되는 문장이 있을 수 있습니다.  손으로 써가는 느낌으로 알기 위해 적은 것이기 때문이며, 출처에 매우 잘 설명되어 있기에 제가 따로 설명할 필요가 없기 때문입니다.

# Object basics

#### object의 정의

object는 관련된 데이터와 기능의 묶음이다.(oop에선 이것을 속성과 method라고 부름)



#### 객체 초기화

literal 적용

#### 객체 접근

object.propertyName

data 면 property, function이면 method라 부른다.



## Dot Notation

위 객체 접근을 보면 dot notation을 통해 접근.

마치 namespace처럼 작동함.

즉, object에 encapsulated되었다고 표현.



#### Sub-namespaces

name 을 ['Bob','Smith']로 선언 하는 것이 아닌,

```js
name : {
  first: 'Bob',
  last: 'Smith'
},
```

로 선언.

이것을 Sub-namespaces라고 한다. person이라는 namespaces에 name이라는 부수적인 namespaces를 정의.

> (namespaces라는 개념은 마치 하나의 집단을 표현하는 말인 것 같습니다. 
>
> 학교가 있으면 학교 구성을 일일이 철수, 영희, 길동, 급식실, 교실....이라고 부르는 것이 아닌, 학교라는 namespace로 해당 집단의 원소들을 묶어냅니다. 그리고 철수,영희,길동은 같은 성질을 가지는 학교의 원소로써 사람이라는 sub-namespaces로 분류합니다. 급식실,교실 등은 건물이라는 sub-namespaces로 둘 수 있겠죠.)
>
> 한편으로 이러한 접근은 사람은 구체적인 현상보다는 개념적 사고를 하기 때문에 가독성이 좋아지는 방식이 아닐까 싶습니다.



## Bracket notation

object의 properties에 접근하는 또 다른 방식.

array에 접근하는 방식과 유사.

이렇게 접근하는 관점은 위의 namespace와 다르게 관련 있는 array에 접근한다는 관점이다.(즉, python의 dict)

####  **bracket notation의 장점**

object의 name을 동적으로 만들 수 있음.

즉,

```js
let dataName = 'height';
let dataValue = '1.75m';
person[dataName] =  dataValue;
```



## What is "this"?

this는 이 this가 쓰여있는 코드를 가지고 있는 object를 의미함.

this라고 두어야 this가 유연하게 사용될 수 있음. 저객체 이객체에서 name이 달라질 수 있으므로.





## Object 생성

#### constructor를 이용하지 않고 일반 function 이용

```js
function createNewPerson(name) {
  const obj = {};
  obj.name = name;
  obj.greeting = function() {
    alert('Hi! I\'m ' + obj.name + '.');
  };
  return obj;
}
```

>new라는 키워드가 어떻게 작동하는지 매번 궁금했습니다. 여기서 명료해지네요. 그리고 Object를 function Person(){ this.name = name} 이런식으로 정의하여 생성해낼 때 왜 this를 사용하는지도 이해가 됩니다. 객체를 생성할 때 해당 객체의 name으로 넣어주어야 하기 때문이죠. 더 읽다보니 아래처럼 잘 나와있네요.
>
>```
> it basically just defines properties and methods. Notice also the this keyword being used here as well — it is basically saying that whenever one of these object instances is created, the object's name property will be equal to the name value passed to the constructor call, and the greeting() method will use the name value passed to the constructor call too.
>```

#### constructor function

```js
function Person(name) {
  this.name = name;
  this.greeting = function() {
    alert('Hi! I\'m ' + this.name + '.');
  };
}
```



#### prototype에 대한 언급

```
let p1 = new Person("Bob");
let p2 = new Person("Sarah");
```

처럼 정의하면 greeting이라는 메소드는 동일함에도 매번 객체를 생성하게 된다. 즉, 메모리 낭비가 발생

따라서 추후에 배울 prototype이라는 것을 통해 효율적으로 객체를 관리할 수 있게 된다.