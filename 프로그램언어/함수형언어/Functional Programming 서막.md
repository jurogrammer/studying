# 출처

* https://en.wikipedia.org/wiki/Functional_programming
* https://www.geeksforgeeks.org/introduction-of-programming-paradigms/



# Functional Programming 서막

### ? 왜 이걸 쓰나요?

이번 년도 3월, 처음 자바스크립트를 배웠을 때 입니다. 이 언어를 처음 마주했을 때 느낌은 오묘했습니다. C언어같다가도... Java같다가도 처음보는 문법도 있었습니다.

Javascript의 문법에 제가 놀란 부분은 총 3가지였습니다. Map, Closure, 그리고 함수였습니다.

Map은 파이썬에서도 즐겨 사용했는데 javascript에서도 구현되어 있어서 '아... 자주 사용하는 함수구나 사람들이 즐겨 사용해서 여기에도 있나보넹~' 하고 넘어갔죠.

또 Closure입니다. 얘는 어떻게 돌아가는진 알겠는데 어떤 상황에서 필요하길래 이게 있는지 도저히 이해가 안됬어요. geeksforgeeks나 MDN사이트를 찾아가서 정독해서 읽어봐도 왜 그상황에서 쓰는건지 이해가 안됬죠. 다른 언어에서는 다른 방식으로 충분히 구현했던 것 같은데 말이죠.

마지막으로는 함수였습니다. OMG... 함수를 변수로 선언하고, 인자로 받고 심지어 함수가 또 함수를 반환하다니... 뒤통수 맞는 느낌이였습니다. 그래서 당시에 일급 함수가 뭔지 온종일 찾아봤습니다.

그 뒤 전 취직을 하여 js와 약간 멀어지면서 위와 같은 개념에 다시 애먹을 일이 없을 줄 알았습니다만... 루비를 사용하면서 또 다시 비슷한 놈을 만났습니다. 루비의 block이란 개념이요!

아니 무슨... 코드 덩어리를 넘겨준다고?? 이게 말이되나? 변수같은 것만 넘길 수 있던거 아니야?; 하면서 큰 혼동이 왔습니다. 여태 이렇게 구현하지 않고도 충분히 잘 작성했던 것 같았으니까요.

블록에 대해 공부하다가 위 고민을 하나로 이어주는 단어를 찾았습니다. 바로 ***함수형 프로그래밍(Functional Programming)***이였죠.

와... 제가 받아들일 수 없었던 내용들이 쏙쏙 나와있었죠. 그래서 하루정도 투자해서 자료를 찾아봤는데 내용이 너무 어려웠습니다 ㅠㅠ 수학에서 파생된 개념이 많았죠.

이번에 Java를 공부하면서 java8에 Funtional Programming 개념이 추가된게 있어서 정복하고자 이 글을 써봅니다.



함수형 언어는 명령형 언어의 패러다임에 속하는 방법입니다. 따라서 선언형 언어와 명령형 언어를 차이점을 알아보는게 좋을 것 같아요.  이를 머리 속에 박고 시작해야 C,JAVA와의 차이점이 눈에 보이거든요.



### 선언형 언어와 명령형 언어

