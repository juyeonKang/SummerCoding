# SummerCoding_TODO list 만들기
### TEST용 개인 서버
> 13.124.39.205:8080/todo

### 작업환경
1. python 3.7.2 (_개발언어)  
2. sqlite3 (python3.7.2 내장_db)   
3. bottle (python module_웹 프레임워크)   

### 설치 방법
1. bottle 설치   
`$ sudo apt-get install python3-bottle`   
2. 해당 git 복사 (필요한 경우 git 설치)   
`$ git clone https://github.com/juyeonKang/SummerCoding.git`   
3. init_db.py 실행 (SummerCoding 폴더로 이동한 후)   
`$ cd SummerCoding`   
`$ chmod u+x init_db.py`   
`$ ./init_db.py`   
4. run_todolist.py 실행   
`$ chmod u+x run_todolist.py`    
`$ nohup ./run_todolist.py &`   
  
------
### 한계점
- apache 등 부하관리 기능을 가진 웹 프레임워크와 연동X   
- 로그인 기능X (사용자별 DB구현이 아닌 todo list 기능을 보여주는 테스트 페이지)   
- 브라우저의 캐시를 이용해서 특정 기간은 로그인을 하지 않아도 되는 환경을 구성하고 싶었으나 로그인 기능이 없어 역시 구현하지 못함
