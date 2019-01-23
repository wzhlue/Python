"""
1.导入Flask类所在的模块
2.创建对象,可以传递参数
3.通过路由路径绑定视图函数
4.启动应用该程序
"""
from flask import Flask

# static_url_path 静态资源路径
# static_folder 静态资源文件夹名称  默认是“static
# template_folder 模板资源文件夹 默认“templates”

# __name__是程序启动的模块
app = Flask(__name__)

@app.route("/")
def test():
    return "使我痛苦者必使我强大！"

if __name__ =='__main__':
    app.run()