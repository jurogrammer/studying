# 출처

* https://en.wikipedia.org/wiki/Lambda_calculus
* A Tutorial Introduction to the Lambda Calculus [2015 Ra´ul Rojas]
* https://www.youtube.com/watch?v=3VQ382QG-y4&t=2554s



# 개요

### 출처

Functional programming의 핵심 개념인 lambda caclulus에 대해 말씀드리겠습니다.  출처는 총 3개를 인용했습니다. 

wiki가 이런 개념은 잘 설명해주기 때문에 위키를 우선으로 봤고, 

그리고 부족한 개념을 보충하기 위해 2015년에 lambda calculus의 간단히 정리한 논문인 [A Tutorial Introduction to the Lambda Calculus]를 참고했습니다. 인용수가 58로 괜찮아서 참조했습니다. 

마지막으로 유튜브를 참조했습니다. 이 유튜브 영상은 꽤나 인상깊었습니다. 자칫 이론으로 설명하고 넘어갈 수 있는 lambda calculus내용을 javascript으로 잘 연결시켜 주었거든요.



### 다룰 내용

이번 장은 lambda calculus의 정의, 어원, 동기로 설명드리겠습니다. 본격적인 내용도 다루고 싶었으나, 잘 설명드리기에는 이해도가 좀 떨어지는 것 같습니다. 따라서 다음에 설명드리기로 하겠습니다. 



### 정의

> ko wiki: 추상화와 함수 적용 등의 논리 연산을 다루는 형식체계이다.
>
> eng wiki: a formal system in mathematical logic for expressing computation based on function abstraction and application using variable binding and substitution. 

영어 정의가 좀 더 자세히 다뤄주네요. 변수를 binding하고 치환을 통해 및 함수의 추상화와 적용 계산을 표현해주는 수학적인 논리에서의 formal system이라고 합니다. 좀 더 간단히 말해서 함수의 연산을 표현해주는 논리 규칙이라고 보시면 됩니다.



lambda calculus용어를 한글로는 람다 대수나, 람다 계산, 람다 계산법이라고 부릅니다. 여기서 λ는 함수를 추상화한 용어(notation)이라 보시면 됩니다. 1930년도에 Alonzo Church란 사람이 소개하였죠.



### 람다 어원

어떤 프로그래밍언어에서 람다 function, 람다 expression이란 용어를 처음 접했을 때 어려웠는데요... 그 이유는 람다가 어떤 의미를 가졌길래 람다라고 지었나 궁금했기 때문입니다.

wiki를 참조해보면... 뭐 별 시덥잖은 이유였습니다. 별 의미없이 붙였다 보시면 됩니다...ㅜ

class-abstraction에서 ![{\hat {x}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/18d95a7845e4e16ffb7e18ab37a208d0ab18e0e0) 이란 notation을 쓰는데 function-abstraction와 구별하기 위해 ^x로 쓰다가 추후 프린팅하기 쉽도록 λ로 변경되었다 하네요. 

나중에 다른 사람이 또 다시 church에게 물어봤는데 function-abstraction을 표현하기 위해 notation이 필요한데 λ가 떠올라서 명명했다고 합니다.

그래서 "λ는 function abstraction을 나타내는구나~~" 하고 넘어가시면 됩니다.



### labmda calculus와 programming

lambda calculus가 어떻게 프로그래밍에 적용될 수 있을까요?? 어떻게 알론소 처치가 만든 함수 연산체계가 프로그래밍에 쓰게 될 수 있을까요?

그건 튜링완전성을 만족시켰기 때문이랍니다. 튜링 완전성을 증명시키면 프로그래밍에서 쓰이는 연산들을 다 구현할 수 있다고 보나봐요. (튜링 완전성은 나중에 따로 소개시켜드리겠습니다.)

이는 다시 말해서 함수로 not연산, or연산 등을 다 표현할 수 있다고 말하는 것이랑 같습니다. 즉, 평소에 우리가 작성한 코드들을 lambda calculus로 표현가능한 것이죠. 와우~!



# Motivation

도입 동기는 2가지로 보시면 됩니다. 함수의 이름과 input parameter를 좀 더 간단히 해보자!로 시작됩니다.

1. 이름 간단하게 하기

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/6020e0858d923aa15ab308584dac8af2d003b879)

