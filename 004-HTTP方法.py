# HTTP （web 应用会话的协议）
# 知道访问 URL 的不同方法。默认情况下，
# 路由只回应 GET 请求，但是通过给 route()
# 装饰器提供 methods 参数可以更改这个行为。

from flask import Flask, request

app = Flask(__name__)


def do_the_login():
    return "do_the_login()"
    #pass

def show_the_login_form():
    return "show_the_login_form()"
    #pass

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        do_the_login()
    else:
        show_the_login_form()

if __name__ == '__main__':
    app.run(debug=True)