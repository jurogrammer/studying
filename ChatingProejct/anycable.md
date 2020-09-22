AnyCable정리

# 1. Message

* 통신은 메시지 기반.
* 모든 메시지는 object임

### server to client

서버에서 클라이언트로 보내는 프로토콜 관련된 메시지는 반드시 type field를 가져야 합니다.

* 가능한 type field

  ```
  [welcome]
  [disconnect]
  [ping]
  [confirm_subscription]
  [reject_subscription]
  ```

* 데이터인 broadcasts message, transmission-they 는 모두 message field를 가지고 있어야 합니다.

### client to server

클라이언트에서 서버로 보내는 프로토콜과 관련된 메시지는 command field를 가지고 있어야 합니다.

* 가능한 commands

  ```
  [subscribe]
  [unsubscribe]
  [message]
  ```



### Handshake

클라이언트가 서버에 접속할 때 발생하는 일

1. 서버가 연결 받고 클라이언트에게 웰컴 메시지 보냄

   ```json
   {"type":"welcome"}
   ```

2. 커넥션 거절 메시지를 보낼 수 있음.

   ```
   {"type":"disconnect", "reason":"unauthorized", "reconnect":false}
   ```



서버는 반드시 위 두 메세지 중 하나를 보내야 함.



### Subscriptions & identifiers

Data messages인 클라이언트 -> 서버나 서버 -> 클라이언트 메시지들은 모두 반드시 identifier 필드를 가지고 있어야 합니다.

identifier필드는 데이터를 특정 채널에 라우트 하기 위해 사용됩니다.

어떻게 identifier를 생성하고 resolve할 지는 서버와 채널에 달려 있습니다.



