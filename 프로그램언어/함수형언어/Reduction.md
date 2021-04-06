# 출처

* https://en.wikipedia.org/wiki/Lambda_calculus

  

# Reduction

reduction의 사전적 정의는 다음과 같습니다.

> the action or fact of making a specified thing smaller or less in amount, degree, or size.

번역하자면 특정한 것의 양, 차원, 사이즈를 줄이는 행위 또는 사실이라고 말할 수 있습니다.



# meaning

wiki에서 reduction의 도입부에 다음과 같이 말합니다.

> The meaning of lambda expression is defined by how expressions can be reduced

lambda calculus의 의미는 expression이 얼마나 축소되는지에 따라 달려있다니... 이해가 잘 안됩니다. 그래서 해당 문장의 출처가 되는 제목은 다음과 같습니다.

>  "A Proof-Theoretic Account of Programming and the Role of Reduction Rules". 

​	흠... Reduction rule과 증명이라는 것을 보니, reduction rule으로 abstraction이 동치인가? 판단할 수 있다. 라고 할 수 있는 것 같아요.

수학에서 1 + 1 + 1 = 1 x 3 = 3     인 것 처럼요.

그리고 lambda calculus에서 축소의 의미를 살려서, lambda가 줄어드는 연산이라고 보시면 됩니다.



# reduction의 종류

reduction 종류는 총 3가지가 있습니다.  α-conversion, β-reduction, η-reduction이 존재합니다. 차례대로 설명드리겠습니다.



### 1. α-conversion

#### 정의

α-renaming이라고도 불리는데, bound variable의 이름을 바꾸도록 하는 연산을 의미합니다.



#### 예시

 λ*x*.*x* 에서 bound variable인 x를 y로 치환한다면 λ*y*.*y* 라고 표현할 수 있죠.



#### 유의사항

##### 1) 용어 혼동

a-equivalent랑은 완전 다른 의미입니다. 이것은 동등성을 말할 때 쓰이는 용어이죠.

##### 2)정확한 룰 적용(bound variable)

abstraction에 의해 Binding된 variable의 이름만을 재정의할 수 있죠.

이전에 설명드린 free and bound variables 설명 중 하나를 발췌했습니다.

> a variable is bound by its nearest abstraction.

ex:) λ*x*.*y* (λ*x*.*z x*)

이 예제에서는 두번 째 람다에 의해 맨 오른쪽 x가 binding되죠.

λ*x*.*z **x*** 이 x가  ***λ*****x**.*z* *x* 여기 굵게 쓰여진 λx에 의해 binding 된다는 것이죠.



따라서 λ*x*.λ*x*.*x* => λ*y*.λ*x*.*x* 은 옳으나,

λ*x*.λ*x*.*x*  => λ*y*.λ*x*.*y* 은 틀린 말이 됩니다. 이것은 variable shadowing이라고 부르기도 합니다.

> 애당초 변수 명을 헷갈리게 쓰긴 했네요;



#### substitution

위처럼 변수명 변경하는 표현을 substitution으로 따로 정의하는 것 같습니다.

##### 정의

> written *M*[*V* := *N*], is the process of replacing all *free* occurrences of the variable *V* in the expression *M* with expression *N*.

M에서 나타나는 모든 자유 변수 V를 N으로 바꾼다는 의미입니다.



##### 귀납적 정의

이를 귀납적으로 정의할 수 있습니다.  여기서 x,y는 variables, M,N는 임의의 lambda expression이라 보시면 됩니다.

1. *x*[*x* := *N*] = *N*

   변수 x에서 x대신 N으로  치환한다! 간단하죵?

2. *y*[*x* := *N*] = *y*, if *x* ≠ *y*

3. (*M*1 *M*2)[*x* := *N*] = (*M*1[*x* := *N*]) (*M*2[*x* := *N*])

4. (λ*x*.*M*)[*x* := *N*] = λ*x*.*M*

   이건 M이 x에 의해 binding되어 있는 abstraction에서 x대신 N을 대입해줘봤자 의미없다는 거죠. **자유 변수를 치환**해주는 작업이니까요.

5. (λ*y*.*M*)[*x* := *N*] = λ*y*.(*M*[*x* := *N*]), if *x* ≠ *y* and *y* ∉ FV(*N*)

   4번이랑 비교하면 바로 이해하실거에요. M에서 x는 자유변수가 될 수 있기 때문에 x대신 N으로 치환해줄 수 있다는 뜻 입니다.

   

### 2. β-reduction

이전에 설명드린대로, 함수의 적용이라고 보시면 됩니다. f(x) = x*2 이라 한다면 f(2) = 2^2 이라고 쓰는 것이요.

β-reduction은 substitution의 용어 아래에 정의될 수 있습니다.



#### 정의

the β-reduction of (λ*V*.*M*) *N* is *M*[*V* := *N*].

V에 N을 집어넣는다면, M에 있는 V는 N으로 치환된다! 간단하쥬? 

여기서 β-reduction에 의해 λV는 사라져서 *M*[*V* := *N*]로 되었습니다. 그래서 reduction이라고 표현하는 것 같습니다.



> 한편으로, 영어로 N에 대해 λ*V*.*M* 을 적용한다라고 표현하더라구요. ㄸ; 생각해보면 맞는 말이네여...
>
> function f가 2를 2^2으로 변환시키니까요 ㄸ; function을 갖다쓰는 느낌에선 apply 표현이 절묘하네요



### 3. η-reduction

이전 informal 설명에서 안나왔던 내용이긴 합니다. 

#### Concept

이 개념의 컨셉은 extensionality에 기초한대요.

extensionality or extensional eqaulity라고 불리는 이 용어는 논리학에서 나오는 말입니다. 좀 읽어보면 외부 속성이 동등할 경우 동등하다! 라고 말할 수 있다는 것 같아요.

예를 들어 A, B 물체의 본질이 뭔진 모르겠어요. 하지만 외적으로는 동일해보여요! 빨간색으로 보이고 둥글고, 흔들면 청명한 소리나고... 그러면 A,B가 extensional equality하다. 라고 말하는 것 같습니다.



#### reduction과 연관

지금 reduction 설명하고 있잖아요? 어떻게 람다 연산이 축소되는지 보겠습니다.

λ*x*.*f* *x* 와 *f* 를 비교해봅시다.

λ*x*.*f* *x* 의 *f* 에 free variable x가 나타나지만 않는다면, *f* 엔 x가 없는 꼴이니까 *f* 라고만 표현할 수 있겠죠? 

f(x) = 4라고 하면 x에 뭘 집어넣든 4가 나오잖아요? 그런 이치입니다.  

따라서 λ*x*.*f* *x* 는  η-reduction에 의해 *f* 로 변환될 수 있습니다. abstraction에서 variable로 축소되었네요 ㅎ





# 끝으로,

이번 장에서는 좀더 formal하게 연산을 정의해보았습니다. reduction의 종류를 나누고, substitution을 수학적으로 표현하기도 했죠. 

드디어 기초적인 내용은 다 배웠습니다!

다음으로는 아주~~ 간단히만 lambda calculus로 어떻게 자연수를 표현할 수 있는지, 그리고 사칙연산을 할 수 있는지를 말씀드리겠습니다.

내용을 읽어보니 프로그래밍이랑 큰 관련없는 것들이 있어서 걸러야할 것 같습니다. 어차피 컴퓨터는 1,2,3,4과 같은 자연수로 표현하니까요.

자주 쓰이는 연산들을 알아볼 예정입니다. 위키보다는 https://www.youtube.com/watch?v=3VQ382QG-y4 이 동영상을 좀 더 참고할 것 같네요. 

