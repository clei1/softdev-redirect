from flask import Flask, render_template, request, session, redirect, url_for, flash
import os

my_app = Flask(__name__)
my_app.secret_key = os.urandom(32)

login = {"hello":"life", "life":"hello"}

@my_app.route("/", methods = ['GET','POST'])
def root():
    '''
    two possible routes:
    welcome page if logged in
    login page if not logged in
    '''
    if "login" in session:
        return redirect(url_for('welcome')) 
    return render_template('form.html')

@my_app.route("/logout", methods = ['GET', 'POST'])
def logout():
    '''
    one possible routes:
    welcome page
    '''
    session.clear()
    return redirect(url_for('root'))

@my_app.route('/welcome', methods = ['GET','POST'])
def welcome():
    '''
    two possible routes:
    welcome page if logged in
    login page if not logged in
    '''    
    if "login" in session:
        return render_template('welcome.html', username = session['username'])
    else:
        return redirect(url_for('root'))

@my_app.route('/response', methods = ['POST'])
def response():
    '''
    three possible routes:
    welcome page if authorized to log in
    login page if error exists
    '''
    for username in login:
        if (request.form["username"] == username):
            if(request.form["password"] == login[username]):
                session["login"] = True
                session["username"] = request.form["username"]
                return redirect(url_for('welcome'))
            else:
                flash('Invalid password.')
                return redirect(url_for('root'))
    flash('Invalid username.')     
    return redirect(url_for('root'))                       

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()

