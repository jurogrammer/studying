# IPC(Interprocess Communication)

> 프로세스 간 통신 방법에 대하여 알아보자.



## 프로세스 간 통신이 필요한 이유

**1.Information sharing**

**2.Computation speed up**

**3.Modularity**

* 시스템의 기능을 나누어 개별 프로세스나 쓰레드로 모듈화하기 위해

**4.Conveience**

* 사용자가 많은 일을 동시에 수행하고 싶을 때 병렬적(parallel)으로 수행할 수 있는 편의 제공



## IPC의 방법의 종류

#### 1.shared memory

* 특정 메모리 공간을 프로세스가 공통으로 사용하는 방법

* 장점
  * message passing에 비해 빠름.
    * 공유 메모리 생성시에만 system call사용
* 단점
  * 충돌을 다뤄야 하므로 복잡해짐

#### 2.Message passing

* 두 프로세스간 message queue를 통해 메세지를 주고 받음으로써 통신
* 장점
  * 구현 간단
  * 충돌 고려 필요 없음
* 단점
  * 메세지를 주고 받을 때마다 system call을 쓰므로 느림.(하지만 최근 연구에선 shared memory의 경우 cache coherency issue때문에 message passing에 비해 느리다고 함)



## Shared-Memory Systems

#### 특징

1.공유된 메모리주소는 프로세스의 메모리주소에 속하게 된다. 

* 일반적으로 프로세스간 메모리 주소는 구분 짓는다. 즉, 통신하려는 프로세스간에는 이 제약을 없애야 함.

2.데이터의 형태나 위치는 프로세스에 의해 결정된다.

* 즉, OS 관할하에 있지 않음.

3.프로세스가 synchronization문제를 책임 진다.

* 프로그래머가 위를 고려하여 작성해주어야 한다는 뜻.



## Message-Passing Systems

#### 특징

1.OS가 제공한 meessage-passing facility는 프로세스간 통신 및 synchronization 문제를 고려할 필요가 없는 메카니즘을 제공해줌.

2.distributed 환경에 용이

* 즉, 네트워크에 의해 연결되어 있는 서로 다른 컴퓨터끼리 통신할 때 유용하다
  * Internet chat program.

3.message-passing facility는 적어도 두가지 operation 제공

* send(message)
* receive(message)

* 이때, message는 가변적일 수 있는데 이를 다루기 위해선 system-level에서 구현이 매우 복잡해진다. 하지만 **programming은 매우 간단해짐!**

4.프로세스 P,Q가 서로 통신하기 위해선 **communication link**가 반드시 존재해야 한다.

* 이 communication link는 다양한 방법으로 물리적으로 구현될 수 있음.
  * shared memory, hardware bus, network 등등
* 하지만 물리적 구현은 OS가 알아서 해주기 때문에 우리는 **logical 구현에 대해 관심가지면 됨**.

5.논리적 구현에 대한 몇가지 방법

* Direct or indirect communication(naming)
* Synchronous or asynchronous communication()
* Automatic or explicit buffering



### Naming

프로세스가 통신하려면 반드시 서로를 언급할 수단이 필요함.(즉, 특정 프로세스를 한정 지을 수 있어야 함.) 이럴 때 direct or indirect 통신 방법이 존재

#### direct communication

* 정의

  통신할 프로세스들은 서로의 이름에 대해 명확히 알아야 한다.(sender, recipient 모두)

*  send, receive 형태

  이러한 배경으로 send와 recevie는 다음과 같은 파라미터 필요

  send(P,message) ,receive(Q,message)

* 특징

  1. 통신을 원하는 두 프로세스간 이 link는 자동적으로 생성됨
  2. link는 정확히! 두 프로세스와 연관되어 있음
  3. 다시 말해, 두 프로세스간에는 정확히 하나의 링크만 존재함.
  4. 2,3을 일컬어 symmetry in addressing이라 함. 즉 1:1 매칭
     - 반면 asymmetry in adreesing이라 함은 sender만 프로세스 이름 알고 receiver는 모름
     - sender (P,message), receive(id, message) 형태
       - 여기서 id는 통신이 발생하는 프로세스 set을 말함.

