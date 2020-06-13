# [문서 읽기]Object initializer

출처 : 

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer

### Object 초기화 방법

1. new Object()
2. Object.create()
   * 
3. literal notation
   * 장점 : 빠르게 초기화 가능



### ObjectLiteral과 JSON 차이

형태는 비슷하나, JSON의 value는 function이 올 수 없다.



### Computed property names

```js
let i = 0
let a = {
  ['foo' + ++i]: i,
  ['foo' + ++i]: i,
  ['foo' + ++i]: i
}
```

property name을 계산하여 초기화할 수 있도록 해줌

[]를 통해 계산할 property name을 정하고 ++i해주기.



### Prototype mutation

```js
__proto__:value
```

```javascript
"__proto__":value
```

만약에 value가 **object**이거나 **null**이라면 초기화된 object의 prototype을 해당 value로 바꿔 줌.





\__proto\_\_ 라는 property를 생성하는 건 아님.





