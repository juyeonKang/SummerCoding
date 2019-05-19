import sys, os, sqlite3

if not os.path.isfile("./testDB.db"):
    conn = sqlite3.connect("testDB.db")
    with conn:
        c = conn.cursor()
        c.execute("CREATE TABLE todo (idx integer, title text, content text, done integer, duedate text, ordernum integer default -1)")
        data = (
            (0, "to do list TEST_title (click)", "to do list TEST_content", 0, '2019-05-18'),
            (1, "안녕하세요!", "만나서 반가워요", 0, '2019-05-19'),
            (2, "+ 버튼을 눌러서 항목을 추가할 수 있어요! :D", "title과 content는 꼭 입력해주세요<br>제목은 30자 이내로 작성해주세요!<br>content 창에서는 &lt;br&gt; 태그를 써서 줄바꿈을 할 수 있어요", 0, '2019-05-20'),
            (3, "마감기한은 선택사항이에요,", "단, 오늘 이전의 날짜는 선택할 수 없어요", 0, '2019-05-21'),
            (4, "물론 제목과 내용은 수정이 가능하답니다 (click)", "content가 표시되는 부분 오른쪽의 아이콘을 눌러보세요", 0, '2019-05-22'),
            (5, "title 앞의 체크박스와 화살표 용도는 너무 분명하죠?", "완료 여부는 체크박스로, 항목의 순서는 화살표로!",0, '2019-05-23'),
            (6, "중요한 할 일을 위쪽에 놓아보세요","항목 추가시 기본 정렬 기준은 완료 여부와 마감기한이랍니다", 0, '2019-05-24'),
            (7, "마감기한이 지난 항목이 있으면 아이콘이 나타나요", "아이콘을 누르면 마감기한이 지난 항목만 표시된답니다", 0, '2019-05-25'),
            (8, "오른쪽의 x를 누르면 항목을 삭제할 수 있어요", "삭제한 항목은 취소할 수 없으니 조심하세요!", 0, '2019-05-26'),
            (9, "항목을 추가하면 자동으로 새로고침이 되지만", "완료여부 수정시에는 새로고침이 안돼요",0,'2019-05-27'),
            (10, "완료된 항목은 이렇게 표시된답니다","완료된 항목 표시",1, '2019-05-28'),
            (11, "마감기한이 설정되지 않은 항목은 이렇게 표시된답니다", "마감기한 없는 항목 표시", 0, '')
        )
        cmd = "INSERT INTO todo(idx, title, content, done, duedate) VALUES (?,?,?,?,?)"
        c.executemany(cmd,data)
        conn.commit()

