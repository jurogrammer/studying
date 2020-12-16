#### source

말 그대로 데이터의 원천으로써, 보통 collection이나 Generator function이 됨.



#### stream

collection과 다른 개념임. 데이터를 담아둔 data structure가 아니라 pipeline을 통해 source로부터 값을 전달해주는 애입니다.



#### aggregate operation



##### 	1. Zero or more *intermediate operations*

​		얘네들은 결과로써 new stream을 생산함

##### 	2. terminal operation

##### 		ex:) forEach

​		stream내 여러 값을 조합하여 하나의 값을 반환하는 operations. 이걸 reduction operation이라고 부른다.

​		non-stream 값을 생산합니다. ex:) primitive value, collection or no value

컴파일러가 e가 Person type인지 추론해냄.



#### pipline

aggregate operation의 나열입니다.



#### mapToInt

새로운 stream type을 내놓도록 해줍니다. 이건 IntStream

파라미터에 명시된 function을 스트림의 각 요소에 적용함.



#### average

stream에 저장된 요소들의 평균을 구합니다. 그리고 type은 OptionalDouble을 내놓지요.