square_sum이란 함수가 있어요. 이 함수는 x,y input parameter를 받아서 x^2 + y^2으로 출력해주는 함수이지요.

그런데 이 함수에 square_sum이란 함수를 붙이지 않고 간단히 만들어 줄 수 있지 않을까요? 다시 말해서 함수를 이름으로 나타내주는 것이 아니라 행동방식 그 자체로 표현해주는 것이지요.

이처럼 말입니다.

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/89bf7c479bc1935d1ddd0519cde149591d0e541b)

> x,y를 넣으면(->)  x^2 + y^2이 출력된다

매우 직관적으로 표시할 수 있죠. 굳이 이름 없이 함수를 그 작동방식으로만 표현한 것입니다. 이러한 면 때문에 람다 함수가 익명 함수라고도 불리는 것 같네요.
현실과 비유를 들면 이와 같을 것 같네요.



<img src="http://img2.tmon.kr/cdn3/deals/2019/11/05/2667388858/2667388858_front_3c2cf058ae.jpg" style="zoom: 25%;" />

이거 보고 거울이라고 말할게 아니라 "빛을 반사시켜주는 도구"라고 말하는 거지요.



2. parameter 간단하게 하기

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/89bf7c479bc1935d1ddd0519cde149591d0e541b)

이 예시를 보면 파라미터 x,y 2개를 받아서 x^2 + y^2 을 출력한다고 나와있죠? 그런데 파라미터를 1개만 받는 함수들로 표현하고 싶은 거에요. 그래서 이는 다음처럼 표현이 됩니다.

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/012fc8f19ed14bf232ee8deefe4ae84dc507875d)

> x를 넣으면, y -> x^2+y^2이 출력된다.

함수를 넣으면 y를 input으로 받는 함수를 다시 출력하도록 하는 것이지요. 이렇게 다시 함수를 출력하도록 하면 단일 인자만 받을 수 있도록 할 수 있습니다!

(x,y) = (5,2)는 다음과 같이 계산할 수 있습니다.

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/951bcb4894272800f3c7e53a20b4fbc1f7c5331d)

[1]   (x -> (y -> x^2 + y^2))(5) 계산을 하면 y -> 25 + y^2이란 함수가 출력이 됩니다.

[2]    (y -> 25 + y^2)(2)를 계산하면 25 + 4 => 29가 출력되게 되죠.

와우... 변수 하나를 넣고 그 변수를 제외한 변수들의 함수를 반환하는 방법으로 이게 가능하네요. 

이와 같이 여러 argument를 받는 함수를 단일 argument로 받는 함수의 chaining으로 구현하는 방법을 **currying**이라고 부른답니다.



> *의문*
>
> 한편으로, 1번째 단계에서 직관적으로는 받아들여졌지만 곱씹을수록 어색함이 있습니다. 보통 수학의 함수에서 argument를 넣으면 그 안의 값이 평가가 되지, 출력으로 나온 함수내부 값 평가에 평가되진 않습니다. 
>
> 다시 말해 x에 5를 넣었더니 y->x^2+y^2 의 함수의 x평가에 사용된 부분 말이죠.  이 부분이 놀랍네요.  추후 이는 β-reduction이라는 용어로 불릴 예정인 것 같아요.



3. 추가적으로 parameter에 대해서, eng wiki엔 없지만 ko wiki에 있는 설명을 첨부하겠습니다.

함수를 표현할 때 (x,y) -> x+y라 하든, (u,v) -> u+v라 하든 변수 명 자체는 큰 의미가 없죠? input과 output간 변수의 연결 고리가 중요한것이지요. 이러한 내용도 동기가 되었다고 하네요.



# 마치며

이번 글은 이정도로 마치고, 다음엔 본격적으로 lambda-calculus의 구성 요소들에 대해 설명드리도록 하겠습니다.

