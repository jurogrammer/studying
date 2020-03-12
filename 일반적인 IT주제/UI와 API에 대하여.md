# UI와 API에 대하여

#### UI(user interface)

사용자와 접점이 되는 지점 user, inter,face 노트북에서의 키보드, 스피커 등등. 사용자와 시스템간 접점이 되어 서로 의사소통이 되도록 도와준다.

#### API(Application Programming Interface)

```.{javascript}
javascript:alert("Hello world");
```

생성된 경고창이 내가 만들었을까 안 만들었을까?

-> 만들기도 했고 안 만들기도 했음.

* 안만든 부분
  * 닫기버튼 확인버튼, 창밖 눌렀을 때 띠딩소리, 이미지 느낌표 등
* 만든 부분
  * 경고창 띄우기(alert 명령어를 브라우저에게 전달했음.)

경고창은 복잡한 애플리케이션인데 브라우저에게 만들으라고 얘기한 적이 없다.

따라서 alert는 브라우저와 얘기하기 위한 인터페이스라고 할 수 있다. 코드의 형태를 띈 인터페이스

경고창은 웹브라우저가 만들었음. 

윈도우 개발자들이 아이콘과 x버튼 확인버튼 등을 만들음. 웹브라우저 개발자가 미리 만들어진 application을 이용



##### 계층적 관계와 Interface

운영체제 -> browser -> webapplication

브라우저가 운영체제의 application을 가져다쓰고 web-app이 browser의 application을 가져다 쓴다.

browser입장에선 운영체제가 플랫폼이며, 그 플랫폼 사이를 이어주는 역할하는 것이 api이다.



![image-20200311134316311](C:\Users\Ju\AppData\Roaming\Typora\typora-user-images\image-20200311134316311.png)

(source 생활코딩:https://www.youtube.com/watch?v=Z4kH0IZVT-8&feature=emb_title )

한 눈에 이해되는 이미지.

웹개발자는 브라우저에게 도움받고 브라우저는 운영체제에게 도움받고... 

내가 하고 싶었던 것은 C언어 수준까지 가서 프로그램을 만들고 싶었다.라고 볼 수 있겠다.