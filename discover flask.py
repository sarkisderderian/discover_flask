from flask import Flask
from flask import render_template
from flask import redirect,request,url_for
from flask import session

app = Flask(__name__)
app.secret_key="my precious"


@app.route('/')
def hello_world():
    return """<center>HOME
            <br>
            <a href="./welcome">welcome</a><br>
            <a href="./login">Login</a><br>

            </center>"""

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if request.method=='POST':
        if request.form['username']!= 'admin' or request.form['password'] != 'admin':
            error='Invalid credentials, Please try agein.'
        else:
            session['logged_in']=True
            return redirect(url_for('home'))
    return render_template('login.html',error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run(port=3030,debug=True)
