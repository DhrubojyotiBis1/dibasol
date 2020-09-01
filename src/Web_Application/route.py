import bcrypt
from flask import request
from Web_Application import app
from Web_Application.models import User
from Web_Application.db_operator import insert, remove

@app.route('/signup', methods = ['POST'])
def signup():
    status_code = 400
    didSignUp = False
    if request.method == 'POST':
        name = request.args.get('name')
        email = request.args.get('email')
        password = request.args.get('pass')
        hash_passord = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        if name and email and password:
            user = User(name, email, hash_passord)
            if user:
                status_code = insert(user)
                if status_code == 200:
                    didSignUp = True
            else:
                status_code = 500
    return {'SignUp': didSignUp}, status_code


@app.route('/signin', methods = ['POST'])
def signin():
    status_code = 400
    didSignIn = False
    if request.method == 'POST':
        email = request.args.get('email')
        password = request.args.get('pass')
        if email and password:
            user = User.query.filter_by(email=email).first()
            if user:
                if bcrypt.checkpw(password.encode('utf-8'), user.password):
                    didSignIn = True
                    return {'Name': user.name, 'SignIn': didSignIn}
                else:
                    status_code = 401
            else:
                status_code = 404
    return {'SignIn': didSignIn}, status_code