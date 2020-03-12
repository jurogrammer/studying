# DOM에 대하여

#### DOM 도입배경(Document Object Model)

브라우저가 화면을 그리고 끝이 아님. HTML문서를 변경한다. HTML문서를 접근해서 변경하기 위하여 DOM이라는 객체 형태의 모델로 HTML코드를 저장함.  접근을 위해 브라우저는 DOM API를 제공한다. 

이렇게 저장된 정보를 **DOM Tree** 라한다.

![DomTree](https://cphinf.pstatic.net/mooc/20180126_280/1516956194218XFPk5_PNG/2-2-2_Dom_tree.png)

(출처 : https://www.edwith.org/boostcourse-web/lecture/16699/)

Dom Tree 접근 API

루트 객체 => document

document에 getElementbyId 등등으로 접근 가능

cssSelector로 또 접근 가능.

* . -> class
* \# -> id
* \> -> 하위 태그
* 등등

!!! 텍스트조차 객체로 저장됨.!!!



