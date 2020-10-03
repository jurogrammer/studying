# Go 환경설정

### 1. Go 설치

#### 방법 1 home brew 이용

단순히 command창에 

``` shell
brew install go
```

하시면 됩니다. 그럼 설치 완료!



#### 방법 2 Go 홈페이지에서 다운 받기.

1. 아래 사이트에서 Download Go 클릭합니다.

https://golang.org/



2. 외부에서 다운받은 실행파일이기 때문에 다운 다운 파일을 contorl 클릭을 통해서 실행합니다. (외부 파일 권한 문제)

   

3. 설치끝!



### 2. Go 환경설정하기

참고 - https://niceman.tistory.com/128

GOPATH를 설정해주고 PATH에 등록해주는 과정입니다. 자바의 프로젝트 생성과 동일하다 보시면 됩니다.



1. 작업하고 싶은 폴더를 만들기

   전 `/Users/ju/Workspace/Go` 로 정하였습니다.

   

2. 해당 폴더에 3가지 폴더를 만들기

   * bin

     빌드한 실행파일이 보관되는 폴더입니다.

   * pkg

     프로젝트에 필요한 패키지가 컴파일 되어 라이브러리 파일이 저장되는 곳입니다.

   * src

     코드를 저장하는 폴더입니다.

3. 이 Go 작업 폴더를 환경설정해줍니다.

   각자 사용하는 shell에 다음을 작성해줍니다. 전 zshell을 사용하기에 ~/.zshell에 작성해줬습니다. 

   제가 등록한 위치대로 작성해보겠습니다.

   ```shell
   export GOPATH="/Users/ju/Workspace/Go"
   export PATH=$PATH:$GOPATH/bin
   ```

   첫 번째 줄의 의미는 GOPATH라는 변수를 위와 같이 정해준다는 뜻이고,

   두번째 줄의 의미는 기존의 PATH에($표시는 변수를 의미합니다.) $GOPATH/bin을 이어붙이고 ,
   PATH에 다시 집어넣어달라는 뜻입니다.

   * $GOPATH/bin을 풀어쓰면 /Users/ju/Workspace/Go/bin이 되겠지요



이렇게 하면 Go 환경설정은 끝납니다.! 

*참고로 **GOROOT**를 설정하라는 블로그 글도 있는데 설정 안해줘도 잘 돌아갑니다.. 전 설정했을 때 에러나서 해당 부분을 설명하지 않았습니다.*



다음은 Tinode 환경설정 및 빌드 방법을 알아보겠습니다.



# Tinode 환경설정

참고 - https://github.com/tinode/chat/blob/master/INSTALL.md 에서 Building from Source부분을 참고하시면 됩니다.



전 mysql을 기준으로 설명드리겠습니다.

여기서 할 작업들은 총 2가지입니다.

1. mysql에 Tinode 테이블 생성
2. Tinode build입니다.



순서는 참조링크를 따라가겠습니다.



### 1. Go를 설치합니다. (이는 위에서 설명했습니다.)



### 2. Mysql을 설치하고 실행합니다.

mysql.server start를 하시면 됩니다.



### 3. mysql버전으로 tinode서버를 빌드하고 db를 초기화 합니다.

```
go get -tags mysql github.com/tinode/chat/server && go build -tags mysql -o $GOPATH/bin/tinode github.com/tinode/chat/server

go get -tags mysql github.com/tinode/chat/tinode-db && go build -tags mysql -o $GOPATH/bin/init-db github.com/tinode/chat/tinode-db
```



여기서 이 문장의 의미를 살펴보겠습니다.

#### **첫번째 문단**

```
go get -tags mysql github.com/tinode/chat/server && go build -tags mysql -o $GOPATH/bin/tinode github.com/tinode/chat/server
```

1. ` go get -tags mysql github.com/tinode/chat/server` 

   go get은 go 패키지를 가져온다는 뜻입니다. 여기선 mysql 버전의 tinode서버를 github를 통해서 가져오고 있죠.

2. `go build -tags mysql -o $GOPATH/bin/tinode github.com/tinode/chat/server`

   mysql버전으로 github에서 가져온 고 파일을, 빌드하여, 빌드한 파일을 $GOPATH/bin/tinode 디렉토리에 저장한다는 의미입니다.

   따라서 깃허브에서 클론한 코드를 빌드하고 싶다면 끝에 있는 디렉토리 위치를 자신이 빌드하고 싶은 폴더의 위치로 바꿔주면 되겠지요!

   예를 들어서 아래처럼요. 이때 1번은 안쳐줘도 됩니다. 깃허브에서 가져온 소스를 빌드하는게 아니니까요.

   ```
   go build -tags mysql -o $GOPATH/bin/tinode /Users/ju/Workspace/Go/src/tinode/server
   ```