* 단점

  1.프로세스를 특정하기 때문에 모듈성이 떨어지게 된다.

  pid를 바꾸면 새로 바뀐 pid를 찾기 위해 old id를 모두 찾을 수 밖에 없음. 

#### Indirect communication

* 정의

  통신 프로세스들이 **메일박스**나 **포트**를 통해 메세지를 주고 받는다.

  * 이때 message를 넣거나 뺄 수 있는 obj를 의미함.(ex POSIX message queues)
  * 각 메일박스는 고유 id를 가진다.

* send receive 형태

  send(A, message)

  receive(A, message)

  이때 A는 메일박스를 의미한다.

* 특징

  	1. 공유된 메일박스를 가지고 있어야 두 프로세스간 링크가 성립(established)된다
   	2. link는 두 프로세스 이상과 관련되어 있을 수 있다.(즉, 한 메일박스는 2개 이상의 프로세스가 통신하기 위해 존재한다.)
   	3. 두 프로세스가 통신하기 위해 하나 이상의 메일박스를 이용할 수 있다.

 * 한 메일 박스에 3개 이상의 프로세스가 접근을 허용함으로써 생긴 문제

   ```
   P1,P2,P3가 있을 때 P1이 메일박스에 메세지를 넣었고, 이때 둘 다 P2,P3가 receive(A,)를 실행했다면 누가 메세지를 받을 것인가?
   ```

   이 답은 어떤 방법을 선택할 것이냐에 따라 결과가 달라진다.

   1. link(메일박스)에 2개 프로세스만 연관되도록 한다.
   2. 한 번에 1프로세스만 receive()를 허용한다.
   3. the system이 어떤 프로세스가 선택하게 할 것인지 결정한다. 이때 누가 선택할 것인지 알고리즘을 정해야하고 system이 sender에 대한 receiver를 확인할(identify) 수 있어야 한다.

* mailbox 소유자(즉, mailbox가 누구의 memory address에 속하는가.)

  * process

    * 프로세스 통신간 mailbox의 소유자를 알 수 있으므로(고유의 mailbox를 소유하므로) 혼동이 없음.
    * 하지만 프로세스가 삭제될 때 메일박스도 삭제되므로 메일박스가 삭제되었는지 알림 받아야함

  * operating system

    * 독립적으로 존재하게 된다. 즉, 어떤 프로세스에게도 특정하게 attach되지 않음.

    * 이에 따라 os는 반드시 다음과 같은 절차를 밟도록 해야 한다.

      ```
      1. Create a new mailbox.
      2.Send and receive messages through the mailbox.
      3.Delete a mailbox.
      ```

    * 새로운 메일박스를 만든 프로세스가 메일박스의 default 소유자가 된다.(초기값)

    * 하지만, ownership과 메세지를 받는 권한은 적절한 시스템 콜을 통해 다른 프로세스에게 전달될 수 있다.(이를 통해 각 메일 박스에 다중 receiver가 존재할 수 있게 됨.)

#### Synchronization

메세지를 읽는 중에 데이터가 업데이트될 수 있음. 따라서 synchronization문제 발생. 이를 위한 send,receive 방식

* Blocking send
  * receiving process 나 mailbox가 데이터를 받는 중에는 sending process가 block 됨
* Nonblocking send
* Blocking receive
  * message를 읽을 수 있을 때 까지(available) recevier가 block 됨
* Nonblocking receive

blocking send()와 receive()를 통해 생산자-소비자 문제 해결 가능.

* 생산자가 blocking send()를 사용하면 receiver와 mailbox에 도착할 때까지 대기 상태가 됨.
* 소비자는 receive()를 쓰더라도 blocking send()에 의해 block됨. 이용가능하면 그때 block해제하여 읽을 수 있음



