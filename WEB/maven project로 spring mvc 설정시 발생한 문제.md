# maven project로 spring mvc 설정시 발생한 것





## 1.web.xml servlet 버전 에러

해결

1)tomcat버전 확인하여 그에 맞는 servlet버전 입력할 것. (프로젝트 생성시 구버전으로 작성되어있다.)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
version="3.1"/>
```

