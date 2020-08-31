# 출처

* https://datatables.net/

  

# 개요

회사에서 데이터 테이블을 이용하여 view를 꾸미고 있습니다. 백엔드에서 화면을 모두 꾸미진 않더라도 ajax하고, 받아온 데이터에 알맞게 적용시키는 코드는 작성해 주어야 합니다. 따라서 이 라이브러리에 익숙해지기 위해 토이 프로젝트를 진행했습니다. 그래서 익힌 내용들을 정리하고 알려드리고자 이 글을 작성해봅니다.



# 사용방법



## 1. DataTable 초기화

```html
<table id = "age-table">
  <thead>
    <tr>
      <th>
        name
      </th>
    <th>
      	age
      </th>
     </tr>
  </thead>
  <tbody>
  	<tr>
    	<td>hong</td>
      <td>20</td>
    </tr>
    <tr>
    	<td>gil</td>
      <td>10</td>
    </tr>
  </tbody>
</table>  

```





1. 데이터 테이블을 적용하려면, 적용하고 싶은 테이블 태그를 찾아서 아래와 같이 작성해주면 됩니다.

```javascript
$('#age-table').DataTable();
```



2. ajax 등 옵션을 적용하기 위해선, DataTable 메서드의 input으로 아래와 같이 literal object를 작성해주시면 됩니다.

```javascript
$('#age-table').DataTable({
    serverSide: true,
	ajax: ~~~~,
    cols: ~~~~,
})
```



이와 같은 뼈대로 DataTable의 선언 및 옵션을 적용할 수 있습니다! 그럼 다음으로는 DataTable의 기본 작동 순서에 대해 말씀드리겠습니다.



## 2. DataTable 작동순서

작동 환경은 다음을 가정합니다.

1. API 서버
2. Client에서 테이블 생성에 필요한 데이터를 API 서버에 요청
3. table은 paging을 적용
4. 검색 창 :` <div id = "question"></div>` 
5. 조건 부분: `<div id = "condition"></div>` ex:)나이, 연령 선택칸



위와 같은 환경에서 DataTable은 다음과 같은 순서로 작동합니다.

1. API서버에 ajax 요청 (초기 렌더링시)
2. ajax요청 후 받은 데이터를 순서대로 출력
3. 테이블 값 변화가 필요한 경우, reload를 통해 데이터 재요청을 합니다.



이 과정을 구현하기 위해서 다음을 고려하셔야 합니다.

1. DataTable이 API서버에 요청시, **어떤 parameter를 담아야 하는지**
2. API서버는 **어떤 parameter를 보내야 하는지**

3. DataTable에서 위를 구현하기 위한 **옵션**



앞으로 위 고려사항을 중심으로 설명드리도록 하겠습니다. 그리고  여러 상황에 대응할 수 있도록 좀 더 일반적인 dataTable 옵션을 작성하겠습니다. 따라서 다른 분들과 설명 상 차이가 있음을 알아주세요~



## 3. DataTable 구현

### 1. DataTable의 옵션들

```javascript
$('#age-table').DataTable({
    serverSide: true,
    pageLength: 25,
    ajax: {
        url: "http://localhost:3000/users",
        type:"GET",
        data: function(d) {
    		d.question = $("#question").val()
    		d.condition = "name"
		},
        dataSrc: function (response) {
            recordsTotal = response.recordsTotal
            recordsFiltered = response.recordsFiltered
            return response.users
		}
	},
    
    columns: [
        {data: "name"},
        {data: "age",
         render: function(data, type, row){
             return "<span id = \"row-age\"> age </span>"
         }
        }
    ]
    
})
```



이 옵션들이면 이 정도면 어지간한 작업들은 다 할 수 있지 않을까 합니다.

그럼 옵션 의미들을 살펴보겠습니다.

1. serverSide

   dataTable은 default로 client-side에서 테이블 작업을 하도록 되어있습니다. 하지만 저흰 API서버를 이용하는 것을 가정했기 때문에 해당 옵션을 true로 설정해주셔야 합니다. true로 설정해주었을 때 테이블 조작에 필요한 parameter(몇 번째 값부터 몇개씩 등...) 를 담아서 request보낼 수 있기 때문입니다. 반대로 client-side였다면 테이블 나열에 필요한 데이터만 가져오면 되므로 ajax시 해당 옵션을 굳이 넣어줄 필요는 없겠죠.

   

   따라서 `serverSide: true`로 작성해주시기 바랍니다.

2. ajax

   dataTable을 채울 데이터들을 요청하는 부분입니다. dataTable 사이트에서 설명하길 jqeury의 ajax를 그대로 사용한답니다.

   * url

     data 요청 endpoint url주소입니다.

   * type

     request시 method를 의미합니다.

   * data

     이건 ajax.data와 동일하게 작동합니다. 이게 스칼라 값이냐 function(or json)이냐에 따라 의미가 달라지는데, function일 경우에 한해서 설명드리겠습니다.  function일 경우엔 **request 파라미터를 넣어줄 수 있는 옵션**이 됩니다. 따라서 위의 경우엔 d라는 input에 추가하고 싶은 파라미터 명 및 값을 대입해주면 됩니다.

     `d.파라미터명 = 값`

     그런데  function대신 json을 넣어줄 수도 있습니다.

     ```json
     {
         question: $("#question").val(),
         condition: "name"
     }
     ```

     처럼 말이죠. 하지만 이 두 방법엔 명백한 차이가 있습니다.

     function으로 작성해주었을 경우엔 ajax를 재사용했을 때 값을 재평가 합니다. 즉, $("question").val()을 다시 실행하는 거죠.

     하지만 json을 적용할 경우엔 처음 $("question").val()값만이 적용됩니다. 아무리 검색어를 바꾼다 한들 일정하니 검색을 구현할 땐 json을 이용하면 안되겠죠.

   * dataSrc

     