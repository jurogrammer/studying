# Consider implementing Comparable



# 개요

이번 내용은 Object 클래스에 있는 메서드가 아닌 Comparable interface에 있는 compareTo method에 소개시켜드리겠습니다.

equals 메서드와 매우 유사하나 동등성 뿐만 아니라 순서 비교를 할 수 있고, 제너릭합니다.



Comparable를 구현한다면, 해당 클래스는 자연 순서(natural ordering)을 가지고 있다고 볼 수 있습니다. 따라서

```java
Arrays.sort(a);
```

와 같은 메서드도 실행할 수 있게 됩니다.

이점들을 정리하면 다음과 같습니다.

1. 검색
2. 극단값 계산
3. 자동 정렬되는 collection 관리 (ex: Treeset)



이러한 이점으로 인해 대부분의 java library와 enum은 Comparable을 구현하였습니다. 자그마한 노력으로 큰 이점을 얻을 수 있기 때문에 value class를 작성한다면 고려하는 것이 좋습니다.



# contract

equals와 매우 유사합니다.

https://docs.oracle.com/javase/8/docs/api/java/lang/Comparable.html#compareTo-T-

규약은 위를 보시면 자세히 나와있습니다.

위 규약을 지키면 다음과 같은 클래스를 사용할 수 있습니다.

1. 비교를 활용하는 클래스

​	TreeSet, TreeMap

2. 검색과 정렬 알고리즘을 활용하는 유틸리티 클래스

   Collections, Arrays

를 사용할 수 있게 됩니다.



### 유의 사항

1. equals는 모든 객체에 대해 반드시 동등하도록 강제하였으나, compareTo는 강제하지 않습니다.
   * ClassCastException을 던지도록 하거나
   * 다른 타입의 비교도 허용한다. (일반적으로 공통 인터페이스를 매개로 비교한다.)

2. equals와 동일하게 반사성, 대칭성, 추이성을 충족해야 합니다.

3. 마지막 규약은 `(x.compareTo(y)== 0) == (x.equals(y))`여야 한다. 인데, 이를 지킨다면 compareTo 메서드로 줄지은 순서와 equals의 결과가 일치하게 됩니다. 이를 어긴다면 equals을 이용하는 Collection, Set, Map과는 엇박자나게 됩니다. 

   ex:) new BigDecimal("1.00")와 new BigDecimal("1.0")은 HashSet에선 두 개의 key가 생성되지만, TreeSet을 사용하면 1개가 저장됩니다.



# 작성요령

### 1. 제너릭 인터페이스

1) 제너릭 타입을 받아 반환하므로 타입이 컴파일 타임에 결정된다. 따라서 캐스팅할 필요가 없게 됩니다.

2) 타입이 잘못됬다면 컴파일 타임에 체크됨.

3) null을 받는다면 NullpointException을 던지게 함. 안한다해도 실행 중 발생

### 

### 2. comapreTo를 구현하지 않은 필드나 표준이 아니라면 Comparator를 사용하여 비교

Compareable을 구현하지 않은 필드 또는 표준이 아닌 필드라면 Comparator를 대신사용 하여 비교합니다.

comparator는 직접사용하거나 자바가 제공하는 것중 하나를 사용하면 됩니다.

```java
public final class CaseInsensitiveString implements Comparable<CaseInsensitiveString>{
  public int compareTo(CaseInsensitiveString cis) {
    return String.CASE_INSENSITIVE_ORDER.compare(s, cis.s);
  }
}
```

위 예제는 java에서 제고아는 comparator를 이용해서 comapreTo를 구현한 예제입니다.



한편으로, 주목할 부분은 비교하는 타입입니다.

앞서 말씀드렸듯이, 일반적으로는 동일한 타입과 비교를 수행합니다.





### 3. 필드가 여러개라면 핵심필드부터 비교

```java
public int compareTo(PhoneNumber pn) {
  int result = Short.compare(areaCode, pn.areaCode);
  if (result == 0) {
    result = Short.compare(prefix, pn.prefix);
    if (result == 0)
      result = Short.compare(lineNum, pn.lineNum);
  }
}
```

핵심인 지역 코드 먼저 비교한다음에 다르다면 곧바로 종료시키도록 합니다. 이렇게 함으로써 performance를 증대시킬 수 있죠.

