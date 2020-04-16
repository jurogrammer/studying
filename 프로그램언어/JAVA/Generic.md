# Generic

>java에서 ''<>'' 기호가 자주 보인다. 
>
>어떤 느낌인지는 알겠지만, 명확히 알고자 강의를 본 내용을 정리하여본다.



## 출처

https://opentutorials.org/module/516/6237 (생활코딩)



## 정의

클래스 내부에서 사용할 데이터 타입을 외부에서 지정하는 기법을 의미.



## 예시

```java
class Person<T>{
	public T info;
}

Person<String> p1 = new Person<String>();
Person<StringBuilder> p2 = new Person<StringBuilder>();
```

1. Class Person\<T>

   * T가 어떤 타입인지 명시되지 않음
   * T가 info 타입이므로 info타입 또한 명시되지 않은 것.

2. new Person\<String>();

   * String 타입으로 명시하여 Person 생성
   * 그에 따라 info 또한 String타입으로 명시됨.

3. Person\<String> p1

   * 생성된 객체가 String 타입으로 명시된 객체이므로 p1의 타입 또한 String 타입으로 명시된 형상이여야 함. 

     그래서 Person\<String>

4. StringBuilder도 위와 같은 논리.



## 사용하는 이유

> generic은 늦게 추가된 기능. 
>
> 어떤 어려움 때문에 이 기능이 추가되었는지 알아보자.



#### 예제

```java
package javapractice;

class StudentInfo{
	public int grade;
	StudentInfo (int grade) {
		this.grade = grade;
	}
}

class StudentPerson{
	public StudentInfo info;
	StudentPerson(StudentInfo info){
		this.info = info;
	}
}

class EmployeeInfo{
	public int rank;
	EmployeeInfo (int rank){
		this.rank = rank;
	}
}

class EmployeePerson{
	EmployeeInfo info;
	EmployeePerson (EmployeeInfo info){
		this.info = info;
	}
}
public class GenericExample {
	public static void main(String[] args) {
		StudentInfo si = new StudentInfo(2);
		StudentPerson sp = new StudentPerson(si);
		System.out.println(sp.info.grade);
		EmployeeInfo ei = new EmployeeInfo(1);
		EmployeePerson ep = new EmployeePerson(ei);
		System.out.println(ep.info.rank);
	}
}

```

#### 문제점

* StudentPerson과 EmployeePerson은 동일한 구조이므로 중복.
  * 유지보수 측면에서 불이익



#### 개선

* StudentPerson과 EmployeePerson을 공통인 클래스 Perosn 생성.
* 이때, info에 대한 객체는 다르므로 공통인 조상 Object로 받음.



개선된 코드

```java
package javapractice;

class StudentInfo{
	public int grade;
	StudentInfo (int grade) {
		this.grade = grade;
	}
}

class EmployeeInfo{
	public int rank;
	EmployeeInfo (int rank){
		this.rank = rank;
	}
}

class Person{
	public Object info;
	Person(Object info){
		this.info = info;
	}
}

public class GenericExample {
	public static void main(String[] args) {
		Person p1 = new Person("부장");
        //info는 Object라는 일반적인 객체이므로 EmployeeInfo 형변환.
		EmployeeInfo ei = (EmployeeInfo)p1.info;//compile 단위에서 에러메세지 x. 실행하면 에러 발생. => type safe하지 않다.
        System.out.println(ei.rank);
	}
}

```



#### 문제점

* Person에 다른 객체를 집어넣어도 작동됨.
  * 추후 Person에 대한 내용을 잊고 전혀 다른 객체 삽입
  * 그럼에도 문법적으로는 잘못되지 않음
    * 찾기 어려움
    * 심각한 버그 초래

* 코드의 중복을 제거함으로써 더 좋은 코드를 만들었다고 생각하나, Object로 일반화 시킴으로써 엉뚱한 객체가 들어와도 compile에서 체크하지 못함.
  * 즉, type-safe하지 않다.
  * type-safe : 해당 type에 해당 type만 들어올 수 있도록 한다.



## Generic 탄생 배경

* 중복제거
* type - safe



#### Generic을 이용한 코드

