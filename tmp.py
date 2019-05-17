import html_string as html
import bottle
from bottle import run, route
import sqlite3

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

run(reloader=True, host='0.0.0.0', port = 8080)
