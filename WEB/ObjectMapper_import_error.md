에러메세지

```
java.lang.ClassNotFoundException: com.fasterxml.jackson.databind.ObjectMapper
```

이 에러메세지는 ObjectMapper를 못찾아서 발생한 에러. 하지만 eclipse library에 들어가보면 해당 파일은 존재한다.

처음에 잘 작동되다가 이후에 이 에러가 발생하면서 안됨.

### 시도한 방법1 [.M2] 폴더를 삭제한다.



1. eclipse종료
2. C드라이브/user/.M2 폴더 삭제
3. eclipse 해당 메이븐 프로젝트 우클릭 -> Maven ->Update project 클릭
4. 재실행

위와 같은 방법을 해보았지만 import error

### 시도한 방법2 jackson 의존성을 다른 버전으로 바꾼다.



##### 최신버전 업그레이드 

-------

1.pom.xml 

2.아래 내용 추가

```
<dependency>
    	<groupId>com.fasterxml.jackson.core</groupId>
  	    <artifactId>jackson-databind</artifactId>
    	<version>LATEST</version>
</dependency>
```

3.eclipse 해당 메이븐 프로젝트 우클릭 -> Maven->Update project 클릭

4.재실행

이 방법 또한 실패. import error

##### 2.9.0버전 다운그레이드

------

실패!



### 시도한 방법3 project삭제 후 재설정

1,2방법 모두 실패해서 프로젝트를 삭제하고 다시 설정하였다. 재설정시엔 jackson 의존성 패키지를 LATEST로 설정해주었다. 그리고 java13.0.2 버전이라 java버전도 1.8이 아닌 13으로 설정해주었다. (java 버전 8이상부터는 13.x.x버전이면 13이라고만 표시해주면 된다.)



이 방법으로 시도하니 다시 잘 된다.



import문제 때문에 2시간동안 애먹었다...