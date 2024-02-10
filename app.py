from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, BooleanField, RadioField, SelectField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class  MyForm(FlaskForm) :
    name = TextAreaField('Enter your name')
    isAccept = BooleanField('Allow')
    gender = RadioField('Gender', choices=[('Male','Male'),('Female','Female')])
    skill = SelectField('Skill', choices=[('English','Englissh'),('Python','Python'),('CSS','CSS')])
    submit = SubmitField('Suubmit')


@app.route('/', methods = ['GET','POST'])
def index() :
    form = MyForm()
    data = {'name':'Baimai', 'age':19, 'salary':'100000'}
    name = False
    isAccept = False
    gender = False
    skill = False
    if form.validate_on_submit() :
        name = form.name.data
        isAccept = form.isAccept.data
        gender = form.gender.data
        skill = form.skill.data
        form.name.data = ""
        form.isAccept.data = ""
        form.gender.data = ""
    return render_template('index.html', mydata = data, form = form, name = name, isAccept = isAccept, gender = gender, skill = skill)

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