# [eclipse]java version 14이용 문제

### 문제

![캡처](C:\Users\Ju\Desktop\캡처.PNG)

eclipse에서 java 컴파일 버전을 14로 맞추기 위해 maven아래와 같이 설정해주고

```xml
    <plugin>
      <artifactId>maven-compiler-plugin</artifactId>
      <version>3.8.0</version>
      <configuration>
      	<source>14</source>
      	<target>14</target>
      </configuration>
    </plugin>
```
해당 메이븐 프로젝트의 .settings에 들어가 facet을 14로 바꿔줬다.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<faceted-project>
  <fixed facet="wst.jsdt.web"/>
  <installed facet="jst.web" version="3.1"/>
  <installed facet="wst.jsdt.web" version="1.0"/>
  <installed facet="java" version="14"/>
</faceted-project>

```

그런데 problem 발생.

![캡처](C:\Users\Ju\Desktop\캡처.PNG)

내가 설정하려 한 java 컴파일 버전과 설치된 자바 버전이 맞지 않는다고 한다.

### 중간에 알게 된 것.

* java 라이브러리는 C:\Program Files\Java\jdk-14.0.1\lib의 jrt-fs.jar에 존재한다.
* 자바 개발이 아닌 실행 관련은 jre가 담당한다. 즉, 컴파일 java 버전이 14여야 한다는 것은 jre의 version이 14여야 한다는 것을 의미한다.

* preference -> java -> compile 을 가면 현재 선택된 컴파일 버전을 알 수 있다.
* java 최신 버전은 이전 버전에 대한 se를 가지고 있다.

### 시도한 방안들

#### 1. java 최신버전 설치 (해결 x)

eclipse최신버전이 java 14를 지원해준다길래 java 2020-03을 설치했는데 동일한 오류가 발생한다.

#### 2. eclipse 시작시 vm 설정 (해결 x)

![캡처3](C:\Users\Ju\Desktop\캡처3.PNG)

* jdk 13으로 되어 있어 14버전으로 바꾸어 주었다.

#### 해결 x

* vm은 virtual machine의 약자. eclipse 실행시 jvm위치를 참고하여 실행하는 것이다.  jre가 바뀌지 않았으므로 잘못된 방법.(java 14버전을 이용하려면 vm 14버전이 필요하다면 말이 달라지긴 한다.)



#### 3. 혹시 jre version은 13이 아닐까? -> openjdk 확인 (해결 x)

* https://jdk.java.net/14/에서 확인한 결과 jre 14버전을 지원해준다.
  * java se는 java에 필요한 라이브러리가 들어간 것을 의미.(standard edition) 즉, 자바14버전 라이브러리 가 들어가 있다. 

![캡처6](C:\Users\Ju\Desktop\캡처6.PNG)



#### 4. eclipse자체가 지원 못해주는 거 아닌가? 이정도면. eclipse 홈페이지를 들어가보자. (해결 o)

* 아래 두 사진을 보면 14버전 선택이 없다. eclipse가 지원 못해주는거라 봐도 무방. 따라서 홈페이지를 들어갔다.

![캡처4](C:\Users\Ju\Desktop\캡처4.png)![캡처5](C:\Users\Ju\Desktop\캡처5.PNG)



* https://www.youtube.com/watch?time_continue=28&v=XoUvOTiVaDc&feature=emb_title

  이 영상이 띄어있더라. 즉, eclipse 최신버전은 4월 15일날 버전을 의미. 이것은 eclipse의 market place를 설치하여 다운 받을 수 있단다.

그렇다... 최신버전은 03이 아니라 마켓 플레이스로 받을 수 있는 04-15...란다.



### 평

유독 java는 c언어나 파이썬에 비해 환경설정하는게 엄청 고되다.