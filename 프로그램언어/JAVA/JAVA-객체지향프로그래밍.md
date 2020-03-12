# JAVA-객체지향프로그래밍

#### 클래스와 인스턴스 그리고 객체

------

> 목표
>
> * 클래스와 인스턴스 그리고 객체의 차이를 알자

##### 클래스

* 설계도

##### 인스턴스

* 부품

##### 객체

* 논란이 많은 정의이다. https://www.facebook.com/groups/codingeverybody/permalink/569274196446454/ 위 페이스북 토론을 보면 알 수 있겠지만 좀 더 추상적인 내용이라 본다. 클래스의 인스턴스는 객체! 라고 이해하고 넘어가겠다.



#### 클래스 멤버와 인스턴스 멤버

----

>목표
>
>* 멤버의 정의를 알 수 있다
>* 클래스 멤버와 인스턴스 멤버가 무엇인지 알 수 있다.



##### 멤버(member)

* 멤버는 구성원이라는 뜻

##### 인스턴스 멤버

* 인스턴스의 멤버로는 그 인스턴스가 가지고 있는 변수와 메소드가 있다.

##### 클래스 멤버

##### 	클래스 변수

* 클래스 멤버로는 그 클래스에 속한 인스턴스들이 있다. 인스턴스들이 공통의 값을 가지게 하기 위해 변수를 클래스 멤버로 선언해주면 된다. 예를 들어 계산기에서 원주율기능.

```.{java}
package org.opentutorials.javatutorials.classninstance;
 
class Calculator {
    static double PI = 3.14;
    int left, right;
 
    public void setOprands(int left, int right) {
        this.left = left;
        this.right = right;
    }
 
    public void sum() {
        System.out.println(this.left + this.right);
    }
 
    public void avg() {
        System.out.println((this.left + this.right) / 2);
    }
}
 
public class CalculatorDemo1 {
 
    public static void main(String[] args) {
 
        Calculator c1 = new Calculator();
        System.out.println(c1.PI);
 
        Calculator c2 = new Calculator();
        System.out.println(c2.PI);
 
        System.out.println(Calculator.PI);
 
    }
 
}
```

* 클래스 멤버에 접근하는 방법

  ```.{java}
  Calculator.PI
  ```

##### 클래스 변수 용도

* 인스턴스를 생성할 필요가 없는 값을 클래스에 저장하고 싶은 경우
* 값의 변경 사항을 모든 인스턴스가 공유해야하는 경우

##### 클래스 메소드

* 클래스에서 제공한 메소드 인스턴스들이 공통으로 가짐

* ```.{java}
  public static void sum(int left, int right){
          System.out.println(left+right);
      }
  ```

##### 클래스 메소드 용도

* 인스턴스 변수를 참조할 필요가 없을 경우. 인스턴스 변수 생성으로 인한 불필요한 메모리 생성을 막을 수 있다.

#### 상속

----

> 목표
>
> * 상속의 정의에 대해 이해할 수 있다.
> * 상속의 활용 방법에 대해 말할 수 있다.

##### 정의

* 새로운 객체에 기존 객체의 변수와 메소드를 물려주는 기능

##### 장점

* 기존 객체의 특징을 물려받아 새로운 객체를 만들고 싶으나, 소스를 변경할 수 없는 경우에도 상속 가능
* 객체가 다른 곳에 이미 사용되고 있을 경우 다른 곳에 불필요한 기능을 추가할 일이 없음.

##### 구현

```.{java}
class SubstractionableCalculator extends Calculator {
    public void substract() {
        System.out.println(this.left - this.right);
    }
}
```



#### 상속과 생성자

-----

##### 상속받을 때 생성자로 인한 문제점.

* 상속시 부모 클래스에 기본생성자 없이 생성자를 명시했을 경우, 자식 클래스에서 객체 생성할 때 값을 넣어주었더라도 기본생성자를 명시하라는 에러 문구가 나온다. 따라서 상속관점에서 재사용성을 위해서 super를 이용한다.

```.{java}
super(left,right);
```

부모 클래스 생성자에 left,right인자를 넘겨준다.

\** 상위 클래스 먼저 생성 후 초기화를 진행해야 한다.



#### overriding

------

상속시 부모가 물려준 메소드들 중 어떤 메소드에 대해서는 자식클래스에서 독자적인 기능을 재정의할 필요가 있음. 그 재정의하는 것을 오버라이딩이라고 한다.

##### 적용시 조건(메소드의 서명(signature))

* 부모의 메소드 자료형과 자식의 메소드 자료형이 같아야 한다.(리턴 타입이 동일해야 한다.)

* 이름이 같아야 한다.

* 파라미터의 갯수와 데이터 타입이 동일해야 한다.



##### 구현

* 부모클래스의 메소드명을 그대로 작성한다.

```.{}
class Calculator {
	int sum(int left,int right) {
		return (left+right);
	}
	int multiply(int left, int right) {
		return left*right;
	}
}

class Calculator2 extends Calculator{
	int sum(int left, int right) {
		return (left+right+10);
	}
}
```

##### 추가 사항

* super.avg()를 통해 부모 메서드를 호출할 수 있음

```.{java}
int sum(int left, int right){
	return super.sum(left,right);
}
```



#### overloading

-----

##### 정의

클래스의 메소드를 정의할 때 같은 이름이지만 서로 다른 매개변수의 형식을 가지고 있는 메소드를 여러개 정의할 수 있는 방법.

java에서는  메소드명이 동일하더라도 signature가 다르면 다른 메소드로 구분한다.

