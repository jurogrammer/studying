# 1. mysql driver 클래스명 변경으로 인한 에러

에러메세지

```
Loading class `com.mysql.jdbc.Driver'. This is deprecated. The new driver class is `com.mysql.cj.jdbc.Driver'
```

설명대로 com.mysql.jdbc.Driver이란 클래스 이름이 com.mysql.cj.jdbc.Driver 이름으로 변경되었다.

드라이브를 불러올 때 Class.forName("com.mysql.cj.jdbc.Driver");  로 불러오면 해결.



# 2. mysql KST 서버타임존 미인식으로 인한 에러

에러메세지

```
The server time zone value '대한민국 표준시' is unrecognized or represents more than one time zone. You must configure either the server or JDBC driver (via the 'serverTimezone' configuration property) to use a more specifc time zone value if you want to utilize time zone support. null
```

시간을 KST를 UTC로 변경해주면 된다. 이는 dburl불러올 시 jdbc:mysql://localhost:3306/db이름 뒤에 다음과 같은 url링크로 작성해주면 된다.

```
?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC
```

이렇게 하면 해결!