#### Buffering

direct or indirect로 사용하든 메세지는 프로세스에 있는 임시 queue와 통신함.(즉 프로세스에 temporary queue가 반드시 존재) 이를 buffer라 부름

* buffer 구현 3가지 방식

  1. Zero capacity(버퍼가 없음)

     큐의 길이가 0인 것. 즉, 어떤 메세지도 큐에 없음. 이에 따라 sender는 block됨.(block이유는 아래보면 명확.  메세지를 보낼 수 있는 상태가 아니기 때문에.(꽉찼다))

  2. Bounded capacity

     큐의 길이(n)가 유한한 것.  따라서 최대 n개의 메시지를 큐에 넣어 둘 수 있음. sender가 메세지를 보낼 때 큐가 비어 있으면 queue에 메세지를 두게 됨. 그리고 sender는 기다리지 않고 데이터를 보낼 수 있게 된다.

     그런데 유한하기 때문에, link가 꽉차면 sender는 반드시 block처리 되어야 함. (빈공간이 날 때까지)

  3. Unbounded capacity

     무한하기 때문에 sender는 block될 일이 없음.



## 구현 예

### POSIX (Shared Memory)

memory mapped files, shared memory 형식.

1. shared-memory object를 생성한다.

   ```
   shm_fd = shm_open(name, O_CREAT|O_RDRW,0666);
   ```

   name : shared-memory object의 이름

   O_CREAT : 해당 name이 존재하지 않으면 생성

   O_RDRW : reading/writing을 위해 열음

   0666 : directory permissions

   return : integer file descriptor

2. shared-memory object 크기 결정

   ```
   ftruncate(shm_fd,4096);
   ```

   4096 : size를 4096byte로 결정

3. shared-memory object를 가진 memory-mapped file 생성. 

   ```
   mmap(0,size,PROT_WRITE,MAP_SHARED,shm_fd,0);
   ```

   return : shared-memory object에 접근하기 위한 pointer 반환.

synchronization 문제를 해결하기 위해 producer-consumer model 이용

### Mach (Message passing)

message passing 방식. 여기는 system call 조차 message로 이뤄짐.

#### 특징

* task가 생성될 때 Kernel mailbox와 Notify mailbox가 생성 됨.
  * Kernel mailbox : Kernel(The kernel)이 task과 통신하기 위해 사용 
  * Notify mailbox : kernel이 이벤트 발생을 알려주기 위해 사용

* 메세지를 전달하기 위해 3개의 시스템 콜만 이용

  * ```
    msg_send()
    ```

    메일박스에 메세지 보냄

  * ```
    msg_receive()
    ```

    메일박스에서 메세지 받음

  * ```
    msg_rpc()
    ```

    remote procedure calls가 실행됨

    * RPCs는 메세지를 보내고 정확히 하나의 메시지를 기다림.
    * 이로 인해 subroutine procedure call이지만 시스템 사이에 작동함. (remote 어원)

  * ```
    port_allocate()
    ```

    새로운 메일박스를 생성하고 메세지 큐에 공간할당함.

    만든 프로세스가 이 메일박스의 주인임

    오직 한 프로세스만 소유자이고 읽을 수 있음.

    하지만 이 권한을 다른 프로세스에게 전달 가능.

  * 





### Windows



## Communication in Client-Server Systems

endpoint가 통신하기 위한 수단.

두 endpoint는 서로의 socket을 통해 통신하게 된다.

보통 1024이하의 port번호는 유명한 서비스를 제공하기 위한 포트로 사용됨. 예를 들어 80번은 웹서비스.

소켓은 ip와 port번호를 통해서 unique하게 되고 이를 통해 통신함.

따라서 127.0.0.1:8080 이게 소켓이라 보면 됨.(http:ip:port 가 소켓...)