![](https://media.geeksforgeeks.org/wp-content/uploads/1-344.png)

(출처: https://www.geeksforgeeks.org/introduction-of-programming-paradigms/)

위 그림은 geeksforgeeks에서 Bhumika_Rani라는 분이 올려준 내용입니다.  두 가지 차이점을 간단히 말씀드리자면 다음의 예시를 볼 수 있어요.

![](https://postfiles.pstatic.net/MjAyMDExMjJfNjcg/MDAxNjA2MDMzMzI5MzQ1.y3Vfu3SV7WiZ0L78ijVf23qeugooTxNVcOFOQWAbc1Ag.akmCJUC7GoxoW7wr0vFbexebon6QRPIV50xfivrJmoIg.GIF.study_ju/ezgif.com-gif-maker.gif?type=w966)

제가 무언가를 했습니다.

이를 뭐라고 표현하실 건가요?



선언형 언어 관점에서는

>  '네모 그렸네요.'

라고 말할 수 있고요,

명령형 언어 관점에서는

>  '점을 찍고 아래로 선을 그리고 반시계 방향으로 90도 꺽어서 선을 그리고 또 반시계방향으로 90도 돌려서 선을 그리고 마지막으로 반시계 방향으로 90도 돌려서 선을 그렸습니다'

라고 말할 수 있어요. 감이 오시나요?

위 느낌의 차이 때문에 선언적 vs 명령형 이란 단어가 붙었구요 또한 WHAT vs HOW 라고 하기도 합니다. 선언형은 무엇을 그릴지에 관심이 있고, 명령형은 어떻게 그릴지에 관심이 있는지 물었다 볼 수 있어요.

그리고 개인적으로 Clean Code에서 봤던 관점으로는 다음과 같이 말할 수 있을 것 같아요. 행위를 추상화 시켜서 (요약하여) 말했다 vs 구체적으로 구구절절 말했다. 라고요.



그래서 C언어는 명령형 중 절차지향언어에 속하므로 변수에 뭘 할당하고... 어떻게 반복하고 등등 이렇게 코딩합니다. 반면에 선언형에 속하는 SQL을 볼까요? 

`SELECT name FROM students`

딱 요약해서 말하고 있죠? 스튜던트 테이블에서 이름 가져와! 라고만요. 여기에 스투던트 테이블의 col이 name이고... 구체적으로 쓰지 않았죠? 이게 큰 차이입니다!

함수형 언어는 이러한 패러다임에 속한다 볼 수 있어요.



### 그래서 함수형 프로그래밍이 뭔데?

함수형 프로그래밍은 간단히 말해서 함수로 작성한 언어입니다. 함수로 함수를 구성하고, 그 함수를 적용하여 프로그램을 만드는 방식이라는 겁니다.

1937년도에 Alonzo Church라는 분이 lambda calculus를 통해 이미 소개되었었죠. 이 패러다임은 간결성, 불변성때문에 요즘 핫해지고 있어요!



그럼 이번 글에선 함수형 언어의 특징에 간단히 알아보고 앞으로 이 주제에 대해 자세히 풀어나가보겠습니다. 저도 자세히 몰라서 ㅎㅎ; 이런 컨셉이다라고 넘어가면 좋을 것 같습니다.



### 함수형 언어의 Concept들



함수로 작성하는 언어에요. side effect를 줄이기 위해 만들었죠. 또한 개인적으로 가독성도 좋아지는 것 같아요.

히스토리 불라불라 설명.

### Concepts

#### 1. First-class and higher-order functions

Higher-oroder functions는 한글로는 고계함수로써, 함수를 arguments로 받고 함수를 반환하는 형태를 의미합니다. 고계함수는 함수를 다루는 함수라고 말을 합니다.

아래 내용을 볼까요? 전 이것을 보고 머리가 뿅! 해지더라구요

<img src="https://postfiles.pstatic.net/MjAyMDExMjJfMjgz/MDAxNjA2MDM0ODQ4MzQ3.yWVwwU6DmEbE3mRTryk7Bhe4tIpUdecM2-_H7VWE0sIg.SIO9MiTBW1GeE7mCq2BgI9EeU_8oZdhWKZPlx6WxD0cg.JPEG.study_ju/IMG_A981BB8B5BFF-1.jpeg?type=w966" style="zoom:50%;" />

수학에서 위와같은 식을 많이 봐왔잖아요? 수학에선 너무 당연하게 넘어갔던 것이였죠. 아무래도 수학에서 넘어온 개념이므로 이와같이 보는게 훨씬 낫겠습니다. 이를 컴퓨터 언어에서 구현한 것이라고 보시면 돼요.

그래서 컴퓨터언어 용어로는 고계함수가 아니라 일급객체라는 표현을 씁니다. 위에서 함수를 변수로 선언하는 것만 추가되면 되죠.

참고로 wiki에서 든 예시로는 미분입니당. 이해하는데 더 도움이 되셨으면 하네요.

<img src="https://postfiles.pstatic.net/MjAyMDExMjJfMTk5/MDAxNjA2MDM1MDE5NDMy.er_MZ27uWmyydAL7yfh37y0obn7t59gT_CPwOCaF_cYg.jJzz8cNiw93s9ZWPApTxD4prCgtAR5wwQ0TgMgv3HZog.JPEG.study_ju/IMG_A8FD2E242F21-1.jpeg?type=w966" style="zoom:50%;" />

그리고 함수가 함수를 반환하고 또 사용하는 형태에서,  partial application, currying이라는 핵심 개념이 나옵니다. 함수형 언어라고 검색하면 빠짐없이 나오는 키워드들이죠. 



#### 2. Pure functions

순수 함수란, side effect가 없는 함수를 의미합니다. 외부 요인에 input에 대해 output이 영향을 안받는다는 뜻입니다. 매우 신뢰할 수 있는 함수가 되겠지요! 그래서 병렬처리에 많이 적영됩니다.



#### 3. Recursion

팩토리얼 예제로 항상 다루는 그 개념이 맞습니다. 함수형 언어에서는 loop가 보통 recursion을 통해 구현이 됩니다. 



#### 4.Strict versus non-strict evaluation

evaluation이라고 하면 사전적 용어로 식을 계산하다라는 뜻입니다. expression(식)을 strict(eager) or non-strict(lazy)하게 계산하는 의미입니다.

다음 예시를 보니 명확히 와닿더군요.

```pytohn
print( length([2+1, 1/0]) )
```

이 exppresion을 evaluate한다면 결과가 어떻게 될까요?

exception이 발생한다고 하신 분들은 strict하게 평가하신 것이고, 2가 출력된다 라고 말씀하신 분들은 non-stric하게 평가하신 것입니다.

전자의 경우는 대부분 생각할 수 있는데 후자의 경우는 좀 생소할 수 있어요.

length라는 함수의 값을 반환하는데 있어서 결국 중요한건 컨테이너에 속한 elements의 수잖아요? 그래서 1/0을 아예 계산하지 않고 값을 반환한 것입니다.

오마이갓~!~!



#### 5. Type systems

이 부분은 잘 이해를 못했습니다... 추후 이 부분을 설명할 때 설명을 첨부하겠습니다. 컨셉조차 모르다니 ㅜ 마음 아프네요.



#### 6. Referential transparency

함수형 프로그램은 assignment를 가지지 않습니다. 왜냐하면 값이 변해버리니까요! 한 번 정의한 값은 변하지 않게 합니다. 사이드 이펙트를 없애려는 노력의 일환이지요.

이러한 형태를 referentially transparent하다 합니다.



#### 7. Data structures

함수형 언어에서 자료 구조는 독특합니다. 명령형 언어에서는 기존 array에 접근하여 값을 변경하는 반면에, 함수형 언어에서는 기존의 값을 유지(또는 영속)하는 형태를 지닙니다.

단순히 값을 복사해서 지내면 메모리가 문제가 되므로 이를 구현하는 방식이 여러가지가 있는 것 같습니다. 여기에 Closure와 Persistent vector라는 것이 나오네요



#### 8. 그 외...

그 외로 불변 상태를 어떻게 유지할 것이냐에 대한 문제에서 모나드(monad)란 개념이 나옵니다. 은행 계좌 문제를 떠올리면요, 결국 계좌의 잔고를 바꾸려면 계좌의 잔고를 더해주거나 깍아줘야하니까요. 어떻게 함수형 프로그래밍에서 이를 구현할 지 궁금하네요 ㅎㅎ



### 마지막으로...

이번 대주제는 Lambda calculus, Type Theory, monad(Category Theory)와 currying에 많은 시간을 투자해야할 것 같습니다. 

Lambda calculus는 함수형 프로그래밍의 근간이 되는 내용이며,

Type Theory는 요즘 타입스크립트처럼 대두가 되고 있는 내용이기도 하고 개인적으로도 컴파일 타임에 잘못을 확인해줄 수 있다는 점에서 좋아하는 내용이기도 합니다. Java Specifiation을 봤을 때 어려웠던 내용이기두 하구요 ㅜㅜ

마지막으로 monad와 currying은 함수형 프로그래밍에서 하도 언급되는 내용이라 어휘가 친숙해졌지 전혀 모르는 내용이라 관심이 많이 갑니다. monad는 난이도가 악명높기도 해서많은 시간을 투자하겠죠..ㅎ;

함수형 프로그래밍에서 개념을 마인드매핑한 이미지로 이 글을 마무리 짓겠습니다.

![](https://postfiles.pstatic.net/MjAyMDExMjJfMzEg/MDAxNjA2MDIyODg2MjQ3.1WyRJzwY8kmh6LTt5YDIwZYGMcxp7XqUZoZcV8i9bjsg.7sFARU6RkEk710XQXtJIokYP2BIoPkfbBlp6IuZtGl8g.PNG.study_ju/Functional_prgoramming_mind_map_(1).png?type=w966)