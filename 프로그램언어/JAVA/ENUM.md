# ENUM

> TodoList 만들기 프로젝트에서 다음과 같은 코드 리뷰를 받았다. 
>
> "서비스 명세에 있는 값은 enum을 사용하세요. 이렇게 하면 오타로 인한 실수 방지 및 type safe한 코드를 작성할 수 있습니다."
>
> java와 c는 다른 면이 있어 강의를 통해 정리하여 본다.



참고 

* https://opentutorials.org/module/516/6091 (생활코딩)
* https://woowabros.github.io/tools/2017/07/10/java-enum-uses.html (우아한 형제 기술 블로그)





## enum 사용 목적



```java
public class ConstantDemo {
    public static void main(String[] args) {
        /*
         * 1. 사과
         * 2. 복숭아
         * 3. 바나나
         */
        int type = 1;
        switch(type){
            case 1:
                System.out.println(57);
                break;
            case 2:
                System.out.println(34);
                break;
            case 3:
                System.out.println(93);
                break;
        }
    }
 
}
```

#### 위 코드의 문제점

1. 주석이 사라질 경우 의미를 이해하기 힘들다.
2. 주석과 코드의 거리가 멀어질 경우 이해하기 힘들다.



### 개선된 코드1

```java

public class ConstantDemo {
    private final static int APPLE = 1;
    private final static int PEACH = 2;
    private final static int BANANA = 3;
    public static void main(String[] args) {
        int type = APPLE;
        switch(type){
            case APPLE:
                System.out.println(57+" kcal");
                break;
            case PEACH:
                System.out.println(34+" kcal");
                break;
            case BANANA:
                System.out.println(93+" kcal");
                break;
        }
    }
}
```

#### 개선사항

1. 이름만 보면 무엇인지 알 수 있음.



#### 문제점

1. 상수 선언이 추가될 경우 중복발생.

```java
private final static int GOOGLE = 1;
private final static int APPLE = 2;
private final static int ORACLE = 3;
```

​	final로 선언한 APPLE 변수에 새로 값을 할당하려 했기에 에러 발생.

​	프로젝트의 규모가 커질수록 중복발생 가능성 높아짐



### 개선된 코드2

접두사를 통해 구분

```
    private final static int FRUIT_APPLE = 1;
    private final static int FRUIT_PEACH = 2;
    private final static int FRUIT_BANANA = 3;
     
    // company
    private final static int COMPANY_GOOGLE = 1;
    private final static int COMPANY_APPLE = 2;
    private final static int COMPANY_ORACLE = 3;
```



#### 개선사항

충돌가능성 훨씬 낮아짐



#### 개선된 코드3

인터페이스를 통해 해결

```java
 
interface FRUIT{
    int APPLE=1, PEACH=2, BANANA=3;
}
interface COMPANY{
    int GOOGLE=1, APPLE=2, ORACLE=3;
}
 
public class ConstantDemo {
     
    public static void main(String[] args) {
        int type = FRUIT.APPLE;
        switch(type){
            case FRUIT.APPLE:
                System.out.println(57+" kcal");
                break;
            case FRUIT.PEACH:
                System.out.println(34+" kcal");
                break;
            case FRUIT.BANANA:
                System.out.println(93+" kcal");
                break;
        }
    }
}
```

#### 개선 사항

* 충동가능성 x
* 문법으로 개선함으로써 훨씬 좋은 코드가 됨

#### 문제점

* 위와 같이 구현할 경우 비교할 수없는 대상을 비교
  *  FROUIT의 APPLE과 COMPANY의 APPLE을 비교하려 함. 만약 두 값이 동일했을 경우 비교할 때 TRUE.



#### 어떻게 개선할까?

* 위의 문제는 같은 int타입으로 정의했기 때문에 발생한 문제
* 따라서 다른 그룹에 있도록 정해준다. 즉, 다른 클래스로 선언



## 개선된 코드3

```java
package org.opentutorials.javatutorials.constant2;
 
class Fruit{
    /*APPLE을 Fruit 클래스 타입으로 선언, Fruit객체를 담는다.*/
    public static final Fruit APPLE  = new Fruit();
    public static final Fruit PEACH  = new Fruit();
    public static final Fruit BANANA = new Fruit();
}
class Company{
    public static final Company GOOGLE = new Company();
    public static final Company APPLE = new Company();
    public static final Company ORACLE = new COMPANY(Company);
}
 
public class ConstantDemo {
     
    public static void main(String[] args) {
        if(Fruit.APPLE == Company.APPLE){//compile error 발생
            System.out.println("과일 애플과 회사 애플이 같다.");
        }
    }
}
```

#### 개선된 사항

* compile이 에러를 검출해줌으로써 사전에 에러 차단 가능
  * Fruit객체와 Company객체는 비교할 수 없으므로 compiler가 값을 비교할 수 없다고 컴파일 에러 발생.

#### 문제점

* switch는 int...등 객체만을 변수에 담을 수 있음. 즉, fruit,company객체는 switch 변수에 넣을 수 없다.

#### 어떻게 해결할까?

* switch 내에 enum은 받을 수 있음. enum을 이용하자!



## 개선된 코드4

enum을 이용한다.

```java
package javapractice;

/*
class Fruit{
	public static final Fruit APPLE = new Fruit();
	public static final Fruit PEACH = new Fruit();
	public static final Fruit BANANA = new Fruit();
}
*/

//위 fruit와 동일한 의미. 컴파일하면 class형태.
enum Fruit{
	APPLE, PEACH, BANANA
}

public class EnumExample {
	public static void main(String[] args) {
		Fruit type = Fruit.APPLE;
		switch(type) { //type의 class가 Fruit라는 걸 알기에 case에 값만 넣어도 알 수 있음.
			case APPLE:
				System.out.println(57);
				break;
			case PEACH:
				System.out.println(34);
				break;
			case BANANA:
				System.out.println(93);
				break;
		}
	}
	
}


```

