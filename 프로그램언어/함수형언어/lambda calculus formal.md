# 참고자료

* https://en.wikipedia.org/wiki/Lambda_calculus#:~:text=Lambda%20calculus%20(also%20written%20as,to%20simulate%20any%20Turing%20machine.



# 개요

이전 게시글에선 lambda calculus를 informal하게 설명해드렸다면 이번엔 좀 더 수학적으로 정의한 것을 말씀드리는 시간을 갖도록 하겠습니다.

lambda caclulus에 대해 깊숙히 알아가려고 한다면 formal하게 정의하는 방법을 숙지해야겠죠. 자료들은 formal하게 쓰여있으니까요...



# Formal definition

### lambda expression의 구성요소

- variables *v*1, *v*2...

  변수 v1,v2....

- the abstraction symbols λ (lambda) and . (dot);

  추상화된 심볼인 lambda와 .(점)

* parentheses()

  소괄호



### lambda expression의 집합(Λ)은 귀납적으로 정의됩니다.

1. If *x* is a variable, then *x* ∈ Λ.

   x가 변수라면 Λ에 속합니다. 즉, 위에서 정의했던 람다 익스프레션의 구성요소 중 하나라고 말할 수 있는 것이죠.

2. If *x* is a variable and *M* ∈ Λ, then (λ*x*.*M*) ∈ Λ.

   x가 변수이고, M이 Λ에 속한다면, (λ*x*.*M*)이 또한 Λ에 속한답니다. 서로 Λ에 속한 것들에 대한 함수식은 Λ에 속한다는 것이죠. (이런 부분 때문에 귀납적으로 정의된다 하는 것 같네요.)

3. If *M*, *N* ∈ Λ, then (*M N*) ∈ Λ.

   M과 N이 Λ에 속한다면, (M N)도 Λ에 속한답니다. 위에서 봤던 application에 속하죠.



흠... 쭉 보면요. 정리하자면 결국 다음과 같이 말할 수 있을 것 같습니다.

**"람다의 구성요소에 대해서, 람다 수식 적용해도 람다 expression이다!"** 라고요. 

왜 이렇게 정의해야 하냐면 또 이전에 봤던 함수를 연속해서 계산하게 되잖아요 ? 커링인가 머시기. 만약에 중간에 다른 차원이 나온다면 커링이 되겠습니까... 1x2x5를 연산하는데, 1x2에서 참치가 나왔어요. 그러면 참치x5가 연산이 돼요?

그러니깐 이런식으로 정의 한 것 같아요.



### Notation

표기를 깔끔하게 정의하기 위해 다음과 같은 컨벤션을 따른다고 합니다.

- Outermost parentheses are dropped: M N instead of (M N).

  가장 바깥 소괄호는 생략

- Applications are assumed to be left associative: M N P may be written instead of ((M N) P).

  application은 좌측부터 연산합니다.

- The body of an abstraction extends as far right as possible: λ*x*.*M N* means λ*x*.(*M N*) and not (λ*x*.*M*) *N*.

  abstraction의 body(λ*x*.M에서 M 해당하는 부분)은 가장 바깥까지 취급합니다.

- A sequence of abstractions is contracted: λ*x*.λ*y*.λ*z*.*N* is abbreviated as λ*xyz*.*N*

  λ*x*.λ*y*.λ*z*.*N* 처럼 abstraction의 나열은 λ*xy*z*.*N 으로 축약됩니다.



### Free and bound variables(자유변수와 종속변수)

1. λ를 abstraction operator라고 부르는데요, body에 있는 모든 variable을 bind하다고 말합니다. abstraction 안에 있는 abstraction이 bound한다고 말하죠.

2. λ*x*.*M*에서 λ*x*를 binder라고 부르고요, λ*x*가 M옆에 붙어서 variable x가 bound된다고 말합니다. 다른 변수는 모두 free variable이라고 말할 수 있죠.

   * 예시 λ*y*.*x x y* 

     Notation에서 3번째에 따라 λ*y*의 body는 x x y입니다.

      그리고 λ*y*에 의해 y가 bound되므로 y는 bind variable입니다.

     그리고 안묵여 있는 x는 free variable이라 말할 수 있죠.

3. variable은 가장 가까운 abstraction에 의해 bound 됩니다.

   * 예시 λ*x*.*y* (λ*x*.*z x*).

     맨 우측 x는 두번째 abstraction에 의해 bound 됩니다.



M이라는 lambda expression의 free variable 집합은 FV(M)으로 표기되고, 다음과 같이 재귀적으로 정의됩니다.

1. FV(x) = {x}, where x is a variable.

   x가 변수라면 x의 free variable의 집합의 원소는 x 하나밖에 없다는 뜻이네요.

2. FV(λ*x*.*M*) = FV(M) \ {x}

   흠... 기호가 어떤 기호인지 찾아봐도 잘 안나오네요. 유추해보았을 때 M의 free variable에서 x원소의 차집합을 구한것 같습니다.

3. FV(M N) = FV(M) ∪ FV(N)

   M N의 자유 변수 집합은 M의 자유변수 집합 그리고 N의 자유 변수 집합의 합집합이랍니다.



free variables가 없는 expression은 closed되었다고 표현하며, closed는 combinators 또는 combinatory logic이라고 한답니다.

> 흠... 전혀 감이 안잡히는 어휘네요. 일반적으로 생각했던 함수들 f(x) = 4x 이런 것들이 combinator이라는건데... 추후 파고 들어야겠습니다.





오늘은 이전에 말씀드린 Informal한 내용을 formal하게 전달드렸습니다. 이제 연산에 대해 말씀드리려고 해요. Reduction 말이져. 이것까지 알면 lambda calculus에서 수학연산을 알려드릴 수 있습니다.!

두근두근~ 다음 글에서 뵙겠습니다.