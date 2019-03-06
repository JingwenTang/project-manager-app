
from flask import Flask, render_template, redirect, url_for ,session, request, flash


app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login/', methods=["GET", "POST"])
def login():
    error = None

    if request.method == 'POST':
        if request.form['email'] != '736658768@qq.com':
            error = "Invalid email"
        elif request.form['password'] != 'kechengsheji':
            error = 'Invalid password'
        else:
            return render_template('index.html')
    return render_template('login.html', error = error)

@app.route('/register/')
def register():
    return render_template('register.html')

@app.route('/forgot/')
def forgot():
    return render_template('forgot_password.html')

@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/surroundings/')
def surroundings():
    return render_template('surroundings.html')

@app.route('/finding/')
def finding():
    return render_template('finding.html')

@app.route('/myself/')
def myself():
    return render_template('myself.html')

if __name__ == '__main__':
    app.run()