# Redirect and Forwarding



## Redirect

A에 자원을 요청 보냈을 시, A는 B에게 요청하라는 메세지를 보내는 것.

#### 비유

부서 A에게 전화를 했지만 A가 부서 B 관할이라며 B 전화번호 넘겨줌. 전화한 사람은 B 전화번호를 통해 B와 연결.

#### 특징

redirect의 번호는 302

A와 연결되있던 request, reponse 객체와 B와 연결된 request, response객체는 다르다.

리다이렉트시 더 이상 필요가 없기에 소멸됨.

#### servlet구현

**Point. A에게 response로 응답 302를 보내주어야 하고 redirect할 주소를 전해주어야 함.**

이때, response의 sendRedirect 메소드를 통해 구현

response.sendRedirect("리다이렉트할 자원의 위치");

```java
response.sendRedirect("redirectPage");
```







## forwarding

클라이언트의 요청을 A가 일부 수행 후 B에게 전달한 후 B가 마무리 작업 한다음 클라이언트에게 응답함.

#### 비유

A가 전화를 받으면 A가 할 수 있는 작업을 한 다음에 B부서에 넘어가서 고객의 요청 내용을 전달 한 후에 B부서가 클라이언트에게 전화하여 내용처리.

#### 특징

클라이언트와 A간 생성된 request,response객체를 B에게 전달해줌. 즉, request,reponse객체가 유지된다.

일부 값 수행시 request 객체에 값을 전달하여 사용한다.(request,response scope)



#### servlet구현

**point. A에게 생성된 request,response 객체를 B에게 보내줘야 함!**

이때,  response.Dispatcher를 이용하여 위를 수행한다.

```java
RequestDispatcher requestDispatcher = request.getRequestDispatcher("/forwardingTest2");
requestDispatcher.forward(request, response);
```

위와 같이 request.getRequestDispatcher에 forwarding할 url을 넘겨서 requestDispatcher 객체 생성(이때 반드시 슬래쉬 붙일 것.)

requestdispatcher 객체에 forwarding할 request와 response를 담아준다.