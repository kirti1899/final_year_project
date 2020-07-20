from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'myPRA'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/myPRA'

mongo = PyMongo(app)

@app.route('/', methods=["GET"])
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return "Hello"

@app.route('/login' , methods=["POST"])
def login():
    users = mongo.db.users
    
    login_user = users.find_one({'name' : request.form['username']})
    
    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
    return 'Invalid username/password combination' 
   
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            #hashpass = bcrypt.hashpw(request.form['pass'], encode('utf-8'), bcrypt.gensalt())
            hashpass = request.form['pass']
            users.insert({'name' : request.form['username'] , 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'Username already exists!'
        
    return "pls check db, insert from my side"

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
