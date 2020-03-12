# Ajax

Asynchronous Javascript and XML의 약자(지금은 XML에 제한된 내용은 아니다.)

* asynchronous란?

  서버에게 데이터를 받는 동안에 다른 행동을 할 수 있는 것. 즉, 새로운 탭을 눌렀을 때 해당 탭이 로딩되는 동안 다른 작업을 할 수 있다면 비동기적, 로딩할 때동안 다른 작업을 할 수 없다면 동기적이라할 수 있다.(작업과 데이터 로딩간 동기말하는 듯)

#### 예제 1

----

서버에 특정 data파일을 요청하여 해당 파일을 웹페이지에 띄우기.

```.{javascript}
function ajax(data){
	var oReq = new XMLHttpRequest(); //객체 생성
	oReq.addEventListener("load", function(){
		console.log(this.responseText); //콜백함수 나중에 실행됨 밑 open및 send먼저 실행
	};
	oReq.open("GET", "http://www.example.org/getData?data =...."); //서버에 요청 준비
	oReq.send(); // 서버에 요청
}
```

위와 같이 서버에 요청하면 해당 http프로토콜의 위치에 있는 데이터를 JSON형태로 보내준다.



#### 예제2

----

html에 time: 이라 적혀있는데, excute버튼을 클릭하면 php문서에서 현재 시간 데이터를 가져와 time : 옆에 현재시간 표시하기.

demo1.html

```.{html}
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
	<p> time : <span id = "time"></span></p>
	<input type="button" id = "excute" value = "excute"/>
	<script>
	document.querySelector('input'),addEventListener('click', function(event){
		var xhr = new XMLHttpRequest();
		xhr.open('GET', './helloTime.jsp');
		xhr.onreadystatechange = function(){
			if(xhr.readyState === 4 && xhr.status === 200){ //4번 통신이 끝날 때 나타나는 이벤트 핸들러. 결과 200 성공
				document.querySelector('#time').innerHTML = xhr.responseText;
			}
		}
		xhr.send();
		
	} );
	</script>
</body>
</html>
```

time.php

```.{php}
<?php
$d1 = new DateTime;
$d1-> setTimezone(new DateTimezone("asia/seoul"));
echo $d1->format('H:i:s');
?>
```



위와 같이 작성하면 php문서를 불러올 때 echo를 통해 시간 값을 받음.

그리고 그 받은 시간 값은 xhr.responseText에 저장되며,

쿼리셀렉터를 통해 #time에 접근한뒤 innerHTML에 받은 시간 값 대입 (객체로 되어있음)



# fetch

XMLHttprequest의 최신기법.

#### 예제

```.{html}
<!doctype html>
<html>
    <body>
        <input type="button" value = "fetch" onclick="
        fetch('css').then(function(response){
            response.text().then(function(text){
                alert(text);
            })
        })
        ">
    </body>
</html>
```

css파일을 받아서 응답결과가 있으면 text를 alert 해줘.

##### 원리 및 문법해석

* fetch('javascript') : clinet가 server에게 javascript파일을 요청함.
* .then() : server가 응답을 받은 뒤 function(response){} 함수를 실행한다.
* then 내에 콜백 함수가 실행될 때 response객체를 input value로 주기로 api설명서에 작성되어 있음.
* 



*궁금증*

*1.함수에 addEentListener로 load?? 무슨 의미지*

*2.데이터를 JSON으로 받았다면 일반 텍스트로 어떻게 보여주나?*

