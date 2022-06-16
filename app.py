from flask import Flask, redirect, render_template, request, session, g
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:boybitz@localhost/database'
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)


class Manager(db.Model):
    email = db.Column(db.String(50), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(15))
    scholars = db.relationship('Scholar')


class Scholar(db.Model):
    ronin_address = db.Column(db.String(50), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    scholar_share = db.Column(db.Integer)
    manager_share = db.Column(db.Integer)
    total_slp = db.Column(db.Integer)
    manager = db.Column(db.String(50), db.ForeignKey('manager.email'))















@app.before_request
def load_logged_in_user():
    manager_email = session.get('manager_email')
    if manager_email == None:
        g.manager = None
    else:
        g.manager = Manager.query.get(manager_email)


@app.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        manager = Manager(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        db.session.add(manager)
        db.session.commit()

        return redirect('login')

    return render_template('Sign_up.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        manager = Manager.query.get(email)
        if manager == None:
            return '<h1>Invalid emalil</h1>'
        elif password != manager.password:
            return '<h1>Invalid password</h1>'
        else:
            session['manager_email'] = manager.email
            return redirect('home')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('login')


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/add-scholar', methods=['POST'])
def add():
    ronin_address = request.form.get('ronin')
    first_name = request.form.get('first')
    last_name = request.form.get('last')
    scholar_share = request.form.get('scholar_share')
    manager_share = request.form.get('manager_share')
    total_slp = request.form.get('total_slp')
    scholar = Scholar(
        ronin_address = ronin_address,
        first_name=first_name,
        last_name=last_name,
        scholar_share = scholar_share,
        manager_share = manager_share,
        total_slp = total_slp, 
        manager = g.manager.email
    )
    db.session.add(scholar)
    db.session.commit()
    return redirect('home')

@app.route('/update-scholar', methods=['POST'])
def update():
    ronin_address = request.form.get('update-ronin')
    first_name = request.form.get('update-first')
    last_name = request.form.get('update-last')
    scholar_share = request.form.get('update-scholar_share')
    manager_share = request.form.get('update-manager_share')
    total_slp = request.form.get('update-total_slp')
    
    scholar = Scholar.query.get(ronin_address)
    scholar.first_name = first_name
    scholar.last_name = last_name
    scholar.scholar_share = scholar_share
    scholar.manager_share = manager_share
    scholar.total_slp = total_slp
    db.session.commit()
    return redirect('home')

@app.route('/delete-scholar', methods = ['POST'])
def delete():
    ronin_address = request.form.get('delete-ronin')
    
    scholar = Scholar.query.get(ronin_address)
    db.session.delete(scholar)
    db.session.commit()
    return redirect('home')
    




