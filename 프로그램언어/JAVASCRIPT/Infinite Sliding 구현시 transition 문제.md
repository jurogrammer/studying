# Infinite Sliding 구현시 transition 문제

무한 슬라이딩 윈도우 구현시 애니메이션 효과가 정상적으로 작동하지 않는 문제가 발생했습니다.

분명 부드러운 이동 효과를 준 후 이동했는데도 순간이동 한다던지, (부드러운 효과 -> 이동)

부드러운 이동 효과를 제거하고 이동했음에도 부드러운 이동 효과가 남아있었습니다. (부드러운 이동 효과 제거 -> 이동 -> 부드러운 효과 켜기) 따라서 이를 해결하기 위한 과정을 적어보려 합니다.



## 참고자료

* https://d2.naver.com/helloworld/59361 (Naver D2 브라우저는 어떻게 작동하는가)
* https://medium.com/@gneutzling/the-rendering-process-of-a-web-page-78e05a6749dc (The rendering process of a web page.)
* https://developers.google.com/web/tools/chrome-devtools/evaluate-performance?hl=ko (google performance tool 사용법)

### 상황

슬라이드가 1,2,3 이 있다고 할 때, 무한 슬라이딩 윈도우를 구현하기 위해 다음과 같이 프로세스를 세웠습니다.

1. s1,s2,s3,s`1으로 설정
2. 애니메이션 효과 키기
3. s3->s\`1으로 이동 했을 때, s\`1에서 애니메이션 효과 끄기
4. s`1에서 s1으로 이동
5. s1에서 애니메이션 효과 키기

이와 같이 구성하려 했습니다.

허나 문제는 절차 3->4->5에서 발생했습니다.



## 문제

### 문제1.

1. **아래의 코드를 1번째 실행 시** : 슬라이딩 효과가 미적용된 채 정상 작동합니다.

2. **아래의 코드를 2번째 실행 시** : 슬라이딩 효과가 적용 된 채 작동됩니다.


이에 따라서 문제는 다음과 같이 말할 수 있습니다. 
**"3이 적용 되지 않은 채 4가 발생한다."**

이를 검증하기 위해 다음과 같이 코드를 작성해보았습니다.

```js
turnOn();
//일정 시간이 지난 후에 아래 코드 실행
shift(100);
turnOff();
```

결과는 놀랍게도 애니메이션 효과가 미적용된 채 이미지가 이동합니다!!!



브라우저는 어떻게 작용하길래 위와 같은 문제가 발생했을까요?

```js
var img = document.querySelector("#logo-default");
var curPos = 0;

function turnOn() {
    img.style.position = "relative";
    img.style.transition = 2000+"ms";
    img.style.transform = "all";
}

function turnOff() {
    img.style.transition = "";
    img.style.transform = "";
}

function shift(dev) {
    curPos += dev;
    img.style.left = curPos + "px";
}
turnOff(); //transition 기능 중지.
shift(200); //transition 없는 상태 +200이동
turnOn(); //그리고나서 transition키기
//이 코드의 문제점 : +200 이동할 때 21번째줄 turnOff()가 적용되지 않은 채 transition 적용이 됩니다.
```





### 문제2.

```javascript
turnOn();
setTimeout(() => {
    shift(200);
},5000)
```

초기시작 시에 turnOn() 이후 5초후 200만큼 이동했음에도 **순간이동**합니다.

이건 또 도대체 뭐가 문제일까요...

처음에 동일한 문제로 보느라 아주 골머리를 쌋습니다.



## 문제 분석

### 분석 툴

google dev tools에서 performance의 timeline을 보고 해결하기로 정했습니다.



### 실험

**목적**

작성하려한 대로 실행하면 브라우저에서 어떤 일이 일어나는지 확인.

**1.init turnOff - shift - turnOn**
결과 : 순간이동 

