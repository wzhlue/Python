#coding:utf8
"""
url_for():是flask中提供的一个方法
作用:可以通过视图函数的名称找到对应的路径
格式: url_for('视图函数',key=value)
场景: 一般用户服务器内部资源定位
导入包的快捷键:alt +enter
"""
from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/')
def test():
    print (url_for('wzh'))
    return "我不会技术，找<a href ='/wzh'>千峰</a>"%(url_for('wzh'))

@app.route('/wzh')
def wzh():
    return "来千峰，你不会后悔，只要你努力"

if __name__ == '__main__':
    app.run()