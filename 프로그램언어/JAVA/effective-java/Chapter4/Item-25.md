# Limit ource files to a single top-level class

자바가 아무리 하나의 소스 파일에 multiple top-level class에 대해 경고하지 않고 실행시키지만, 위험하고 어떤 이점도 없습니다.

이렇게 하면 한 클래스를 여러가지로 정의할 수 있게되고, 어떤 것이 실행될지는 컴파일 순서에 따라 변경됩니다.





# 해결책

### 1. top-level class를 서로 다른 소스파일로 분리

### 2. static memer class로 선언

