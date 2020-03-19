# jdbc mysql 연결 방법



## 연결절차

#### 1.java의 sql package 로드

```java
import java.sql.*;
```



#### 2.Mysql Driver 로드

```java
Class.forName('com.mysql.cj.jdbc.Driver');
```

Class.forName은 클래스를 로드해주는 역할함. com.mysql.cj.jdbc.Driver란 클래스를 로드해주는 것이다. 이후 이 클래스는 java.sql에 있는 DriverManager가 이용하게 됨



#### 3.mysql과 connection

```java
Connection conn = DriverManager.getconnection("dburl,dbUser,dbpasswd");
```

해당 연결을 Connection 객체에 담아준다.



#### 4.sql작성하여 준비

```
PreparedStatement ps = conn.prepareStatement(sql);
```

바로 sql작성하여 실행한다기보단, 연결 객체의 prepareStatement메소드에 sql을 입력하여 preparedStatement객체를 생성한다. 

이때, sql에 들어갈 값이 변동된다면 다음과 같이 작성해주면 된다.

```java
String sql = "SELECT description,role_id FROM role WHERE role_id = ?";
			ps = conn.prepareStatement(sql);
			ps.setInt(1, roleId);
			rs = ps.executeQuery();
```

변동하는 부분에 ?를 넣고, ps.setInt를 통해 값을 넣어준다. ps.setInt(1,roleId);의 뜻은 첫번째 물음표에 인트타입의 roleId를 넣어준다.는 의미. *(sql을 바로 실행하지 않고 ps에 담아두는 이유는 sql이 이렇게 불완전할 수 있어서 그렇구나?)*

#### 5.sql 실행

```java
ResultSet rs = ps.excuteQuery();
```



sql이 출력을 하는 질의면 ps.excuteQuery()를 통해 결과값을 가지는 객체를 생성 후 ResultSet객체에 담는다.



#### 6.결과물 출력

```
while(rs.next()){
	String description = rs.getString(1);
	int id = rs.getInt("role_id");
}
```

결과물을 한 번에 다 주는 것이 아닌, 해당 데이터가 있는 pointer를 넘겨받고 한행 한행 결과를 rs를 통해 받는다.

그리고 rs에 담겨진 결과물을 출력하는 방법은 rs.getString or rs.getInt를 통해 수행되며, 들어간 메소드엔 열의 번호 또는 열의 이름을 통하여 출력할 값을 선택할 수 있다.

값을 받을 객체는 Dto를 통해 값을 전달하여 출력.

모든 작업이 끝난 후엔 생성된 했던 객체 conn,ps,rs 를 역순으로 없애준다.





## 에러를 고려한 코드



#### 1.DriverManager 로드 오류 캐치

```
try {
			Class.forName("com.mysql.cj.jdbc.Driver");
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
```

mysql 드라이버 클래스를 로드. 이때 클래스가 없는 에러가 발생한다면 해당 내용을 출력



#### 2.커넥션생성 후 ps객체에 sql담아 실행하는 에러 캐치 후 ps객체로 출력시 에러 캐치

try (Connection conn = DriverManager.getConnection(dburl, dbUser, dbpasswd);
				PreparedStatement ps = conn.prepareStatement(sql)) {

```java
		try (ResultSet rs = ps.executeQuery()) {

			while (rs.next()) {
				String description = rs.getString(1);
				int id = rs.getInt("role_id");
				Role role = new Role(id, description);
				list.add(role); // list에 반복할때마다 Role인스턴스를 생성하여 list에 추가한다.
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	} catch (Exception ex) {
		ex.printStackTrace();
	}
	return list;
```


## Try with resource

conn,ps,rs객체 받을 시 Connection conn = NULL;  처럼 선언하고 받았다면 객체 생성 한 후에 finally에서 그 객체를 닫아주는 부분을 작성해주어야 하는데 , try부분에 위처럼 할당받았다면 알아서 객체를 삭제해줌. 이를 try with resource 구문이라고 한다.



