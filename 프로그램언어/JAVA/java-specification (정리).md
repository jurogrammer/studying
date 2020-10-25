* 모르는 단어

  97p `strictfp`

* 기본 자료형의 축소형변환

  이해하려면 1시간 넘게 소비해야할 듯.



* interface type J to any non-parameterized interface c that is not final (85p)
* boxing 형변환
* 캡쳐형변환 이해하기





#### 2가지 버그를 수정합니다.
* 날짜에서 Month의 값이 1작게 출력되는 현상
* 가입했음에도 불구하고 가입 히스토리가 없는 경우 에러 처리
  * 가입여부는 ssmMember테이블의 sinsang_pay_join 컬럼을 참조하고,
  * 가입 히스토리는 ssm_sinsang_pay_join_history 테이블을 참조합니다.





쿼리속도 개선

1. 포인트 코드 검색할 때 조인하지 말고 포인트코드에서 해당 값만 불러와. 
   * 왜냐하면 어차피 1개임
2. 포인트 코드 검색할 땐 구분이 필요없으므로 구분 선택을 숨겨버려! 캡슐화





읽어볼 글

1. table join만드는건 mapping table만드는 거였는지 확인







1. params permit

2. get_page_info

   