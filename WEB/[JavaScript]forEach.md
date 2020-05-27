# forEach

### 목적

> 인덱스 에러 줄임(전체 배열을 반드시 돌으므로.)
>
> 간결



foreach : 각 값 참조해줌

map : return으로 배열을 반환해줌.

filter : return은 true false로. true인 값만 return 해줌.





# 객체

### 정의

javascript의 객체는 key,value형태로 취해진 것.



자바스크립트의 객체는 객체 리터럴이 그 자체이다.



```javascript
var healthObj = {
  name : "달리기",
  lastTime : "PM10:12",
  showHealth : function() {
    console.log(this.name + "님, 오늘은 " + this.lastTime + "에 운동을 하셨네요");
  }
}

healthObj.showHealth();
```

위에서 보이듯이 객체 리터럴이 객체 그 자체!

필드 값? -> name, lastTime.

메소드 ? -> showHealth.

OMG!



# this는 무엇을 가르킬까? 

* 함수의 실행 컨텍스트를 말한다.
  * 이 함수의 참조 지점을 의미함.
  * 위에선 healthObj에 의해 showHealth가 불렸기 때문에 여기서 this는 healthObj이다.
  * (bind, call, apply를 배우면 달라질 수 있긴 함)

- 자바스크립트의 객체는 singleTone.

### this가 바뀌는 경우.

```javascript
var others = {
    todos : "아무것도 하지 않는다."
}

var todo = {
    todos : ["자바스크립트 공부하기"],
    showTodo : function() {
        return this.todos;
    }
}
```



todo.showTodo.call(others);

실행결과 : 아무것도 하지 않는다.



이유. todo에서 showTodo를 호출한다. 하지만 실행 문맥을 others로 바꿈으로써(this가 others로) 함수가 참조하는 객체가 others로 바뀐다. 따라서 return this.todos => return others.todos;가 된다.



# bind

**핵심 키워드**

>this
>
>bind



```javascript
var healthObj = {
  name : "달리기",
  lastTime : "PM10:12",
  showHealth : function() {
    setTimeout(function() {
        console.log(this.name + "님, 오늘은 " + this.lastTime + "에 운동을 하셨네요");      
    }, 1000)
  }
}
healthObj.showHealth();
```

healthObj는 반환되고 window가 setTimeout을 실행하므로 this는 window가 된다.

이 때문에 함수바깥에 bind(this)를 하면 됨.

```javascript
var healthObj = {
  name : "달리기",
  lastTime : "PM10:12",
  showHealth : function() {
    setTimeout(function() {
        console.log(this.name + "님, 오늘은 " + this.lastTime + "에 운동을 하셨네요");      
    }.bind(this), 1000) //function 메소드로 bind! 
  }
}
healthObj.showHealth();
```

함수에 .을 찍으면 함수가 객체로 변하고 function native 객체에 있는 메소드를 부를 수 있다. (대표적으로 bind)

* bind는 함수를 반환하는 함수이다.(return 값 존재) 

* 따라서 다음과 같이 말할 수 있다.

  ```javascript
  function() {
          console.log(this.name + "님, 오늘은 " + this.lastTime + "에 운동을 하셨네요");      
      }.bind(this)
  => return 값으로 다시 함수 반환. function()
  해당 function은 this가 healthObj를 가리킴.
  ```

  ```javascript
  var newFunction = function(){}.bind(this);
  ```

  

**그런데 allow function에서는 this가 가르키는 것이 다를 수 있다.!**

