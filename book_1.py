from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 设置配置信息
# 数据库的链接地址,<协议>://<用户名>:<密码>@<IP地址>:<端口>/数据库名字
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/book"
# 设置数据库追踪信息, 并压制警告
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 创建SQLAlchemy对象,关联app
db = SQLAlchemy(app)


# 编写类,继承db.Model
# 角色模型(一方)
class Role(db.Model):
    __tablename__ = "roles"  # 指定数据库表名字

    # 主键,整数类型
    id = db.Column(db.Integer, primary_key=True)
    # 设置名字,字符串类型,唯一,不能为空
    name = db.Column(db.String(64), unique=True, nullable=False)

    # 为了方便的看到该类身上的属性
    def __repr__(self):
        return "<Role:%s>" % self.name


# 用户模型(多方)
class User(db.Model):
    __tablename__ = "users"  # 指定数据库表名字
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    # 外键,引用Role中的id
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))

    # 为了方便的看到该类身上的属性
    def __repr__(self):
        return "<User:%s>" % self.name


@app.route('/')
def hello_world():
    return "helloworld"


if __name__ == '__main__':
    # 删除的是继承自db.Model类所对应的表
    db.drop_all()

    # 创建的是继承自db.Model类所对应的表
    db.create_all()

    app.run(debug=True)