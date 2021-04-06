# Favor static member classes over nonstatic

이번 Item에선 nested class가 무엇인지, 종류와 사용법에 대해 알아봅니다.



### nested class란?

다른 클래스 안에 정의된 클래스



**자신을 감싼 class에서만 쓰여야 합니다.** 그 외라면 TopLevel class로 두어야 하죠.

> static class도 그래야 하는가?



### 종류

* static member class

* inner class
  * nonstatic member class
  * anoymous class
  * local class



# 설명

### static member class

#### 성격

다른 클래스 안에서 선언되고, private로 선언된 enclosing class의 멤버에도 접근할 수 있습니다. 이점을 제외하고는 일반 class와 동일하죠.



#### 접근 규칙

다른 static member와 동일하게 적용

만약 private로 선언된다면 enclosing class에 의해서만 접근 가능



#### 사용 예

* outer class와 함께 쓰일 때만 유용한 public helper class로 활용

ex:) Calculator class의 Operation enum



#### + private static member class

##### 성격

enclosing class의 component를 나타낼 때 사용

##### 사용예

Map 내 Entry

Entry의 method들은 Map의 인스턴스를 접근할 필요없으므로 private로 선언



### nonstatic member class

#### 성격

* 문법상으로는 static 유무의 차이지만 의미상 차이는 큼.

* nonstatic member class의 인스턴스는 outer class의 인스턴스와 implicit하게 연결됨.
  * 이로인해 nonstatic class의 instance method에서 ***클래스명.this***형태로 outer class의 instance method를 호출할 수 있음(***클래스명.this*** 는 qualified this라 부름(이 책에선 정규화된 this로 번역)
  * 메모리를 더 차지하고 오래걸림



#### 연결 관계 정해지는 시기

* 일반적으로는 member class가 instance화 될 때 정해짐

  방법1. enclose class의 instance가 method를 호출할 때 그 메서드 안에서 생성될 때 관계 형성

  방법2. 드물게 enclosingInstance.new MemberClass(args)로 형성





#### 사용 예 - Adapter

outer class의 instance가 관련이 덜한 instance로 보여지도록 view로 사용할 때

* Map interface의 KeySet, entrySet, values가 반환하는 컬렉션 뷰

* 다른 컬렉션 인터페이스 구현들에서 자신의 반복자를 구현할 때

  ```java
  public class MySet<E> extends AbstractSet<E> {
    
    
    @Override public Iterator<E> iterator() {
      return new MyIterator();
    }
    
    private class MyIterator implements Iterator<E> {
      
    }
  }
  ```

  



#### static vs nonstatic

* member class가 enclosing class의 instance를 참조해야 한다면 nonstatic, 아니면 static



이유: 연결관계 때문에 enclosing instance가 garbage collected하지 않을 수 있음



### anonymous class

#### 성격

* 이름 없음
* enclosing class의 Member는 아니고, 다른 member에서 선언되며 동시에 인스턴스화됨
* 표현만 유효하다면 어디서든 사용 가능

* nonstatic으로 선언될 때만 enclosing class 인스턴스 참조 가능
* static맥락에서 static constant외 static member 가지지 못함
  * static constant란 final primitive or final string을 의미



#### 사용 예

##### 제약

1. 선언 시점에만 instance만들 수 있음
2. instanceof 검사 및 클래스 이름이 필요한 작업 수행 불가
3. 여러 인터페이스 구현 불가
4. 인터페이스 구현하면서 상속 불가
5. 익명 클래스가 supertype에서 상속한 member제외 호출 불가
6. expression 중간에 위치하므로 짧지 않음녀 가독성 떨어짐



##### 사용

1. 보통 작은 함수 객체(small function object)나 처리 객체(process object) 만드는데 사용 (이제는 람다로 교체)
2. static factory methods 만들 때 사용 (Item20의 intArrayAsList)



### Local class

#### 성격

* 가장 드물게 사용

* 지역 변수 선언할 수 있는 곳 어디든 선언 가능
* 지역 변수와 유효범위 동일
* member class처럼 이름 존재, 
* nonstatic 문맥에서 사용될 때만 outer class instance참조 가능(익명 클래스와 유사)
* static member 못가짐
* 가독성 위해 짧게 작성해야 함

