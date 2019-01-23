"""
abort(代号):主动抛出异常异常代号信息
raise(异常对象)
会配合@app.errorhandler(代号/对象)使用,做自定义错误页面的提示
400 - 错误的请求。
403 - 禁止访问
404 - 未找到。 ·404.0 -（无） – 没有找到文件或目录
HTTP 500 - 内部服务器错误
HTTP 400 - 请求无效
"""
from  flask import Flask

app = Flask(__name__)
@app.route("/")
def test():
    # 程序一旦抛出异常，下面的代码会终止执行
    # abort(404)
    #raise (Exception("异常来了!"))
    return "千里之行始于足下"

@app.errorhandler(Exception)
def errorhandler_403(e):
    return "你的权限不够，禁止访问该方法"


if __name__ == '__main__':
    app.run()