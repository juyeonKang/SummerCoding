import html_string as html
import bottle
from bottle import run, route, request, post, static_file
import sqlite3
import datetime

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath,root="./") 

@route('/get_init')
def get_init():
    # 현재 날짜 확인
    now = datetime.datetime.now()
    nowDate = now.strftime("%Y-%m-%d")
    ch_cmd = "SELECT EXISTS (SELECT * FROM todo WHERE duedate < '%s' AND duedate !='');"%nowDate

    conn = sqlite3.connect("testDB.db")
    with conn:
        c = conn.cursor()
        c.execute("SELECT MAX(idx) FROM todo")
        idx = c.fetchall()[0][0]
        c.execute(ch_cmd)
        check = c.fetchall()[0][0]
        #print(idx)
        #print(check)
        
    return {"idx":idx, "noti":check}

@route('/todo')
def todo():
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
def todo_dead():
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
def todo_add():
    # /todo 에서 + 누르면 해당 페이지로 이동, todo 추가
    return "hello"

@route('/check', method='POST')
def check():
    idx = int(request.body.read().decode().split("-")[0])
    update_cmd = "UPDATE todo SET done=CASE WHEN done=1 THEN 0 ELSE 1 END WHERE idx=%d"%idx

    conn = sqlite3.connect("testDB.db")
    with conn:
        c = conn.cursor()
        c.execute(update_cmd)
        conn.commit()
        
    return 0

@route('/add', method="POST")
def add():   
    data = request.body.read().decode().split(",")
    #print(data)
    idx = data[0]
    title = data[1]
    content = data[2]
    duedate = data[3]
    ordernum = data[4]
    insert_cmd = "INSERT INTO todo VALUES (%s, '%s', '%s', 0, '%s', %s)"%(idx,title,content,duedate,ordernum)

    conn = sqlite3.connect("testDB.db")
    with conn:
       c = conn.cursor()
       c.execute(insert_cmd)
       conn.commit()
       
    return 0

@route('/delete', method='POST')
def delete():
    data = request.body.read().decode()
    del_cmd = "DELETE FROM todo WHERE idx = %s"%data
    conn = sqlite3.connect("testDB.db")
    with conn:
        c = conn.cursor()
        c.execute(del_cmd)
        conn.commit()

    return 0

run(reloader=True, host='0.0.0.0', port = 8080)
