# 블록요소 내 텍스트 수직 중앙 정렬 하는 방법.



#### **시도1)**

vertical-align : middle

안됨; 왜 그러는지는 잘 모르겠다.



#### 시도2)

text-align : center:

수직, 수평 가운데 정렬이 된다. ...?



#### 시도3)

블록요소 wrapper를 생성한 후, 

부모 element 를 display : flex로 만든 후

justify-content : center 

블록요소가 수직,수평 가운데 정렬이 된다.



#### 시도4)



블록요소 wrapper를 생성한 후, 

부모 element 를 display : flex로 만든 후

align-items : center 

블록요소가 수직가운데 정렬이 된다! 해결.