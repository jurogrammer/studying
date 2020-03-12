## ROOT폴더에 servlet을 작성한 배경

edwith를 통하여 풀스택 개발자 부스트코스를 수강 중인데, 프로젝트1의 과제로 localhost:8080/servlet 와 같은 ROOT 경로를 통해서 홈페이지를 구축해야만 하는 것으로 오해했다. 

html 파일은 ROOT폴더 구성을 보아 ROOT폴더에 그대로 넣으면 될 것으로 보였고 무난히 실행됬다. (시작 디렉토리가 ROOT로 되어 있는 듯 하다.)

하지만 servlet은...? eclipse의 도움을 받아 작성했기 때문에 여정이 시작됬다.



***Tomcat과 Java에 대한 이해도가 낮아 많이 헤맸고 그만큼 많이 이해하게 되었다.***



<u>*추측은 밑줄 밑 기울이기 처리하겠습니다.*</u>

## 실행 과정 

**Tomcat의 디렉토리 구조** 및 **Servlet실행 절차**에 대해 알아야 한다.!!



1. Tomcat폴더엔 톰캣 실행에 필요한 폴더와 **webapps**폴더가 존재한다.

   webapps은 웹 어플리케이션을 담은 폴더라 할 수 있다. <u>*톰캣을 실행하면 webapps로 디렉토리가 기본 설정되어 있는 것 같다.*</u> 

   따라서 Tomcat을 실행하고 http를 http://localhost:8080/[webapps 내의 폴더명] 로 요청하면 webapps 로 접근하여 해당 내용을 전송한다.

   * 그래서인지 webapps에 있는 기본 폴더들의 이름이 example,docs,ROOT등이 있다. 웹 어플리케이션의 정의를 이해한다면 폴더명들이 수긍이 될 것이다.

2. webapps폴더엔 서블릿을 실행시키기 위한 WEB-INF 폴더 및 web.xml파일을 생성해야 한다.

   톰캣은 http://localhost:8080/firstapp(webapps폴더명)/myfirstservlet이란 서블릿 요청을 받으면 webapps\firstapp\WEB-INF\classes 폴더에 들어가 서블릿 이름이 있는지 확인 후 내용을 전송한다.  그런데 모종의 이유로 해당 서블릿 파일의 이름과 url주소를 분리해놓았다. 그래서 myfirstservlet은 서블릿의 이름이 아닌 서블릿에 맵핑된 url이라 보면 된다.

   맵핑과 같은 서블릿에 대한 내용들은 WEB-INF 폴더명답게 WEB-INF\web.xml에 기록되어 있다. 해당 폴더에서 survlet을 지정하기 위해 class명을 기입해줘야 한다.

   ```.{xml}
     <servlet>
       <servlet-name>example</servlet-name>
       <servlet-class>FirstServlet</servlet-class>
     </servlet>
     <servlet-mapping>
       <servlet-name>example</servlet-name>
       <url-pattern>/myfirstservlet</url-pattern>
     </servlet-mapping>
   ```

   servlet-name은 임의로 지정한 servlet이름이라 볼 수 있고, (<u>*mapping의 Key가 될 애인 듯*</u>) servlet-class엔 요청하고 싶은 servlet의 class명을 적어주면 된다. 여기서 java는 객체지향 언어로, <u>*클래스로 관리하므로 파일명보단 클래스명이라고 말해주는 것 같다.*</u>

   그리고 mapping부분에서 내가 지정한 servlet이름에 대해 url주소를 입력해주면 된다. 위의 경우에선 /myfirstservlet이라 지정했으므로 http://localhost:8080//firstapp/myfirstservlet 같이 작성하여 요청하면 서블릿데이터를 받을 수 있다.

   **여기서 중요한건 !!classes내 class파일들은 compile되어 있어야 한다.**

   compile은 tomcat의 lib에서 servlet-api.jar와 작성한FirstServlet.java파일을 컴파일 해준다. (java에 대해 잘 몰랐다; 이 부분은 링크와 같은 느낌이다. FirstServlet.java 클래스를 servlet-api.jar와 묶어서 컴파일 해줌)

   ```
   javac -cp 생략\lib\servlet-api.jar 생략\FirstServlet.java
   ```

   이렇게 컴파일 해주면 class파일이 생성되고 이를 WEB-INF\classes에 넣어주면 된다.



## 왜 헤맸는가?

#### 1. java에 대한 이해가 부족했다.

class명 기입시 edwith 예시에선 firweb.helloservlet이여서 반드시 .이 필요한 줄 알았는데 helloservlet.class 파일을 접속하기 위한 표현이였다. firweb폴더에 helloservlet이 있다는 것. 

그리고 .class가 컴파일된 파일인지도 몰랐다. tomcat은 compile하여 실행하기보단 이미 compile된 코드를 실행한다. 다른 소프트웨어들도 그럴 것 같다.

#### 2.Tomcat디렉토리 및 실행과정을 가볍게 넘어갔다.

Tomcat을 사용하기 위해 정해진 틀(디렉토리)를 이해하고 접근해야 했으나 강의의 설명에 불구하고 가볍게 여겼다. 그래서 이해한 내용을 바탕으로 servlet을 실행한 것이 아닌, 남들이 한 것을 그대로 베끼기에 급급했고 여러 시행착오를 겪을 수 밖에 없었다. webapps에 폴더를 생성해서 servlet을 실행해보기도, ROOT 폴더의 WEB-INF가 아닌 ROOT에 servlet파일을 넣어보기도 했다. 아주 난장판~

### 보충 방안

1 -> java를 두시간 정도 시간투자해주자. 앞부분부터 정독!

2 -> Tomcat설명 부분을 다시 듣고 정리해보자.