# 참고자료

* effective java 3rd edition



# 초고

You need to be familiar with the customary and effective ways to structure your code.

보통 프로그램 언어 책은 그 자체의 속성인 반면, 사용성(usage)는 해당 언어를 사용하는 커뮤니티 속성이라고 볼 수 있기 때문입니다.

그리고 이러한 사용성은 시간이 흐르면서 바뀔 수 있지요.

조슈아 브로치는 Sun에서 자바 프로그램을 확장하고 구현하고 사용하는 것에 몇년을 보냈습니다. 자신을 포함한 다른 사람들의 많은 코드를 알고 있지요. 여기에서 그는 좋은 조언을 해줄 것 입니다.



# Chapter 1 Introduction

이 책은 java 언어와 기초적인 libraries를 효과적으로 사용할 수 있도록 고안되어 있습니다.

기초적인 라이브러리는 다음을 가리킵니다.

* java.lang
* java.util
* java.io
* subpackages
  * java.util.concurrent
  * java.util.function



### 아이템들

그리고 이 책은 90가지의 item으로 구성되어 있습니다. 각각은 하나의 룰을 나타내죠. 그리고 각각의 아이템은 11개의 챕터로 약하게 묶여 있습니다.

각 챕터는 software design의 넓은 관점을 나타내며 아이템들은 상호 참조되어 책을 통해 책을 읽는 코스를 정할 수 있게 합니다.



### 용어 정리



#### 몇가지 용어에 대하여 Java Language Specification(이하 JSL)과 다른 용어를 사용할 것입니다.

1. JSL과 달리 inheritance는 subclassing과 동의어입니다.
2. inheritance for interface란 용어 대신 a class implement an interface 또는 interface extends anothor이라고 표현할 것입니다.



#### JSL에 정의되지 않은 기술적인 용어를 사용할 것입니다.

1. exportAPI, simply API는 인터페이스 또는 패키지에 접근하는 classes, interfaces, constructors, members, and serialized forms를 의미합니다.(API elements)
2. API를 사용하는 프로그램을 만드는 프로그래머를 user of the API라고 부르고
3. API를 사용하는 코드가 구현된 클래스를 client of the API라고 부릅니다.

