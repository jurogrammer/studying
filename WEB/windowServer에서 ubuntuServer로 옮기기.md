윈도우 -> ubuntu 서버 데이터 이식시 문제점



#### 1.JDK version 불일치

	* jdk verison을 일치시키기 위해 window 컴퓨터 jdk 설치
	* ubuntu apt-get 방식이 아닌 https://openjdk.java.net/install/ 이 사이트에서 설치
	* eclise에서 jdk 버전 수정



#### 2.경로 불일치

* properties 경로를 C://였다면 ubuntu에선 /home/ju..로 설정



#### 3.MYSQL version 불일치

* window에선 8.x 버전을 사용하다가 ubuntu에서 apt-get으로 얻는 것이 5.x라 5.x로 변경.
* 연결이 안된다... 원격으로 하려니 느리다.
* 



## 고민

#### 

#### 서버 옮긴 목적

server를 노트북에 놓으니 cpu잡아먹고.. ddns기능을 이용할수 없어서 집컴퓨터로 옮기자.

#### 문제

1. idle작업 환경 불일치로 인한 편의성 문제
   * window에서 idle로 작업하고 ubuntu로 파일을 옮겨서 테스트하는 방식으로 작업하려고 하는데... 여간 번거롭다. 공유된 폴더를 작업하는 방식으로 바꿔야할 듯 하다.
   * window에서 idle 작업하고 원격으로 ubuntu들어가서 또 eclipse작동하니 전혀 편한것 같지 않다.



#### 느낀점

1. 특정 프로그램의 버전이 영향을 주는 범위를 알아야 한다.
   * 영향을 주는 범위를 찾느라 소요한 시간이 최소 1시간은 되는 듯 하다.
   * 범위는 구체적으로.  -> os, class간.. , maven...