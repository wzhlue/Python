"""
1.如果一个路由绑定多个视图函数,那么优先访问的是谁?
优先访问的是先装饰的

2.如果多个路由绑定一个视图函数,通过哪些路径可以访问到该视图函数
通过所有的路径都可以访问
"""
from flask import Flask

app = Flask(__name__)

@app.route("/wzh")
@app.route("/quyuan")


def test():
    return "天生我材必有用"

@app.route("/wzh")
@app.route("/wang")
def test2():
    return "千金散尽还复来"

if __name__ =='__main__':
    app.run()