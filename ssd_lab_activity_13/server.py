from flask_login import (login_manager, LoginManager, login_user, logout_user, login_required, UserMixin)

from flask_sqlalchemy import SQLAlchemy

from flask import (Flask, render_template, request, redirect, session)


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'secretkey'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique=True, nullable=False)  
    name = db.Column(db.String(200))
    password = db.Column(db.String(100), nullable=False)

def main():
    with app.app_context():
        db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', methods=["GET"])
def hello_world():
    return render_template('signup.html')

def err(msg,typ=True):
    if typ:
        return {"ErrorMessage": msg}
    else:
        return {"Result":msg}



@app.route('/logout')
def logout():         
    return redirect('/login')
    



@app.route("/login", methods = ["POST", "GET"])
def do_login():
    if (request.method=="POST"):
        req = request.form
        print(req)
        username = req["user_name"]
        password = req["password"]
        check_user = User.query.filter_by(username = username).first()
        if check_user is not None:
            if (check_user.password == password):
                login_user(check_user)
                return err("Logged in successfully",False)
            else:
                return err("Password is incorrect")
        else:
            return err("User does not exist")
    else:
        return render_template("login.html")



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='GET':
        return render_template('signup.html')
    else:
        email = request.form.get('user_name')
        name = request.form.get('name')
        password = request.form.get('password')
        user = User.query.filter_by(username=email).first()
        if user:
            return err('Email address already exists')
        new_user = User(username=email, name=name, \
                        password=password)
        db.session.add(new_user)
        db.session.commit()
        return err("Registered successfully",False) 




if __name__ == '__main__':
    main()
    app.run(host="127.0.0.1",port="5000",debug=True)