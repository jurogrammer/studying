# Methods Common to All Objects

Object가 아무리 concrete class더라도 상속을 염두해두고 만들었습니다.

그리고 objects의 equals, hashCode, toString, clone 그리고 finalize method는 오버라이딩을 염두해두고 만들었죠. (이하 nonfinal method)따라서 이 메서드들은 규약이 정해져 있습니다.

이를 지키지 않으면 다양한 자바 라이브러리에서 문제를 일으키죠.

이번 챕터에서는 언제, 그리고 어떻게 nonfinal method들을 사용하는지에 대해 말씀드리겠습니다.

