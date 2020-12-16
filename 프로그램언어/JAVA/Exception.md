# 출처

* https://docs.oracle.com/javase/specs/ (오라클 Java SE 8)



# 목표

1. Java SE 8의 Exception에 알아보고,

2. 프로그래밍 관점에서 Exception을 이해하자. (형식이 아닌 본질적인 부분)



# 들어가기 앞서서...

### 개요

프로그램이 자바 프로그래밍 언어의 의미적인 제약을 위반할 경우에 **JVM**은 **프로그램에** exception이라는 에러를 전송합니다.



자바는 의미적인 제약이 위반되거나 또는 프로그램에 의해 제어(control)가 전이될 수 있습니다. exception이 발생한 지점으로부터 프로그램이 명시한 지점으로의 전이 말이죠.



exception은 exception이 발생한 지점으로부터 던져졌다고 불릴 수 있으며, 통제가 전이된 지점에서 잡혔다고 볼 수 있습니다.



그리고 프로그램은 throw라는 statements를 통해서 명확하게 Exception을 던질 수 있습니다.

throw statements를 이용하면 오래된 스타일인 의미없는 숫자 표기로부터 벗어날 수 있습니다. 에러가 났을 때 -1, 0이런 값으로 표기하기보단, 에러를 객체로 던질 수 있다는 말이죠.



모든 Exception은 Throwable 클래스나 이것의 서브클래스 인스턴스로써 표현됩니다. 이러한 객체는 exception이 발생한 후 이 에러를 잡은 handler에게 정보를 전달하기 위해 사용될 수 있습니다.



Handlers는 try statements의 catch clauses에 생성됩니다.



exception을 던지는 과정 동안에 JVM은 현재 스레드에서 시작했지만 완전히 종료되지 않은 요소들을 하나하나씩 종료합니다.expression, statements, method등 말이죠.



이 과정은 해당 exception을 처리해줄 handler를 찾을 때까지 수행되며 해당 handler를 찾지 못한다면 uncaught exception handler에 의해 처리됩니다.



### try-catch의 어원 (추측)

자바 창시자인 제임스 고슬링은 캐나다 사람인데요. 캐나다는 아이스 하키가 유명합니다. 그래서 아이스하키에서 공을 던지고 이 공을 잡기 위한 노력을 프로그램으로 표현한 것 같습니다.

