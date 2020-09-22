# Tinode의 validation을 알아보자

### validation이 뭔가요?

tinode에 회원가입시, 인증하는 절차입니다. (아니, 왜 인증이 필요하지?! 그 사람이 현실에 있는 사람인지 대응시키기 위해?)

사이트 이곳저곳 회원가입할 때 핸드폰 인증하고, 이메일 인증하고... 이런 것과 같다고 보시면 됩니다.



### 이 주제를 다루는 이유

신상마켓은 도소매상임을 인증하는 절차를 거쳐 가입하게 됩니다. 

그런데 개발하려는 채팅서비스는 **신상마켓 이용자들을 대상**으로 제공하려는 서비스입니다. 

신상마켓이 아무나 이용할 수 없는 것 처럼, 채팅서비스도 아무나 가입하도록 해서는 안됩니다. 신상마켓 서비스 이용자들이 사용하도록 해야지요. 그렇기 때문에 validation을 적용해야 합니다.



### 그럼 어떻게 validation을 적용할 생각?

회원가입시 요청을 아바라에 보낸뒤 아바라에서 해당 회원이 맞는지 확인한 다음에 접속가능하도록 합니다.

(만약에, 신상마켓 회원 아이디와 비밀번호 정보를 그대로 긁어온다면 필요없긴 하겠죠 ㅎㅎ;)



### validation을 어떻게 구현?

제가 잘못읽은 것일 수 있겠지만, API문서를 봤을 때 이에 대한 부분이 자세히 서술되어 있진 않은 것 같습니다. 그래서 어떤 API를 주고 받는지 살펴봤습니다.

#### 기본제공해주는 web에선 회원가입시 어떤 API를 주고 받을까?

![](https://postfiles.pstatic.net/MjAyMDA5MTdfNTUg/MDAxNjAwMzI3NTQ4MTIx.ItBZ6BRBL4wdAjQCjB1x034iK05Wu0XIbLSs8CAke9sg.E2L0jt6HL-BUQeNWFHjwcEPlabrwDW3rCWE5E25vG7cg.JPEG.study_ju/%EC%9D%B4%EB%AF%B8%EC%A7%80_2020._9._17._%EC%98%A4%ED%9B%84_4.23.JPG?type=w966)

Tinode에서 기본 웹으로 제공하는 사이트가 있습니다. 그 웹사이트에서 회원가입 요청을 했을 때 서버쪽으로 보내는 api입니다.

여기서 보시면 credential(cred) validation 방식을 서술하고 있습니다. email방식을 선택했고, 보낼 이메일 주소는 f@f.c이다.라고 되있네요.

오... 여기 소스는 워낙 잘 작성되어 있어서 소스에서 키워드를 email, validation으로 검색을 해봤습니다.



#### 코드

##### validator

```go
// Package validate defines an interface which must be implmented by credential validators.
package validate

import (
	t "github.com/tinode/chat/server/store/types"
)

// Validator handles validation of user's credentials, like email or phone.
type Validator interface {
	// Init initializes the validator.
	Init(jsonconf string) error

	// PreCheck pre-validates the credential without sending an actual request for validation:
	// check uniqueness (if appropriate), format, etc
	// Returns normalized credential prefixed with an appropriate namespace prefix.
	PreCheck(cred string, params map[string]interface{}) (string, error)

	// Request sends a request for confirmation to the user. Returns true if it's a new credential,
	// false if it re-sent request for an existing unconfirmed credential.
	//   user: UID of the user making the request.
	//   cred: credential being validated, such as email or phone.
	//   lang: user's human language as repored in the session.
	//   resp: optional response if user already has it (i.e. captcha/recaptcha).
	//   tmpToken: temporary authentication token to include in the request.
	Request(user t.Uid, cred, lang, resp string, tmpToken []byte) (bool, error)

	// ResetSecret sends a message with instructions for resetting an authentication secret.
	//   cred: address to use for the message.
	//   scheme: authentication scheme being reset.
	//   lang: human language as reported in the session.
	//   tmpToken: temporary authentication token
	//   params: authentication params.
	ResetSecret(cred, scheme, lang string, tmpToken []byte, params map[string]interface{}) error

	// Check checks validity of user's response.
	// Returns the value of validated credential on success.
	Check(user t.Uid, resp string) (string, error)

	// Remove deletes or deactivates user's given value.
	Remove(user t.Uid, value string) error

	// Delete deletes user's record.
	Delete(user t.Uid) error
}

```

validate 패키지 내에 validator라는 파일이 존재했습니다. 이 애는 interface로 선언되어 있습니다. 즉, 다른 validator또한 올 수 있으니 인터페이스로 의존하도록 만든 것 같습니다.

그리고 validate폴더엔  email, tel폴더가 있고 그 안엔 validate.go라는 파일이 존재하지요. 이 파일들은 validator를 구현하고 있습니다.

![](https://postfiles.pstatic.net/MjAyMDA5MTdfMzMg/MDAxNjAwMzI4NzU2MDg5.uQl-u_DBjWUAaKhIn2gXfD9BsL4YbbAKDdeOaHwgxoMg.J0c1lS11vcgix8xYRGAflUziPq6leW6NNQfx5kZZg6og.PNG.study_ju/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2020-09-17_%EC%98%A4%ED%9B%84_4.45.53.png?type=w966)



#### 결론

1. 그래서 validator를 구현하여 우리가 원하는 validator 서비스를 만들고,
2. front단에서 해당 서비스 이름을 method에 넣어 호출하도록 하면 됩니다!



끝으로, tinode에서 제공하는 API문서를 첨부하며 마치도록 하겠습니다.





### Tinode validation API문서

---

### Credential Validation

Server may be optionally configured to require validation of certain credentials associated with the user accounts and authentication scheme. For instance, it's possible to require user to provide a unique email or a phone number, or to solve a captcha as a condition of account registration.

The server supports verification of email out of the box with just a configuration change. is mostly functional, verification of phone numbers is not functional because a commercial subscription is needed in order to be able to send text messages (SMS).

If certain credentials are required, then user must maintain them in validated state at all times. It means if a required credential has to be changed, the user must first add and validate the new credential and only then remove the old one.

Credentials are initially assigned at registration time by sending an `{acc}` message, added using `{set topic="me"}`, deleted using `{del topic="me"}`, and queries by `{get topic="me"}` messages. Credentials are verified by the client by sending either a `{login}` or an `{acc}` message.

---

