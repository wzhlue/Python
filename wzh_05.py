#coding:utf8
"""
redirect:重定向,自定定位到另外的资源
格式:redirect('路径'), 内部的默认状态码是302

注意:使用url_for传递参数,接收方需要与传递方完全一致
"""
from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route("/taobao")
def aredirect():
    return redirect(url_for("jingdong",num=100))#加上参数需要使用url_for

@app.route("/jingdong/<int:num>")
def jingdong(num):
    return "欢迎来到京东%d"%num


if __name__ == '__main__':
    app.run()