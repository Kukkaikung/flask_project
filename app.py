from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index() :
    data = {'name':'Baimai', 'age':19, 'salary':'100000'}
    return render_template('index.html', mydata = data)

@app.route('/about')
def about() :
    products = ['เสื้อผ้า', 'เตารีด', 'ผ้าห่ม']
    return render_template('about.html', myproduct = products)

@app.route('/admin')
def profile() :
    name = 'Pai'
    age = 30
    return render_template('admin.html', myname = name, myage = age)


if __name__ == "__main__" :
    app.run(debug=True)