```java
class Person<T, S>{
	public T info;
	public S id;
	Person(T info, S id){
		this.info = info;
		this.id = id;
	}
}

public class GenericExample {
	public static void main(String[] args) {
		Integer id = new Integer(1);
		Person<EmployeeInfo, Integer> p1 = new Person<EmployeeInfo, Integer>(new EmployeeInfo(1), id);
		System.out.println(p1.id.intValue());
				}
}
```

* id는 int 타입. 
* int는 객체가 아님.
* 따라서 int를 나타내주는 객체 필요
* 그것이 바로 Integer (wrapper class)
* 따라서 Integer를 사용하여 int 타입 객체를 만들어준다.

* 추가 : new Integer는 JAVA 9이후로 deprecated 됬다 한다.

  * https://runestone.academy/runestone/books/published/csawesome/Unit2-Using-Objects/topic-2-8-IntegerDouble.html 내용을 참조하면 선호하는 방법은 다음과 같다.

    ```java
    Integer id = 1;
    ```

#### 줄일 수 있는 내용

```java
Person<EmployeeInfo, Integer> p1 = new Person<EmployeeInfo, Integer>(new EmployeeInfo(1), id);
```



```java
		EmployeeInfo e = new EmployeeInfo(1);
		Integer i = 10;
		Person p1 = new Person(e,i);
		System.out.println(p1.id);
```

위와같이 e의 타입과 i의 타입을 명시해주면 Generic 명시 필요 없음. 컴파일이 e와 i가 어떤 타입인지 알 수 있으므로.



#### 메소드에도 사용가능

```java
class Person<T, S>{
	public T info;
	public S id;
	Person(T info, S id){
		this.info = info;
		this.id = id;
	}
	public <U> void printInfo (U info) {
		System.out.println(info);
	}
}

public class GenericExample {
	public static void main(String[] args) {
		EmployeeInfo e = new EmployeeInfo(1);
		Integer i = 10;
		Person p1 = new Person(e,i);
		p1.<EmployeeInfo>printInfo(e);
		//p1.printInfo(e);와 동치. e가 어떤 타입인지 알 수 있으므로.
		}
```





#### 문제

* generic에 어떤 값이든 들어올 수 있게 됨.



#### 개선사항

abstract나 interface를 이용하여 제한.

```java
package org.opentutorials.javatutorials.generic;
/*
abstract도 가능

abstract class Info{
    public abstract int getLevel();
}
*/
interface Info{
    int getLevel();
}
/*class EmployeeInfo extends Info도 가능*/
class EmployeeInfo implements Info{
    public int rank;
    EmployeeInfo(int rank){ this.rank = rank; }
    public int getLevel(){
        return this.rank;
    }
}
//abstract든 info든 T extends Info 구문은 동일.
class Person<T extends Info>{
    public T info;
    Person(T info){ 
        this.info = info; 
        //info가 가진 getLevel은 이용가능.
        info.getLevel();
    }
}
public class GenericDemo {
    public static void main(String[] args) {
        Person p1 = new Person(new EmployeeInfo(1));
        Person<String> p2 = new Person<String>("부장");
    }
}
```

* T는 Info의 자식만 받도록 특정지음.

  ```java
  class Person<T extends Info>
  ```
  * 이때 Info는 interface, abstract 둘 다 허용가능

* Info가 지닌 method만 사용 가능.

  ```java
  info.getLevel();
  ```
  * Info가 지니지 못한 메소드를 사용하려 한다면 에러 발생





# 총평

generic의 목적은 코드의 중복을 방지하기 위해서.

1. 같은 구조의 클래스들이면 하나의 클래스를 만들어 주어야 한다.
2. 그런데 내부에서 입력받는 클래스가 다르면 이때 와일드카드인 Generic을 이용하여 선언한다.
   * Object로 받으려 할 경우 type-safe하지 못하다.
3. type-safe를 보장하기 위해서 <와일드 카드 extends classType>을 정해준다.
   * 이러면 확장한 classType에 대해서만 값을 받을 수 있게 된다.



즉, 중복을 방지하기 위해서 도입했으나 type-safe 문제로 문법이 좀 복잡해졌다.