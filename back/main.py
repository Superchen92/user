from flask import Flask, jsonify, request
from flask_cors import CORS,cross_origin
import db

app = Flask(__name__)
CORS(app, resources=r"/*")
app.static_folder = 'dist'
app.static_url_path = '/dist'
@app.route('/')
def index():
    return "Hello World!"


@app.route("/get_user_list", methods=['GET'])
def getUerList():
    users = db.session.query(db.User).order_by(db.User.id).all()
    user_list = []
    for user in users:
        user_dict = {'id': user.id, 'name': user.name, 'gender': user.gender}
        print(user_dict)
        user_list.append(user_dict)
    
    result = {'status': 200, 'data': user_list}
    return jsonify(result)

@app.route("/add_user", methods=['POST'])
def addUser():
    if request.method == 'POST':
        data = request.get_json()
        user = db.User(name=data['name'], gender=data['gender'])
        db.session.add(user)
        db.session.commit()
    return {'message': '新增用户成功'}

@app.route("/edit_user", methods=['PUT'])
def editUser():
    if request.method == 'PUT':
        data = request.get_json()
        user = db.session.query(db.User).filter_by(id=data['id']).first()
        if user is not None:
            user.name = data['name']
            user.gender = data['gender']
            db.session.commit()
            return {'status': 'ok','message': '修改用户成功'}
        return {'status': 'ok','message': '没有这个用户'}
