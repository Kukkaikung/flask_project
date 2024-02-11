from flask import Flask,render_template,request,session,flash,url_for
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from wtforms import TextAreaField, SubmitField, BooleanField, RadioField, SelectField
from wtforms.validators import DataRequired



app = Flask(__name__)


app.config['SECRET_KEY'] = 'mykey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/ASUS/Desktop/VS code/PsuTerm02/241-152/database.db'

db = SQLAlchemy(app)






class User(db.Model, UserMixin) :
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False, unique = True)
    password = db.Column(db.String(80), nullable = False)


class  MyForm(FlaskForm) :
    name = TextAreaField('Enter your name', validators=[DataRequired()])
    isAccept = BooleanField('Allow')
    gender = RadioField('Gender', choices=[('Male','Male'),('Female','Female')])
    skill = SelectField('Skill', choices=[('English','Englissh'),('Python','Python'),('CSS','CSS')])
    submit = SubmitField('Suubmit')





@app.route('/')
def index() :
    return render_template('index.html',)

@app.route('/login')
def login() :
    return render_template('login.html',)

@app.route('/register')
def register() :
    return render_template('register.html',)

@app.route('/second', methods = ['GET','POST'])
def second() :
    form = MyForm()
    if form.validate_on_submit() :
        flash(' Reord data')
        session['name'] = form.name.data
        session['isAccept'] = form.isAccept.data
        session['gender'] = form.gender.data
        session['skill'] = form.skill.data
        form.name.data = ""
        form.isAccept.data = ""
        form.gender.data = ""
    return render_template('second.html', form = form)

@app.route('/about')
def about() :
    products = ['เสื้อผ้า', 'เตารีด', 'ผ้าห่ม']
    return render_template('about.html', myproduct = products)

@app.route('/admin')
def profile() :
    name = 'Baimai'
    age = 30
    return render_template('admin.html', myname = name, myage = age)

@app.route('/sendData')
def singupform() :
    fname = request.args.get('fname')
    description = request.args.get('description')
    return render_template('thankyou.html', data = {'name':fname, 'description':description}) 

if __name__ == "__main__" :
    app.run(debug=True)