![](https://postfiles.pstatic.net/MjAyMDA2MTVfMjg0/MDAxNTkyMjEwODQwMDA1.mHAx3LsprNbb4RyL6cbwEaoJS2-LslAAtX1FjeqGYrsg.-oDAFVcWmn_Jxli-yZX7_u5nRWBmXCKPH4kT0-Bzc5Mg.PNG.study_ju/init_trunOff-shift-turnOn(2).PNG?type=w966)

* 보시다시피 function Call을 모두 실행한 후에 rendering이 시작됩니다. 그렇다면 정상작동해야 되는데 순간이동 해버립니다.
* 또한, turnOff와 shift, 그리고 turnOn이 **한 호흡에 실행된 후에 스타일 렌더일이 발생**하는 것을 볼 수 있습니다.  따라서 순간이동 후 다시 슬라이드 효과를 주려면 다음 호흡에서 실행되도록 해야 함을 알 수 있습니다.



**2.init turnOn- setTimeout(shift)**
결과 : 순간이동

**목적**

처음 애니메이션 적용시, 설마 turnOn이 적용되지 않은 채 이동했나 싶어 위와 같은 실험을 해보았습니다.

![](https://postfiles.pstatic.net/MjAyMDA2MTVfMjE2/MDAxNTkyMjExNjY0MzEw.Y2UpSRccUXMysN81mg2-9N_QiFCN6aT5rTbk65R61q0g.gdBHstSQ-IzMxqB-qc4DGewvqLI85Q8bRMuH8iYdL2Eg.PNG.study_ju/init_turnOn-shift.PNG?type=w966)

* 보시는 바와 같이 turnOn에서 정상적으로 렌더링 한 후에, shift에서 또 다시 렌더링을 하죠. 즉, 정상적으로 turnOn이 적용되었다고 볼 수 있습니다.



* **한편으로, 생각해보면 turnOn이 정상작동되지 않았다면, 페이지 이동조차 되지 않았을 겁니다. position : relative효과는 turnOn에서 실행된것이니까요. 설마 코드의 맨 윗줄만 실행되고 말았나 싶어 위치를 바꾸어보았습니다. 하지만 결과는 동일하게 순간이동 되었습니다.**



**3.init  turnOn-shift(0)-shift(200)**

결과 : 부드러운 이동

**목적**

turnOn의 transition 효과가 한번이라도 이동이 발생해야만 적용되는것인가 싶어서 적용해보았습니다.



* 부드럽게 잘 이동합니다. shift()를 한번이라도 적용한 후에는 잘 작동되었습니다. 도대체 무엇이 문제일까 싶어서 stack overflow에서 찾아보던 결과... 초기 left값이 셋팅이 되지 않아서였습니다. 분명 이전 슬라이딩 윈도우짤 때도 이 부분 때문에 애먹었었는데 또 같은 실수를 반복했네요..



## 문제 결론

결론적으로 2가지 관점에서 예상한 대로 움직이지 않은 원인을 알 수 있었습니다.

1. browser의 schedule

   브라우져의 스케줄에 의해 Js가 먼저 모두 실행된 다음 rendering으로 넘어갔기 때문에 부드러운 이동 효과가 적용된것입니다.

2. 초기 위치 지정

   이미지의 절대 위치를 지정해주지 않는 이상 브라우저는 이미지의 위치를 모릅니다. 따라서 이를 지정해주지 않았기 때문에 처음에 순간이동 하였고, 그 뒤엔 브라우저가 위치를 알고 있으므로 정상적으로 작동하였습니다.



## ...

**명확히 알아서 불분명함을 극복하자!**

Js를 통해 브라우저를 조작하다보면 예상치 못한 결과가 꽤나 발생합니다. 그런데 이번에 브라우저가 어떻게 작동하는지 살펴봄으로써 Js에 대한 두려움을 한 번 넘어서는 계기가 되었습니다. 



**chrome browser 공식문서는 어디에..?**

한편으로 chrome 작동방식에 관한 문서를 못찾았는데... 네이버 D2 를 보니 표준안이 있다고 하더군요. 어쩐지 Firefox랑 Chrome이 동일한 결과를 내주었었는데 이런 이유같습니다.



**앞으로 문제 원인 분석을 위한 방법은 아래와 같이 체계적으로!**

앞으로 분석할 땐 위처럼 문제 원인을 진단하기 위해 어떤 **신뢰성있는 툴**을 이용할 것이고, 어떤 **가설**을 세우고, 어떤 **실험**을 하여 증명할지 지금보다 구체적으로 정해야겠습니다. 위와 같이 실험한 것은 주먹구구식으로 하다가 정리하게 된 것 입니다..



파이팅!