```.{java}
class Calculator {
	int sum(int left,int right) {
		return (left+right);
	}
	int multiply(int left, int right) {
		return left*right;
	}
	int sum(int one, int two, int three) {
		return one+two+three;
	}
}
```

##### overloading 규칙

* 리턴 타입이 다른 메소드를 정의한다면 오류를 발생시킨다. int A()과 void A()에서 반환시 어떤 메소드를 반환할 것인가 명확하지 않음. 따라서 오류를 발생시킨다.
* 파라미터의 수와 파라미터의 자료형이 메소드를 구분짓는 요소. 따라서 이름을 달리 하는 것만으로는 메소드를 구분할 수 없다. 그래서 오류 발생. void A(int a) void A(int b)오류 발생



#### class path

----

##### 정의

* 클래스가 존재하는 경로를 지정함으로써 클래스를 불러오는 방법

##### 방법

* exam.java 생성 (class Item(), class ClassDemo 선언)
* javac exam.java경로 -> class로 컴파일 완료
* 이때 Item.class과 ClassDemo.class 2개의 클래스 파일이 생성된다.

##### 실행시 발생할 수 있는 문제

예제 내용

```.java{}
class Item2{
    public void print(){
        System.out.println("Hello world");  
    }
}
 
class ClasspathDemo2 {
    public static void main(String[] args){
        Item2 i1 = new Item2();
        i1.print();
    }
}
```

* class를 못 찾는 경우
  * java ClasspathDemo2 cmd에서 실행하면 Hello world 출력됨
  * 만약 Item2가 다른 디렉토리가 없다면 출력안됨
  * 이때 java -classpath ".;lib" ClasspathDemo2로 입력하면 다음과 같은 의미이다
    * ClasspathDemo2를 컴파일하는데 . 현재 경로에서 검색해보고 여기에 없으면 .lib에서 검색해보아서 필요한 클래스를 찾아라.
    * 이말을 따르면 classpath의 default 값은 java -classpath "." ClasspathDemo2와 같다.

#### 환경변수

----

실행할 때마다 classpath를 지정해주면 매우 번거로운 일. 따라서 환경변수라는 운영체제 전역 변수에 위치를 지정해주면 된다.

##### 장점

* 매번 classpath를 지정해주지 않아도 실행가능.

##### 단점

* 운영체제가 변경되었을 경우 환경변수를 재설정해주어야 함.

##### 구현 방법

* 시스템 변수 ->CLASSPATH의 위치를 등록
* cmd 재시작
* java class명 만 입력해도 가능.

#### 패키지(package)

----

##### 배경

* 여러 사람들이 개발할 때 클래스의 중복이 존재할 수 있음. 이 충돌들을 막기 위해 package라는 것을 만들음

##### 패키지 생성 방법

* 패키지 접근

  ```.
  C:\Users\Ju\eclipse-workspace\javapractice\src\javapractice\overriding.java
  ```

  * C:\Users\Ju\eclipse-workspace\javapractice : 프로젝트 위치
  * src : 자바 소스코드가 담겨져 있는 위치
  * javapractice : 자바 패키지의 이름(위치)
  * overriding.java : 자바 소스코드 이름

  즉, 패키지는 일종의 디렉토리라 할 수 있다.

* 패키지 생성명

  * 도메인 이름 사용(조직의 명) -> 도메인은 중복될 가능성이 없기 때문에.

##### 타 패키지 접근법

* import 이용.     org.javapractice2패키지의 overriding2 소스코드에 있는 모든 클래스를 불러와라.

  ```.{java}
  import org.javapractice2.overriding2.*;
  ```

##### 자바에 패키지 표시법

* ```.{java}
  package org.javapractie2.overriding2;
  ```

  이와 같은 방식으로 해당 클래스 파일이 어떤 패키지에 위치하는지 나타낼 수 있음.

#### 손코딩(손코딩예시 폴더 참조)

----

##### 디렉토리 설명

* bin : byte code로 변환된 클래스 존재
* src : source code 존재.
* 패키지는 . <-은 다음 디렉토리를 의미. org.opentutorials -> org/opentutorials... 의미함.

##### 컴파일

* javac src/org/opentutorials/javatutorials/examples/example3/*.java -d bin

  자동으로 bin이란 디렉토리에 컴파일된 클래스파일이 저장되도록 할 수 있음.

  이때 \bin\org\opentutorials\javatutorials\examples\example3 이 디렉토리에 class파일이 저장된다.

##### 서로 다른 패키지에서 로딩한 동일한 클래스명이 존재할 경우

```.{java}
org.opentutorials.javatutorials.examples.example1.B b = new org.opentutorials.javatutorials.examples.example1.B();
```

* 임포트한 클래스가 위치한 패키지 명을 명시할 것.

#### API에 대해.

-----

```.{}
System.out.println(1);
```



* 지금까지 무수히 많은 예제에서 사용했던 코드다. 이것이 화면에 어떤 내용을 출력하는 것이라는 건 이미 알고 있다. 하지만 도대체 우리가 정의한 적이 없는 이 명령은 무엇일까?를 생각해볼 때가 왔다. 문법적으로 봤을 때 println은 메소드가 틀림없다. 그런데 메소드 앞에 Sytem.out이 있다. System은 클래스이고 out은 그 클래스의 필드(변수)이다. 이 필드가 메소드를 가지고 있는 것은 이 필드 역시 객체라는 것을 알 수 있다. 그리고 System을 인스턴스화한적이 없음에도 불구하고 필드 out에 접근할 수 있는 것은 out이 static이라는 것을 암시한다.