Layered architecture

고민.

어느 부분에서 복잡한 로직을 구현해야 할까...(1이상이면 뭘 호출하고 ... 이런 복잡한 로직)

Controller엔 받을 parameter가 정해지므로, Service엔 어떤 인자를 입력하여 받을까?

Dao엔 어떤 인자를 넣어줄까? 어느정도 확장성을 가지게 만들까?!

service에서 Dao를 더 호출하여 Controller에 전달해줄까

service를 파편화 시키고 Controller에서 service를 더 호출할까?

복잡하다...



Controller



Service



Dao