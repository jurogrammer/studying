# 출처

* https://en.wikipedia.org/wiki/Lambda_calculus#Notation



# 선행 자료

* https://jurogrammer.tistory.com/131 lambda caclulus Intro
* https://jurogrammer.tistory.com/132 Formal System



# 개요

이번 글에선 lambda calculus를 informal하게 설명하겠습니다. 그쵸.. 처음부터 formal하게 설명하면 머리아픕니다. 맥락을 파악하기 어렵구요. 따라서 formal한 정의와 사칙연산, boolean등으로 simulate하는 것은 다음에 알아보도록 하겠습니다.



lambda caculus를 다시 설명하자면 다음과 같죠.

formal system인데, computation 표현하기 위한 mathmetical logic입니다.

어떤 계산이냐하면,

* function abstraction

  function의 추상화 형태이며

* function application using variable binding and substitution

  variable을 연결하고 치환함으로써 함수에 적용합니다.



formal system이라고 했으니까 여기서 사용하는 **기호(symbol)** 및 **표기법(notation)**이 있을 것이고, 이 기호에 관한 **추론 규칙(또는 연산 operation)**이 있겠지요?

notation 먼저 정리드리겠습니다.



# Notation



### 표기법

formal system을 배우니 무엇이 유효한 표현인지 알아야겠죠? 이 labmda caclulus에서 유효한 표기법이요!

유효한 표기법? 뭔 소리인가 싶을 수 있어요. formal system에 대해 아직 어색하다면요. 제가 그랬거든요 ㅎㅎ;



예를 들어 제가 식 하나를 써볼게요.

```
 ㄱ x 1 = @
```

위화감이 들지 않나요? 곱셈있고, 등식이긴 한데... 수식이라고 하기엔 ㄱ이 뭐고 @이 뭔지 모르잖아요? 

이 위화감은 "수학에 정의된 올바른 표기법을 사용하지 않아서"라고 말할 수 있습니다. 그러니 lambda calculus에서도 유효한 표기법으로 작성을 해야겠지요. 그 유효한 표기를 lambda terms라고 부릅니다.

lambda terms가 어떻게 생겼는지 알아보죠.



### lambda terms