한편으로 위 코드는 보기 불편합니다. 따라서 java는 comparator construction methods를 제공합니다.

# Comparator Construction methods

(비교자 생성 메서드)

```java
private static final Comparator<PhoneNumber> COMPARATOR =
  comparingInt((PhoneNumber pn) -> pn.areaCode)
  	.thenComparingInt(pn -> pn.prefix)
 		.thenComparingInt(pn -> pn.lineNum);

public int compareTo(PhoneNumber pn) {
  return COMPARATOR.compare(this, pn);
}
```



### 이점

1. 가독성이 좋습니다.
2. COMPARTOR를 static 필드로 선언 해준다면 사용하기도 편합니다.



### 단점

1. 속도가 느려집니다. (저자 테스트 기준 약 10%정도)



### 작동방식

##### 1. 첫번째 비교

![](https://postfiles.pstatic.net/MjAyMDEyMDFfMTcx/MDAxNjA2NzgzNDMxMzQy.y4XxrTD455nXrT_7acgkWzlAH9PXRE5HwsZst1pG2Dsg.1OJtsEj6uLKJ6S2xoTfFFUA1wb_25IbZ4VjiMndINgog.PNG.study_ju/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2020-12-01_%EC%98%A4%EC%A0%84_9.33.20.png?type=w966)



![](https://postfiles.pstatic.net/MjAyMDEyMDFfNzYg/MDAxNjA2NzgzNDMxMzM5.KTbG41IAKOoIFj9rK4Gk_aWoGFkZBMpnjseaxkLceQkg.Gk-PyI85Te8a6PqgxgYBJ3JoJjvJ4bvFdJw3utwTb-sg.PNG.study_ju/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2020-12-01_%EC%98%A4%EC%A0%84_9.33.01.png?type=w966)

##### 2. 두번째 이후의 비교

![](https://postfiles.pstatic.net/MjAyMDEyMDFfODUg/MDAxNjA2NzgzNDMxMzQz.fhmfVD4RTsD4diKVHSC19dTqY3q27qjJg7d-Wycb-BQg.Be9OjShb9r6slZ-skYc3Jo5-eTyhQkkIvkx6e8nfudwg.PNG.study_ju/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2020-12-01_%EC%98%A4%EC%A0%84_9.41.48.png?type=w966)



![](https://postfiles.pstatic.net/MjAyMDEyMDFfMjEx/MDAxNjA2NzgzNDMxMzQ0.CTUfSKlFMw2759QWOzJ1y1juom8WmzlCxXbfc-MmRK0g.A5n0Pgz_xwJWP6QrTGQChz0d6HPqBbbebX7V9K5izd4g.PNG.study_ju/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2020-12-01_%EC%98%A4%EC%A0%84_9.41.22.png?type=w966)

### 보조 생성 메서드들

#### 숫자용 primitive type 메서드

1. long과 double비교를 위한 메서드 (comapreToLong, compareToDouble)
2. short는 int버전 이용
3. float는 double버전 이용



#### 객체 참조용 비교자 생성 메서드

##### comparing overloadding

1. 키추출자 받아서 그 키의 자연적 순서 비교
2. 키 추출자 하나와 추출된 키를 비교할 비교자 (2개 인수 받음)



##### thenComparing overloadding

1. 비교자 하나만 받아서 그 비교자로 부차 순서 정함
2. 키 추출자를 인수로 받아 그 키의 자연적 순서로 보조 순서 정함
3. 키추출자 하나와 추출된 키를 비교할 비교자까지 총 2개인수 받음



### 구현시 주의사항

```java
static Comparator<Object> hashCodeOrder = new Comparator<>() {
  public int compare(Object o1, Object o2) {
    return o1.hashCode() - o2.hashCode();
  }
}
```

값의 차를 비교하는 방식을 사용하면 안됩니다.

오버 플로우를 일으키거나 IEE754에 따른 오류를 낼 수 있습니다.



대신 아래의 두 방식을 사용하도록 합시다.

#### 1. static compare method 활용

```java
static Comparator<Object> hashCodeOrder = new Comparator<>() {
  public int compare(Object o1, Object o2) {
    return Integer.compare(o1.hashCode(), o2.hashCode());
  }
}
```



#### 2. comparator constructor method 활용 방식

```java
static Comparator<Object> hashCodeOrder = 
  Comparator.comparingInt( o -> o.hashCode());
```

