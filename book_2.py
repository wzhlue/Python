from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
#关闭csrf验证
# app.config["WTF_CSRF_ENABLED"] = Flase

app.config["SECRET_KEY"] = "jfdkfjkdjfd"

#数据库配置信息
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost:3306/book"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#创建对象,关联app SQLAlchemy是一个扩展包用来，负责Python语言和mysql数据库交互
db = SQLAlchemy(app)

#创建模型类
#作者(一方)
class Author(db.Model):
    #指定数据库名称
    __tablename__ = "authors"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True,nullable=False)

    #关系属性,backref
    books = db.relationship("Book",backref="author",lazy="dynamic")

#书籍(多方)
class Book(db.Model):
    # 指定数据库名称
    __tablename__ = "books"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True,nullable=False)

    #外键关系
    author_id = db.Column(db.Integer,db.ForeignKey(Author.id))

#定义表单类,继承自FlaskForm
class BookForm(FlaskForm):
    author_name = StringField('作者',validators=[DataRequired('需要填写')])
    book_name = StringField('书名',validators=[DataRequired('需要填写')])
    submit = SubmitField('添加')


# 显示页面, 添加书籍
@app.route('/', methods=["GET","POST"])
def show():

    #创建表单
    form = BookForm()

    #获取数据
    author_name = form.author_name.data
    book_name = form.book_name.data

    #验证是否符合标准
    if form.validate_on_submit():

        #取出作者对象
        author = Author.query.filter(Author.name == author_name).first()

        #判断作者是否存在
        if author:

            #获取书籍对象
            book = Book.query.filter(Book.name == book_name,Book.author_id == author.id).first()

            #判断书籍是否存在
            if book:
                flash('该作者, 已经有这本书')

            else:
                #创建书籍对象
                book = Book(name=book_name)
                book.author_id = author.id

                #添加到数据库
                db.session.add(book)
                db.session.commit()

        else:
            #创建作者对象,并保存到数据库
            author = Author(name=author_name)
            db.session.add(author)
            db.session.commit()

            #创建书籍对象,并保存到数据库
            book = Book(name = book_name)
            book.author_id = author.id
            db.session.add(book)
            db.session.commit()

    #查询数据
    authors = Author.query.all()

    #渲染数据到前端页面
    return render_template('file01library.html',form=form,authors = authors)

# 删除书籍
@app.route('/delete_book/<int:id>')
def delete_book(id):

    #1.通过编号取出书籍
    book = Book.query.get(id)

    #2.删除书籍
    db.session.delete(book)

    #3.提交到数据库
    db.session.commit()

    #4.显示页面
    return redirect(url_for('show'))

#删除作者
@app.route('/delete_author/<int:id>')
def delete_author(id):

    #1.通过编号取出作者
    author = Author.query.get(id)

    #2.遍历删除书籍
    for book in author.books:
        db.session.delete(book)

    #3.删除作者
    db.session.delete(author)

    #4.提交到数据库
    db.session.commit()

    #5.显示页面
    return redirect(url_for('show'))

if __name__ == '__main__':

    #为了演示方便,先删除表
    db.drop_all()

    #创建表
    db.create_all()


    #添加测试数据
    au1 = Author(name='老王')
    au2 = Author(name='老尹')
    au3 = Author(name='老刘')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()

    bk1 = Book(name='老王回忆录', author_id=au1.id)
    bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    bk3 = Book(name='get_flashed_messages', author_id=au2.id)
    bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()

    app.run(debug=True)


