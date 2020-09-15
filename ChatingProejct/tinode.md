# 모르는 용어

* IM router

* publish-subscribe model

* long-polling



# 설명된 용어

* session

  

# 어떻게 동작하니?

#### Server

session과 user와 topics를 연결시킴



#### Session

클라이언트app과 서버간 연결을 의미



#### User

세션을 통해 서버와 연결한 사람들



#### Topic

명명된 커뮤니케이션 채널. (which routes content between sessions) (아마 이 토픽이 세션간에 데이터를 날라준다는 의미인 듯.)



#### User와 Topic은 고유의 ID를 할당받음.

##### User

usr + base64-URL-encoded pseudo-random 64-bit number ex:) usr2il9suCbuko

##### Topic



### Client

* ex:) mobile or web application
* **클라이언트**는 websocket이나 long polling을 통해 **서버**와 연결
* 클라이언트는 대부분의 일을 수행하기 위해 인증받아야 함.
* 클라이언트는 `{login}` packet을 보냄으로써 세션을 인증한다.
  * 자세한 내용은 [Authentication](https://github.com/tinode/chat/blob/master/docs/API.md#authentication) 에 있음.
* authenticated되면 클라이언트는 토큰 받음
* 동일한 유저에 대해 복수의 동시적인 세션이 생성됨.
  * Logging out is not supported?



#### Topic

세션이 생성되면 유저는 토픽을 통해서 통신가능해집니다.

type

1. me
   * 자신의 프로파일을 관리하고, 다른 토픽으로부터 알림을 받기 위한 토픽입니다.
   * 모든 유저에게 존재.
2. fnd
   * 다른 유저와 토픽을 찾기 위해 사용되는 토픽.
   * 모든 유저에게 존재합니다.

3. Peer to Peer topic

   두 유저만을 위해 생성된 토픽. 따라서 이 topic 이름은 다른 유저의 ID를 따릅니다. (따라서 usr2il9suCbuko 형식)

4. Group topic

   * 단톡방을 위한 채널
   * grp + 랜덤 이름으로 지정 ex:) grpYiqEXb4QY6s
   * 



