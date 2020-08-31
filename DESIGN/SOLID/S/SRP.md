# 단일 책임 원칙

### 출처

https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html

### 의문점

> 도대체 reason to change?는 뭘까?



### 사람들이 해석하는 reason to change

1. 버그 픽스?
2. 리팩토링?



### 핵심

reason to change 와 responsibility를 연관 짓는 것.

위 2가지 사항은 프로그래머의 책임

=> **프로그램의 디자인이 누구에게 반응해줘야 하는가?!**





### 예시



#### 1.CEO

CEO에게 보고하는 것은 C-Level결정임 (CFO, COO, CTO)



#### 2.CFO

finance 컨트롤하는 것에 책임



#### 3.COO

회사를 운영하는데 책임



#### 4.CTO

회사의 기술적인 개발에 책임이 있음



[java code]

```java
public class Employee {
  public Money calculatePay();
  public void save();
  public String reportHours();
}
```

변경될 이유는 결국 사람의 의한 것이다!

employee가 calcuatePay를 잘못하면, CFO가 책임을 물을 것이고, save()가 잘못되면 CTO가 잘못될 것이다. 따라서 잘못된 것에 대해 CFO는 해당 기능을 변경하라 지시할 것!

여기서 다른 기능까지 변경되면 안된다. 하나를 변경했을 때 해당 사항만 변경되야 하므로. 다른 것 까지 변경된다면 변경 이유가 다른 것에 의해 다른 기능이 변경되는 꼴.



#### 재정의

Another wording for the Single Responsibility Principle is:

> Gather together the things that change for the same reasons. Separate those things that change for different reasons.

If you think about this you’ll realize that this is just another way to define cohesion and coupling.



응집도

한 모듈 내에 존재하는 함수 데이터 사이의 밀접한 정도(관련성이 얼마나 밀접한지)



결합도

하나의 모듈이 다른 모듈에 의존하는 정도. 각 모듈이 서로 관련성이 적어서 결합도가 낮을 수록 모듈간 독립성이 높아짐.





