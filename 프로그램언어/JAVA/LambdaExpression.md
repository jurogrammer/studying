# 출처

* https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html



# 개요

anonymous class가 새로 선언하기엔 애매해서 심플하게 만드는 방법이라고 할 때, 만약에 메소드가 하나만 있는 경우를 고려해보자. 이러면 클래스의 의미가 불분명해질 수 있다. 

이럴 경우엔 다른 메소드에 기능만(functionality) argument로 넘기는걸 생각해볼 수 있다. 예를 들어서 버튼이 눌렸을 때 어떤 기능을 수행할 지 넘겨주는 것 말이당.

Lambda expression은 이것을 가능하게 하며, functionality를 method argument로, 또는 코드를 data로 볼 수 있게 해준다.





# Ideal Use Case for Lambda Expressions

social networking application 고려.

관리자가 특정 액션을 할 수 있도록 하는 기능을 만들고 싶습니다.

메세지 보내거나 





you need to implement a functional interfa