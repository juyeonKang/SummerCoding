import html_string as html
import bottle
from bottle import run, route, request, post
import sqlite3
import datetime

@route('/todo')
def index():
    # html source code 틀
    str_top = html.todo_top()
    str_bottom = html.todo_bottom()
    str_todos = ""

    # sqlite3 데이터 읽어와서 todos 요소 추가
    conn = sqlite3.connect("testDB.db")
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM todo ORDER BY done ASC, ordernum ASC, duedate ASC")
        rows = c.fetchall()
        for data in rows:
            str_todos += html.new_todo(data)

    # source = final html source code
    source = str_top + str_todos + str_bottom

    return source

@route('/todo_dead')
def index():
    # /todo 에서 deadline 알람을 누르면 해당 페이지로 이동,
    # duedate 비교해서 초과한 것 출력,
    # dead는 check 누르면 display none으로 변경

    str_top = html.dead_top()
    str_bottom = html.todo_bottom()
    str_dead_todos = ""

    # 현재 날짜 확인
    now = datetime.datetime.now()
    nowDate = now.strftime("%Y-%m-%d")

    # SELECT문장 생성
    select_cmd = "SELECT * FROM todo WHERE done==0 AND duedate < '%s' ORDER BY duedate ASC"%nowDate
        
    conn = sqlite3.connect("testDB.db")
    with conn:
        c = conn.cursor()
        c.execute(select_cmd)
        rows = c.fetchall()
        for data in rows:
            str_dead_todos += html.dead_todo(data)

    source = str_top + str_dead_todos + str_bottom
    
    return source

@route('/todo_add')
def index():
    # /todo 에서 + 누르면 해당 페이지로 이동, todo 추가
    return "hello"

@route('/check', method='POST')
def index():
    idx = int(request.body.read().decode().split("-")[0])
    update_cmd = "UPDATE todo SET done=CASE WHEN done=1 THEN 0 ELSE 1 END WHERE idx=%d"%idx

    conn = sqlite3.connect("testDB.db")
    with conn:
        c = conn.cursor()
        c.execute(update_cmd)
        conn.commit()
        
    return 0

run(reloader=True, host='0.0.0.0', port = 8080)
