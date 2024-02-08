from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def text():
    return 'Hello duriya'

if __name__ == "__main__" :
    app.run()