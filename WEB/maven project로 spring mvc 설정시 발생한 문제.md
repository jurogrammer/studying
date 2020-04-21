# maven project로 spring mvc 설정시 발생한 것



## 1.java version 불일치

#### 설명

java를 14로 사용하려고 하나 facet에서 13까지 밖에 없음. 결국 java version이 불일치.

#### 해결

1)pom.xml maven-compiler-plugin 설정

```xml
<plugin>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.8.0</version>
    <configuration>
        <source>14</source>
        <target>14</target>
    </configuration>
</plugin>
```



2)eclipse의 Navigator window에서(모든 파일 보기 가능) .settings 폴더의 org.eclipse.wst.common.project.facet.core 설정

```xml
<?xml version="1.0" encoding="UTF-8"?>
<faceted-project>
  <fixed facet="wst.jsdt.web"/>
  <installed facet="jst.web" version="3.1"/>
  <installed facet="wst.jsdt.web" version="1.0"/>
  <installed facet="java" version="14"/>
</faceted-project>

```

java version을 14로 설정함.



3)maven update 및 eclipse 재시작



## 2.web.xml servlet 버전 에러

해결

1)tomcat버전 확인하여 그에 맞는 servlet버전 입력할 것.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
version="3.1"/>
```