![](https://postfiles.pstatic.net/MjAyMDExMDlfMTA0/MDAxNjA0ODk3NTY1NTY3.KNRQalLenP_syDOHles88OIRCyDVYUB0kr9Pq0nHSpwg._L6TDrqOEgO240prjTpiQgOwDivMUlttG4QYAAmFcD4g.PNG.study_ju/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2020-11-09_%EC%98%A4%ED%9B%84_1.52.22.png?type=w966)

## 1. Exception 의 종류와 원인

### 1-1. Exception 종류

* Throwable
  * Exception
    * RuntimeException

* Error



* unchecked exception class => runtime exception 클래스나 error 클래스입니다. 이 예외들은 발생해도 복구하기 어렵다고 판단한 예외들이죠.

  

* checked exception class => unchecked exception class를 제외한 exception class. 다시 말해서 RuntimeException 타입, 이 타입의 서브타입, 그리고 에러타입 그리고 에러타입의 서브타입을 제외한 Throwable의 하위 클래스입니다.

  이 예외들은 발생할 경우 복구할 수 있다고 판단한 예외들입니다.



관계를 그림으로 정리하자면 아래와 같습니다.

<img src="https://postfiles.pstatic.net/MjAyMDExMDlfMjcz/MDAxNjA0ODk4MTQ3ODk2.oWoMgXRO79os9m7wDJYsHOdVHOvTaHXSaO_oU1G8PW8g.VnIbsXY60LPCJ5o4uViMpYZfP3f9ZguUeiGAZIPlywgg.JPEG.study_ju/SE-7b72ef9d-0246-4d35-ab50-4f05037dec6e.jpg?type=w966" style="zoom:67%;" />

### 1-2. Exception의 원인

1. throw statement가 실행될 경우

2. 비정상 실행 조건이 동기적으로 JVM에 의해 발견될 경우
   * 정수를 0으로 나누는 동작처럼 비정상적인 실행
   * 프로그램을 loading, linking, initializing할 동안의 에러
   * 내부 에러나 자원의 제한이 JVM이 자바 프로그램 언어로부터 실행을 막음. 이때는 VirtualMachineError의 서브클래스 타입 인스턴스가 던져짐.
3. 비동기 예외가 발생할 경우



### 1-3. 비동기 익셉션

대부분 Exception은 하나의 쓰레드에 의해 동기적으로 발생합니다. 그리고 특정한, 예상되는 포인트에서 예외가 발생하죠. 그런데 비동기 exception은 프로그램 실행 중에 잠재적으로 어떤 지점에서든지 발생할 수 있습니다.



#### 비동기 익셉션의 원인

1. Thread or ThreadGroup의 stop method의 실행(deprecated)
2. JVM에서 내부 에러나 자원의 제한으로 프로그램이 실행되지 못할 경우.

### 2. Compile-Time Checking of Exceptions 

형식자체가 잘못되었다!

Java 프로그래밍 언어는 프로그램이 method나 constructor의 실행에서 야기될 수 있는 checked exception의 처리를 포함하도록 요구합니다.



익셉션 핸들러가 존재하는지 이 컴파일 타임에 체킹하는 것은 적절히 처리되지 않은 예외들을 줄이기 위해서 디자인되었습니다.



throw절에 의한 각각의 checked exception은 해당 익셉션의 클래스나 해당 클래스의 수퍼 클래스 중 하나를 언급해야 합니다.



throw절에서 명명된 checked exception calss는 implementor와 method 또는 constructor간의 계약의 일부분입니다.



오버라이딩 메서드의 throw 절은 이 메서드가 해당 checked exception을 던지는 것을 명시하지 않을 수 있지만, interface에서는 반드시 명시해야 합니다.



unchecked exception class는 compile-time에선 확인하지 않습니다.

1. Error class

   프로그램에서 많은 부분에서 발생할 수 있으며, 복구하기가 어렵거나 불가능합니다. 프로그램이 해당 Exception을 선언하면 어수선하고(cluttered) 무분별(pointless)할겁니다. 하지만 매우 정교한 프로그램을 만든다면 이러한 조건들을 복구하려 하겠지요.

2. Run-time exception classes

   자바 프로그램 언어의 디자이너의 판단에 의해 프로그램의 정교함을 돕지 않습니다. 자바 컴파일러에게 런타임 중에 발생할 수 있는 에러를 알려줘봤자 해결할 수 있는게 없습니다. 그리고 해당 exception class를 설정하게 해줘봤자 프로그래머를 짜증나게 합니다.



특정 룰을 따른다면, statement나 expression이 exception class E를 던질 수 있다고 말할 수 있습니다.

catch clause가 잡을 수 있는 클래스를 잡을 수 있다고 말할 수 있습니다. (*We say that a catch clause can catch its catchable exception class(es):*)

* 각각의 catch clause에서 잡을 수 있는 익셉션 클래스는 exception parameter의 선언된 타입입니다.
* 여러 catch clauses에서 캐치 가능한 예외 클래스는 예외 파라미터의 유형을 나타내는 조합의 대안입니다.



compile-time 중 에러 체킹이기 때문에 아래와 같은 분석을 수행합니다.

### 2-1. Exception Analysis of Expression

* 표현식의 예외 분석

### 2-2. Exception Analysis of Statements

* 문장의 예외 분석

### 2-3. Exception Checking

* method나 constructor의 바디가 몇몇의 exception class E를 던질 수 있다면 컴파일타임에러가 난다. 

  * 이때 E는 checked exception이고,
  * 선언된 몇몇 클래스의 서브클래스가 아니면, 
  * 어디에 선언된 서브클래스? 메서드나 constructor의 throws clause에.

  다시 말해서, throw절에 E타입을 던지도록 선언하지 않았으면서 메서드나 생성자가 E타입을 던질 수 있다고 하면 컴파일 타임 에러가 난다고.

* 람다 표현식도 위와 마찬가지
* 명명된 클래스나 인터페이스의  variable initializer나 static initializer가 checked exception class를 던진 경우.
* instantvariable initializer도 동일.
* 명명된 클래스에선 exception에 대해 적절한 정보를 전파해야할 책임이 있다. 익명 클래스에 관해선 java-compiler가 알아서 처리해줌.
* try block에서 throw절에서 던진 예외를 catch block에서 잡을 수 없다면 컴파일 타임 에러 발생



코드 예제

```java
class StaticallyThrownExceptionsIncludeSubtypes {
    public static void main(String[] args) {
        try {
            throw new FileNotFoundException();
        } catch (IOException ioe) {
            // "catch IOException" catches IOException
            // and any subtype.
        }
        try {
            throw new FileNotFoundException();
            // Statement "can throw" FileNotFoundException.
            // It is not the case that statement "can throw"
            // a subtype or supertype of FileNotFoundException.
        } catch (FileNotFoundException fnfe) {
            // ... Handle exception ...
        } catch (IOException ioe) {
            // Legal, but compilers are encouraged to give
            // warnings as of Java SE 7, because all subtypes of
            // IOException that the try block "can throw" have
            // already been caught by the prior catch clause.
        }
        try {
            m();
            // m's declaration says "throws IOException", so
            // m "can throw" IOException. It is not the case
            // that m "can throw" a subtype or supertype of
            // IOException (e.g. Exception).
        } catch (FileNotFoundException fnfe) {
            // Legal, because the dynamic type of the exception
            // might be FileNotFoundException.
        } catch (IOException ioe) {
            // Legal, because the dynamic type of the exception
            // might be a different subtype of IOException.
        } catch (Throwable t) {
            // Can always catch Throwable.
        }
    }

    static void m() throws IOException {
        throw new FileNotFoundException();
    }
}
```



### 3. Run-Time Handling of an Exception

* exception이 던져질 때 제어(control)는 exception을 발생한 code로부터 동적으로 가까운 try statement의 잡을 수 있는 catch절로 이동한다.



* statement나 expression은 동적으로 catch 절에 의해 eclosed된다.
  * 만약에 statement나 expression이 try satement의 try블록에 나타나거나,
  * statement나 Expression의 caller가 catch절에 의해 enclosed된 경우에.



* statement나 expression의 caller는 그것이 어디에서 발생하느냐에 달려있다.
  * 메서드 내에서는 caller는 메서드 호출 표현이다.
  * constructor나 instance initializer 또는 instance variable을 위한 initializer에 한해서 caller는 class instance creation expression이나 object를 생성하도록 하는 newInstance method 호출자이다.
  * static initializer나 static variable initializer에 한해서 caller는 class나 interface를 초기화하도록 하는 expression



* 특정한 catch 절이 exception을 처리할 수 있는지 여부는 catch 절의 catch 가능한 exception class에 던져진 object의 클래스를 비교함으로써 결정한다. catch class는 catch가능한 exception class가 exception의 class이거나 exception의 super class일 경우에 가능하다.



* exception이 던져질 때 발생한 control transfer은 예외를 처리할 수 있는 catch class를 만날 때까지 expression이나 statement의 불완전 종료를 야기한다.

  처리할 수 있는 catch절을 만났다면 catch블록을 실행함으로써 실행은 계속된다.

  exception을 발생시킨 코드는 절때 다시 한 번 실행되지 않습니다.



* 모든 exception(synchronous and asynchronous)은 정확합니다. 제어의 전이가 발생할 경우, exception이 던져진 지점 전의 statements가 실행되거나 expression이 평가된 모든 영향은 반드시 일어난 것으로 봅니다. 에러가 발생한 이후의 expression, statements는 처리되지 않습니다.

* catch절이 처리할 수 있는 exception이 발견되지 않을 경우,  현재 쓰레드는 terminated됩니다. (프로세스 상태도의 terminated 떠올리면 될 듯하네요.) termination되기 전에 모든 finally 절이 실행되고, 잡히지 않은 exception은 아래의 절차에 따라 처리됩니다.
  * 만약에 현재 쓰레드가 uncaught exception handler set을 가지고 있다면 handler가 실행됩니다.
  * 그렇지 않으면 현재 쓰레드의 부모인 ThreadGroup의 uncaughtException method가 호출됩니다. 만약에 ThreadGroup과 이것의 부모인 ThreadGroups가 uncaughtException을 오버라이드하지 않으면 default handler의 uncaughtException 메서드가 호출됩니다.



#### try-catch-finally statement 설명

* code가 불완전 종료(abruptly complete)됬음에도 특정코드가 실행되길 원한다면 finally 절을 사용하세요
* try-finally or try-catch-finally statement의 try나 catch 절이 불완전 종료했다면, exception에 맞는 catch절이 없어도 exception이 전파되는동안 finallly clause이 실행됩니다.
* finally절은 try block의 불완전 종료하거나 finally절이 스스로 불완전 종료했을 때 실행됩니다. finally절이 불완전 종료했을 경우엔 try block의 불완전 종료 사유가 버려지고(discard) finally절에 의한 새로운 이유가 전파됩니다.

```java
class TestException extends Exception {
    TestException() { super(); }
    TestException(String s) { super(s); }
}
class Test {
    public static void main(String[] args) {
        for (String arg : args) {
            try {
                thrower(arg);
                System.out.println("Test \"" + arg +
                        "\" didn't throw an exception");
            } catch (Exception e) {
                System.out.println("Test \"" + arg +
                        "\" threw a " + e.getClass() +
                        "\n with message: " +
                        e.getMessage());
            }
        }
    }
    static int thrower(String s) throws TestException {
        try {
            if (s.equals("divide")) {
                int i = 0;
                return i/i;
            }
            if (s.equals("null")) {
                s = null;
                return s.length();
            }
            if (s.equals("test")) {
                throw new TestException("Test message");
            }
            return 0;
        } finally {
            System.out.println("[thrower(\"" + s + "\") done]");
        }
    }
}
```



input

```
divide null not test
```



output

```java
[thrower("divide") done]
Test "divide" threw a class java.lang.ArithmeticException
 with message: / by zero
[thrower("null") done]
Test "null" threw a class java.lang.NullPointerException
 with message: null
[thrower("not") done]
Test "not" didn't throw an exception
[thrower("test") done]
Test "test" threw a class TestException
 with message: Test message
```