#### **두번째 문단**

```
go get -tags mysql github.com/tinode/chat/tinode-db && go build -tags mysql -o $GOPATH/bin/init-db github.com/tinode/chat/tinode-db
```

이 부분은 db를 초기화하기 위한 문장입니다. 즉, tinode를 위한 db를 생성하기 위한 부분이지요.  이것을 실행한다고 db가 초기화 되는 것이 아니라, 이 문장을 실행하면 **db를 초기화 실켜줄 수 있는 실행파일이 생성**됩니다.!

1. `go get -tags mysql github.com/tinode/chat/tinode-db`

   이건 뭐 앞서 보시듯이 생성시킬 소스코드를 가져오는 부분입니다.

2. `go build -tags mysql -o $GOPATH/bin/init-db github.com/tinode/chat/tinode-db`

   그 소스를 빌드해주는 것이죠.



### 4. DB 접속 정보를 설정해줍니다.

DB 설정정보는 다음 위치에 있습니다.

```
$GOPATH/src/github.com/tinode/chat/tinode-db/tinode.conf
```

이것을 편집기로 열어서 다음 부분을 찾습니다.

여기선 디렉토리 위치가 위와같이 되어 있지만 여러분이 앞서 받은 tinode설정파일 위치로 설정해주시면 됩니다.

제 예시로는 `/Users/ju/Workspace/Go/src/tinode/chat/tinode-db/tinode.conf`가 되겠지요.



```
	"mysql": {
		"dsn": "root@tcp(localhost)/tinode?parseTime=true",
		"database": "tinode"
	},
```

이 부분에서 dsn을 수정해주셔야 합니다. 간단히 예시로 설명하고 넘어가겠습니다.

root 계정에, 비밀번호를 1234, tcp프로토콜로, localhost에 접속하고 싶다면

```
"dsn": "root:1234@tcp(localhost)/tinode?parseTime=true",
```

이렇게 수정해주시면 됩니다.



### 5. DB Initializer를 실행합니다.

```
$GOPATH/bin/init-db -config=$GOPATH/src/github.com/tinode/chat/tinode-db/tinode.conf
```

위에서 설정한 파일을 바탕으로 db initiallizer를 실행하는 것입니다.

 실행파일이기 때문에 bin폴더에 있는 init-db를 명령어로 넣은 것이구요, 뒤는 -config에 config파일이 위치한 디렉토리를 작성해준 모습입니다.

위 명령어를 수행하면 DB가 생성됩니다.





### 6. 정적 파일을 다운받아 줍니다.

아마 요청에 대해 웹으로 대응해주기 위해서 이를 받아주는 것 같습니다. 또는 사진도 등록하구요. 그래서 이 파일들을 보관하고 싶은 디렉토리에

https://github.com/tinode/webapp/archive/master.zip

https://github.com/tinode/tinode-js/archive/master.zip

에서 받은 파일들을 압축을 풀어 그 폴더에 몰아넣어 줍시다.



### 7. DB를 실행해줍니다.

mysql.server start 명령어를 통해 실행해주시면 됩니다.



### 8. 대망의 시작!

```
$GOPATH/bin/tinode -config=$GOPATH/src/github.com/tinode/chat/server/tinode.conf -static_data=$HOME/tinode/webapp/
```

1. `$GOPATH/bin/tinode`

   이 부분은 빌드한 tinode를 실행해주는 것입니다.

2. `-config=$GOPATH/src/github.com/tinode/chat/server/tinode.conf`

   앞서 4번에서 설정한 tinode 설정파일로 실행한다는 것을 의미합니다. 앞서 말한대로 제 디렉토리는 `/Users/ju/Workspace/Go/src/tinode/chat/tinode-db/tinode.conf`  

   이렇게 되겠지요.

   

3. `-static_data=$HOME/tinode/webapp/`

   앞서 말한 정적 데이터 위치입니다.



이렇게 실행하면 6060포트로 접속하라는 글이 딱 뜰겁니다 ㅎㅎ 즐거운 개발하십쇼!