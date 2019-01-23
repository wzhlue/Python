"""
url_map:可以查看当前的应用程序app中已经绑定了哪些视图函数和路由之间的映射关系
格式: app.url_map返回的是一个map集合

"""
from flask import Flask

app = Flask(__name__)
@app.route('/wzh')
def test():
    return "使我痛苦者，必使我强大！"

if __name__ =='__main__':
    print(app.url_map)
    #Map([ < Rule
    # '/wzh'(OPTIONS, HEAD, GET) -> test >,
    # < Rule
    # '/static/<filename>'(OPTIONS, HEAD, GET) -> static >])
    app.run()
