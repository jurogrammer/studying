# 오류 내용

jsp파일을 실행시 한글이 깨져서 출력된다.

```
í•  ì¼ ë“±ë¡



ì–´ë–¤ ì¼ì¸ê°€ìš”?


ëˆ„ê°€ í• ì¼ì¸ê°€ìš”?


ìš°ì„ ìˆœìœ„ë¥¼ ì„ íƒí•˜ì„¸ìš”
•1ìˆœìœ„
•2ìˆœìœ„
•3ìˆœìœ„


< ì´ì „

ì œì¶œ

ë‚´ìš© ì§€ìš°ê¸°
```



#### 작성한 코드

```jsp
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>registerTodoThing</title>
</head>

<body>
<header class = "register-header">
    <h1 class = "register-header-h1">할 일 등록</h1>
</header>

<article class = "register-article">
    <div class = "wrapper-question">
        <div class = "question" id = "q1">어떤 일인가요?</div>
        
    </div>
    <div class = "wrapper-question">
        <div class = "question" id = "q2">누가 할일인가요?</div>

    </div>
    <div class ="wrapper-question">
        <div class = "question" id = "q3">우선순위를 선택하세요</div>
        <ul class = "slt-rank">
            <li class= "rank" id = "rank1">1순위</li>
            <li class= "rank" id = "rank2">2순위</li>
            <li class= "rank" id = "rank3">3순위</li>
        </ul>
    </div>
</article>

<footer class = "register-footer">
    <div class = "register-footer-nav" id = "pre"> &lt; 이전</div>
    <div class = "register-footer-nav" id = "submit">제출</div>
    <div class = "register-footer-nav" id = "eraise">내용 지우기</div>
</footer>
</body>
</html>

```

위와 같이 \<head>부분에서 utf-8임을 명시하였고 eclipse preference에서 utf-8로 지정해줬는데도 한글이 깨졌다.



# 문제 접근

html문서가 저렇다고 되있지만, 

jsp는 서블릿으로 변환되어 작동한다 ->  java에서 인코딩이 utf-8이 아니여서 깨진게 아닐까?

그래서 jsp로 작성했던 예제를 살펴보니 다음과 같은 코드가 눈에 띄었다.

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
```

이를 보면 위와 같은 속성의 값들을 명시해줘야 했던게 아닐까?



# 문제 해결 방안

#### 1.이전 JSP파일 참조하여 상단 property 입력

입력할 내용은

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
```

이와 같다.

이를 덧붙여 코드를 아래와 같이 수정하였다.

```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>registerTodoThing</title>
</head>

<body>
<header class = "register-header">
    <h1 class = "register-header-h1">할 일 등록</h1>
</header>

<article class = "register-article">
    <div class = "wrapper-question">
        <div class = "question" id = "q1">어떤 일인가요?</div>
        
    </div>
    <div class = "wrapper-question">
        <div class = "question" id = "q2">누가 할일인가요?</div>

    </div>
    <div class ="wrapper-question">
        <div class = "question" id = "q3">우선순위를 선택하세요</div>
        <ul class = "slt-rank">
            <li class= "rank" id = "rank1">1순위</li>
            <li class= "rank" id = "rank2">2순위</li>
            <li class= "rank" id = "rank3">3순위</li>
        </ul>
    </div>
</article>

<footer class = "register-footer">
    <div class = "register-footer-nav" id = "pre"> &lt; 이전</div>
    <div class = "register-footer-nav" id = "submit">제출</div>
    <div class = "register-footer-nav" id = "eraise">내용 지우기</div>
</footer>
</body>
</html>

```



결과는 아래와 같이 한글이 정상 출력되었다.

```
# 할 일 등록

어떤 일인가요?

누가 할일인가요?

우선순위를 선택하세요

- 1순위
- 2순위
- 3순위

< 이전

제출

내용 지우기
```