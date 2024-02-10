from flask import Flask,render_template,request,session
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, BooleanField, RadioField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class  MyForm(FlaskForm) :
    name = TextAreaField('Enter your name', validators=[DataRequired()])
    isAccept = BooleanField('Allow')
    gender = RadioField('Gender', choices=[('Male','Male'),('Female','Female')])
    skill = SelectField('Skill', choices=[('English','Englissh'),('Python','Python'),('CSS','CSS')])
    submit = SubmitField('Suubmit')


@app.route('/', methods = ['GET','POST'])
def index() :
    form = MyForm()
    if form.validate_on_submit() :
        session['name'] = form.name.data
        session['isAccept'] = form.isAccept.data
        session['gender'] = form.gender.data
        session['skill'] = form.skill.data
        form.name.data = ""
        form.isAccept.data = ""
        form.gender.data = ""
    return render_template('index.html', form = form)

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