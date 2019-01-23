"""
后台向客户端(浏览器,手机app,iPad,电子设备)返回数据的时候,往往都需要指定数据格式 json
有两种方式指定json格式:
1. jsonify(dict)
2. json.dumps(dict),需要配合response,设置Content-Type
"""
from flask import Flask, jsonify

app = Flask(__name__)
@app.route("/")
def desc():
    wzh = {
        "name":"xiaozhang",
        "age":18
    }
    #return jsonify(name="xiaowang",age=18)
    return jsonify(wzh)

if __name__ == '__main__':
    app.run()