#### 개선된 사항

* 아주 깔끔해짐.
  * class로 선언할 시 (주석부분) 만들다 만건지 헷갈릴 수도 있음
  * 보기 편함



## 추가 내용1(생성자)



```java
package javapractice;

/*
class Fruit{
	public static final Fruit APPLE = new Fruit();
	public static final Fruit PEACH = new Fruit();
	public static final Fruit BANANA = new Fruit();
}
*/

//위 fruit와 동일한 의미. 컴파일하면 class형태.
enum Fruit{
	APPLE, PEACH, BANANA;
	
	Fruit() {
		System.out.println("Call Constructor");
	}
}

public class EnumExample {
	public static void main(String[] args) {
		Fruit type = Fruit.APPLE;
		switch(type) { //type의 class가 Fruit라는 걸 알기에 case에 값만 넣어도 알 수 있음.
			case APPLE:
				System.out.println(57);
				break;
			case PEACH:
				System.out.println(34);
				break;
			case BANANA:
				System.out.println(93);
				break;
		}
	}
	
}
```

#### 출력 결과

```
Call Constructor
Call Constructor
Call Constructor
57
```



#### 살펴볼 내용

* enum과 주석코드는 같기 때문에 call Constructor가 3번 호출된다.
  * 각각의 APPLE,PEACH,BANANA에 대해 Fruit객체를 생성하므로.



## 추가내용2(생성자로 특성부여)

```java
package javapractice;

/*
class Fruit{
	public static final Fruit APPLE = new Fruit();
	public static final Fruit PEACH = new Fruit();
	public static final Fruit BANANA = new Fruit();
}
*/

//위 fruit와 동일한 의미. 컴파일하면 class형태.
enum Fruit{
	//apple객체 생성시, 생성자로 "red"값을 넣어준다.
	APPLE("red"), PEACH("pink"), BANANA("yellow"); 
	
	//Fruit 또한 클래스이므로 생성자를 가질 수 있음. 각 생성자별 color 만들기
	public String color;
	
	Fruit(String color) {
		System.out.println("Call Constructor "+this);
		this.color = color;
	}
}

public class EnumExample {
	public static void main(String[] args) {
		Fruit type = Fruit.APPLE;
		switch(type) { //type의 class가 Fruit라는 걸 알기에 case에 값만 넣어도 알 수 있음.
			case APPLE:
				System.out.println(57+"kcal, color "+Fruit.APPLE.color);
				break;
			case PEACH:
				System.out.println(34+"kcal, color "+Fruit.PEACH.color);
				break;
			case BANANA:
				System.out.println(93+"kcal, color "+Fruit.BANANA.color);
				break;
		}
	}
	
}


```

#### 살펴볼 내용

각 과일 별로 색을 부여하자.(즉, 각 객체에 대해 특성 부여)

#### 과정

1. Fruit의 instance 변수로 color 만들기

2. 생성자에 color 변수 초기화

   1. 입력으로 color변수값 입력

      ```java
      APPLE("red")
      ```

   2. APPLE 객체 생성시 "red" 값 대입. 

      다음과 동등

      ```
      Fruit APPLE = new Fruit("red");
      ```

#### 결과

APPLE 객체에 color라는 인스턴스 변수가 생성된다.

Fruit.APPLE.color => "red"



#### 문제점

인스턴스 변수를 수정할 수 있음. private로 만들고 메소드를 만들어라.



## 추가내용3(인스턴스 변수 접근금지)

```java
package javapractice;

/*
class Fruit{
	public static final Fruit APPLE = new Fruit();
	public static final Fruit PEACH = new Fruit();
	public static final Fruit BANANA = new Fruit();
}
*/

//위 fruit와 동일한 의미. 컴파일하면 class형태.
enum Fruit{
	//apple객체 생성시, 생성자로 "red"값을 넣어준다.
	APPLE("red"), PEACH("pink"), BANANA("yellow"); 
	
	//Fruit 또한 클래스이므로 생성자를 가질 수 있음. 각 생성자별 color 만들기
	private String color;
	
	public String getColor() {
		return this.color;
	}
	
	Fruit(String color) {
		System.out.println("Call Constructor "+this);
		this.color = color;
	}
}

public class EnumExample {
	public static void main(String[] args) {
		Fruit type = Fruit.APPLE;
		switch(type) { //type의 class가 Fruit라는 걸 알기에 case에 값만 넣어도 알 수 있음.
			case APPLE:
				System.out.println(57+"kcal, color "+Fruit.APPLE.getColor());
				break;
			case PEACH:
				System.out.println(34+"kcal, color "+Fruit.PEACH.getColor());
				break;
			case BANANA:
				System.out.println(93+"kcal, color "+Fruit.BANANA.getColor());
				break;
		}
	}
	
}


```

#### 살펴볼 내용

* 인스턴스 변수는 수정못하도록 막는 것이 좋음. 따라서 메소드를 이용하여 color 값을 불러옴.





#### 추가 필요한 내용

* enum을 이용하면 안에 어떤 값이 있는지 확인하기 어려움

* 다음 메소드를 이용하면 됨.

  * ```java
    for(Fruit f : Fruit.values()){
    	System.out.println(f+", "+f.getColor());
    }
    ```

  * 출력결과

    ```java
    APPLE, red
    PEACH, pink
    BANANA, yellow
    ```

  