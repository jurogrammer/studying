# Object Model

브라우저는 태그를 객체화시켜 정보를 저장한다.  따라서 javascript에서 이미지의 크기를 키우고 싶다면, 이미지 객체를 찾아 그 객체가 가지고 있는 width속성에 값을 대입해주면 된다.

```.{javascript}
var imgs = document.getElementsByTagName('img');

imgs[0].style.width = '50px';
```

![img](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/904/2229.png)



(source : http://learn.javascript.ru/browser-environment)

* window는 전역객체이므로 window.document라고 작성하지 않고 document라고 작성해도 됨.
* document,navigator,Object등등은 window의 property임.
* javascriptcore에서는 object,array,function등 객체를 가지고 있음.

```
javascript의 역할

​	웹페이지에 기능을 더해 HTML 웹페이지를 동적이고 살아 있게 만드는 것.
```

이 말에 따르면 javascript는 객체를 통해 접근하여 동적이고 살아 있게 만들 수 있게 됨.