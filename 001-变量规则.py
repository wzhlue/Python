"""
要给 URL 添加变量部分，
你可以把这些特殊的字段标记为 <variable_name> ，
这个部分将会作为命名参数传递到你的函数。
规则可以用 <converter:variable_name>
指定一个可选的转换器。
"""
from  flask import Flask
app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s'%username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d'% post_id

if __name__ == '__main__':
    app.run()