|   Syntax   |    Name     |                         Description                          |
| :--------: | :---------: | :----------------------------------------------------------: |
|    *x*     |  Variable   | A character or string representing a parameter or mathematical/logical value. |
| (λ*x*.*M*) | Abstraction | Function definition (*M* is a lambda term). The variable *x* becomes [bound](https://en.wikipedia.org/wiki/Free_variables_and_bound_variables) in the expression. |
| (*M* *N*)  | Application | Applying a function to an argument. M and N are lambda terms. |

wiki에서 가져온 표인데요, lambda에서 사용하는 notation은 3가지가 전부입니다! 단순하죠? 의미도 우리 직관과 크게 다를게 없습니다.



#### 1. variable 

평소에 말하는 변수를 의미합니다. 그런데 2가지를 의미할 수 있어요. 하나는 parameter이며, 하나는 수학 또는 논리적인 value를 의미한다네요.

parameter와 argument 두 가지 말하는 것 같네요. 

parameter는 함수 내에서 사용되는 변수를 의미할 것이고,

 argument는 보통 함수를 invoke하기 위해 parameter위치에 집어넣는 값을 의미하잖아요. argument를 좀 더 자세히 설명한 것 같습니다.



허용되는 값은 수학적인 또는 논리적인 값이라고 합니다.

수학에서 값은 1,2,3 이런 정수가 있을 것이고, 논리학에서 값은 참, 거짓을 의미하겠네요. 



#### 2. Abstraction

Abstraction은 단순히 함수를 set up한 것입니다. 호출한게 아니에요! 값을 집어넣어서요. 

f(x) = X^2 + 2 와 f(2) = 2^2 + 2의 차이라고 보시면 됩니다. 왼쪽은 함수를 단순히 정의(set up)한 것 이죵.



f(x) = x^2 + 2를 Abstraction 표기법으로 바꿔보겠습니다.

abstraction의 표기법은 (λ*x*.M)형태라고 적혀있죠?

x는 f(x)의 x에 대응하며, M은 x^2 + 2에 대응됩니다. 



(λ*x*.M)표기를 말로 풀어 설명하면 다음과 같죠.

> 함수(λ)인데, x를 집어넣으면 M을 반환(또는 치환, 변환)해줘~

> ![\lambda x.t](https://wikimedia.org/api/rest_v1/media/math/render/svg/6c340da553f36c8832a4a6aff7d235dd2acb760a) is a definition of an anonymous function that is capable of taking a single input x and substituting it into the expression t.



그리고 위처럼 정의해서 좌측 x의 값이 변함에 따라 M의 x가 영향받게 되죠? f(2) = 2^2 + 2 처럼 말이죠. 

서로 다른 별개의 변수일 수도 있는데, 연결 관계를 가지게 된것입니다. 즉, abstraction은 변수 x를 M에 관하여 binding한다고 말할 수 있습니다.

그리고 테이블에 설명된 것처럼 M또한 lambda terms여야 유효한 표현이 됩니다.



#### 3. application

간단히 말해서 function에 Lambda를 집어넣는 것을 의미합니다. 

아까 작성했던 f(x) = x^2 + 2에 2를 대입한 것을 (λ*x*.x^2+2) (2)라고 표현하는거에요.영어로 표현하면 다음과 같습니다.

> **ts** represents the application of a function **t** to an input **s**, that is, it represents the act of calling function **t** on input **s** to produce **t(s)**.



다시 말해서 abstraction처럼 함수를 정의하는 것과 대조적으로 함수를 실행하는 것을 뜻합니다!







### 추가로...

lambda caclulus에선 변수 선언이 없습니다.



λx.x+y라고 표기한다면 y는 아직 정의되지 않았다고 표현할 뿐이죠.

그래서 λx.x+y를 말로 풀어 설명한다면 input인 x를 집어넣으면 x에 아직 알려지지 않은 y를 더한다. 라고 표현할 수 있습니다.  유효한 표기법이라는 겁니다.



> 여기서 좀 신기했네요. 정의되지 않은 변수라... 결과물에 정의되지 않은 변수가 있다면 프로그래밍 언어에선 에러를 던지잖아요? 제가 알고 있는 고등 수학까진 이미 정의된 변수에 대해서 연산만하구요.
>
>
> lambda calculus intro 게시물의 motivation에서 나왔던 것처럼 중간 연산 결과물 때문에 위와 같이 정의했다면, 이해가 되네요 ㅎㅎ x -> y -> x^2+y^2 말이죠.
>
>  여기서 y -> x^2 + y^2만 봤을 때는 x^2은 정의되지 않은 변수잖아요?  그런데 우리 직관적으로는 x -> y-> x^2 + y^2의 연산이 납득되죠. 이런 디테일이 재밌네요 ㅋㅋ



# Operation

formal system에서 symbol, notation을 정의하고 추론 규칙을 만드는 것처럼, lambda caclulus에선 정의한 lambda terms에 대해 Operation이 존재합니다.



|              Operation               |     Name     |                         Description                          |
| :----------------------------------: | :----------: | :----------------------------------------------------------: |
|  (λ*x*.*M*[*x*]) → (λ*y*.*M*[*y*])   | α-conversion | Renaming the bound variables in the expression. Used to avoid [name collisions](https://en.wikipedia.org/wiki/Name_collision). |
| ((λ*x*.*M*) *E*) → (*M*[*x* := *E*]) | β-reduction  | Replacing the bound variables with the argument expression in the body of the abstraction. |

와... 여기 2개가 전부입니다. 다 우리 직관과 별반 다를게 없는 말이죠. 표현 자체는 되게 어려워 보이는데 간단합니다. 차근차근 알아보죠.



### 1. α-conversion

좌측에서 Operation column에서 보이는 바와 같이 단순히 변수 명만 바꿔주는 거에요. 의미는 동일하나 symbol만 교체 한다고 말할 수 있죠.

f(x) = x^2 + 2로 표기하나 f(t) = t^2 + 2로 표기하나 **함수의 동작방식**면에선 차이가 없잖아요? 애당초 lambda calculus가 익명 함수로 불릴 수 있었던 이유는 함수의 동작방식에 집중하는 거였으니까요.

이 Operation을 정의한 이유는 이름 충돌(name collision)을 피하기 위해서 입니다. 

λx.x^2+2의 x와 λx.x+2의 x는 서로 다른 x인데, operation할 때 헷갈릴 수 있잖아요. 그러니깐 이런 operation을 정의한 겁니다. 



우리는 직관적으로 "어? 다른 x니까 다른 변수로 놔야징~" 라고 말할 수 있는 것을 

"name collision을 피하기 위해 다른 변수로 치환하고, 이를 α-conversion이라 부른다!!"

라고 엄밀하게, 수학적으로 표현해서 정의한거죠.



그리고 bound variable은 abstraction labmda terms에서 봤듯이 변수 x가 M에 관해서 binding되었다라고 표현했잖아요? 그 변수를 의미합니다.



### 2. β-reduction

오... 요상한 기호가 있어요 x:= E 라고요. 이름도 뭔가 간지고요. 베타 리덕션이라고.  사실 뭐 별거 없습니다... 

f(x) = x^2 + 2 함수에서 2를 대입한 식 f(2) = 2^2 + 2 요거.

이게 바로 β-reduction입니다.

x가 x^2 + 2에 관해서 binding되어 있고, 여기에 x^2 + 2(abstraction of body라고 표현)에서 x대신 숫자 2 (argument Expression이라고 표현)를 치환했잖아요?

((λ*x*.*M*) *E*)이렇게 적으면, (*M*[*x* := *E*])로 됩니다. 즉 M에 E를 대입한 것입니다~라는거에요~  



그리고 추가적으로 알아야할 내용에 대해 적어보겠습니다. 총 5가지로 볼 수 있어요. 



#### Free variables

λx.x^2+2라고 표현한다면, x는 x^2 + 2에 관해 binding됬다고 표현했잖아요? 묶여 있는거죠! 이와 반대로 자유로운 변수가 있다는 겁니다! 눈치 빠르시다면 아까 정의되지 않은 변수와 관련되있구나! 알거에요

free variables은 다음처럼 정의할 수 있어요. (inductively하게 정의합니다.)

1. lambda terms인 variable x만 본다면, x 그 자체가 free variable 입니다.
2. λx.t의 free variable **집합**은! t의 free variables 집합인데, x는 제외합니다.
3. ts의 free variable 집합은! t의 free variable 집합과 s의 free variable 집합의 합집합입니다.



λx.x 요놈을 예로 들어볼게요.

1. λx.x에서 우측 x는 1번에 의해 free variable이라고 할 수 있죠? 
2. 그 다음의 lambda terms인 λx.x를 봅시다. 2번을 적용한다면 t에 해당하는 x의 free variable은 x입니다. 그리고 좌측 람다 옆의 변수 x를 제외해야겠지요? 따라서 {x} - {x} 해서 free variable은 없다! 라고 말할 수 있습니다.



λx.yx는 어떨까요?!

직관적으로 y입니다! 라고 하겠지만 우린 엄밀하게 접근해야죠. 앞서 정의한 free variable의 3가지 케이스요

간단히 논리 순서대로 말하자면



1(y에 관해) -> 1(x에 관해)-> 3(xy에 관해) -> 2 (λx.yx에 관해)

로 y라고 말할 수 있겠습니다~



#### Capture-avoiding substitutions

α-conversion과 관련있어요. capturing은 binding과 비슷한 의미이구요. 

"서로 다른 의미가 동일한 의미로 capturing되는 것을 피하기 위해 치환한다."

라고 말할 수 있습니다. 

fresh와 관련해서 수식들이 있긴한데... formal하게 정의할 때 말씀드리도록 하겠습니다.



#### brancket사용(소괄호)

애매함을 제거하기 위해 사용합니다. 두 가지 이상의 의미를 가질 수 있는 수식을 제거하기 위해서죠. 평소 알고 있는 수학에서처럼 소괄호는 연산 우선순위를 가집니다.



#### functions that operate on functions

lambda calculus에서 함수는 first class values로 취급됩니다. 따라서 function이 input이 될수도, output이 될수도 있죠.



앞서 정의한 lambda terms와 Operation 관점에서, 

1. Operation은 lambda terms이기만 하면 연산할 수 있다고 했잖아요? 
2. 그런데 lambda terms엔 abstraction인 함수도 포함되죠~
3. 따라서 값 뿐만이 아니라 함수에 관해서 연산이 가능하네~

라고 말할 수 있습니다.



# 정리

막상 다 적어보니깐 우리가 일고 있는 함수 연산이랑 크게 다를 바 없죠? 알고 있는 수학에서 함수를 좀 더 간단화하고 연산을 정의했다고 볼 수 있겠습니다.



도입부에서 lambda calculus정의가 잘 와닿지 않았을 수 있으니 다시 한 번 가져와보겠습니다. 이젠 아~~ 이게 이뜻이였고만!!! 할 겁니다.



formal system인데, computation 표현하기 위한 mathmetical logic입니다.

어떤 계산이냐하면,

* function abstraction

  function의 추상화 형태이며

* function application using variable binding and substitution

  variable을 연결하고 치환함으로써 함수에 적용합니다.



어떤 계산인지 2개가 와닿지 않으신가요? function abstraction은 람다 자체를 의미하고 그 표현은 lambda terms의 abstraction에서 배웠죠.

그리고 Function application은 lambda terms 세번째 application과 Operation에서 β-reduction을 의미하겠네요 ㅎㅎ 굳~



다음엔 formal한 정의에 대해 알아보고 그 다음엔 사칙 연산 같은 것들이 어떻게 simultate되는지 알아보도록 하겠습니다~