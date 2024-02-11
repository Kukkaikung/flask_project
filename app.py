from flask import Flask,render_template,request,session,flash,url_for, redirect
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from wtforms import TextAreaField, SubmitField, BooleanField, RadioField, SelectField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError, InputRequired
from flask_bcrypt import Bcrypt








app = Flask(__name__)


class  MyForm(FlaskForm) :
    name = TextAreaField('Enter your name', validators=[DataRequired()])
    isAccept = BooleanField('Allow')
    gender = RadioField('Gender', choices=[('Male','Male'),('Female','Female')])
    skill = SelectField('Skill', choices=[('English','Englissh'),('Python','Python'),('CSS','CSS')])
    submit = SubmitField('Suubmit')





@app.route('/')
def index() :
    return render_template('index.html')


@app.route('/intoduce', methods = ['GET','POST'])
def introduce() :
    return render_template('introduce.html')

@app.route('/myskill', methods = ['GET','POST'])
def myskill() :
    return render_template('myskill.html')


@app.route('/second', methods = ['GET','POST'])
def second() :
    return render_template('second.html')

@app.route('/hobby')
def hobby() :
    return render_template('hobby.html')

@app.route('/admin')
def admin() :
    name = 'Baimai'
    age = 30
    return render_template('admin.html')

@app.route('/favorite')
def favorite() :
    return render_template('favorite.html')

@app.route('/sport')
def sport() :
    return render_template('sport.html')

@app.route('/coding')
def coding() :
    return render_template('coding.html')

@app.route('/music')
def music() :
    return render_template('music.html')


if __name__ == "__main__" :
    app.run(debug=True)