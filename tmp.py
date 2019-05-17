import html_string as html
import bottle
from bottle import run, route
import sqlite3

@route('/todo')
def index():
    # html source code 틀
    str_top = html.make_string()
    str_bottom = html.make_string_end()
    str_todos = ""

    # sqlite3 데이터 읽어와서 todos 요소 추가     
    str_todos += html.new_todo(1,"할일 1111","내용111",0,"1996-11-04")
    str_todos += html.new_todo(2,"title2","content2",0,"0000-00-00")
    str_todos += html.new_todo(3,"title","content",1,"0000-01-15")
    str_todos += html.new_todo(4,"t","c",0,"2019-05-20")
    

    # source = final html source code
    source = str_top + str_todos + str_bottom

    return source


run(reloader=True, host='0.0.0.0', port = 8080)
