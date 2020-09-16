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



session이 `{sub}`패킷을 보냄으로써 토픽에 참여할 수 있습니다. (세션은 클라이언트와 서버가 연결된 상태를 의미하니까 서버 내부적으로 연결 상태를 가지는 것 같음.)



`{sub}` 3가지 기능을 수행합니다. - 자세한 내용은 `{sub}` 섹션에서 확인.

1. new topic을 생성하고
2. 유저가 토픽을 구독할 수 있게 하고
3. 세션을 토픽에 붙여줍니다.



user가 topic에 참여하면 `{pub}`패킷을 보내서 컨텐츠를 생성할 수 있고,
 **그 컨텐츠들은 다른 붙여진 세션**을 통해 `{data}`패킷으로 전송이 됩니다.



user는 `{get}` `{set}`을 통해 topic의 메타 데이터를 불러오고 업데이트할 수 있습니다.



토픽의 메타 데이터가 변경이 된다면, live sessions에 `{pres}`패킷으로 보고 됩니다.이는 영향을 줄 수 있는 모든 토픽에 전송을 합니다. (ex me packet)



```
When user's me topic comes online (i.e. an authenticated session attaches to me topic), a {pres} packet is sent to me topics of all other users, who have peer to peer subscriptions with the first user.
```





# 서버와 연결하는 방법

1. endpoint에 apikey를 넣어서 전송
   * 데모앱에는 default API key가 포함됨.
2. connection이 오픈되면 client는 {hi} message를 서버에게 보내야함. 서버는 {ctrl}메시지로 보냄(성공이나 실패나타내는 메세지)





# 유저

1. producer and consumer of messages
2. authentication level
   1. `auth`
   2. `anon`

3. 연결이 되면, 클라이언트 어플리케이션은 유저의 권한을 인증하는 {acc} 나 {login} 메세지를 보낼 수 있음. 
4. 유저의 속성들
   1. created
   2. updated
   3. status
   4. username (unique string used)



유저는 서버와 여러 세션을 연결하고 있을 수 있음. 각 세션은 User-Agent를 통해 태깅되어 있음. (클라이언트 구분)



A user may maintain multisple simultaneous connections (sessions) with the server. Each session is tagged with a client-provided `User Agent` string intended to differentiate client software.







# Authentication

인증 위치 ({acc}, {login})



token

basic

annoymous

- `rest` is a [meta-method](https://github.com/tinode/chat/blob/master/server/auth/rest) which allows use of external authentication systems by means of JSON RPC.



authentication method는 어댑터를 통해 구현될 수 있음.



로그인을 위한 인증, 무엇을 위한 인증... 등등으로 나뉘어 있음.





새로운 계정이 생성될 때, 어떤 authentication method를 쓸 것인지 서버에게 알려줘야 함.

When a new account is created, the user must inform the server which authentication method will be later used to gain access to this account as well as provide shared secret, if appropriate. 





