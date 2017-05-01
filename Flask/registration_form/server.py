import re
from flask import Flask, render_template, session, flash, request, redirect, url_for
app = Flask(__name__)
app.secret_key = 'ch1ckdatc0d3s'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def main():
    session['your_errors'] = []
    return render_template('index.html')

@app.route('/process', methods=["GET", "POST"])
def processes():
    email = request.form['email']
    firstName = request.form['first_name']
    lastName = request.form['last_name']
    password = request.form['password']
    confirmPass = request.form['passwordConfirm']
    isValid = True


    if len(email) < 1 :
        email = flash("Please enter your email")
        session['your_errors'].insert(0,{'email': email })
        isValid = False

    elif not EMAIL_REGEX.match(email):
        otherEmail = flash("Invalid Email Address!")
        session['your_errors'].insert(0,{'otherEmail': otherEmail })
        isValid = False


    if len(firstName) < 1 :
        firstName = flash("Please enter your First Name")
        session['your_errors'].insert(1,{'firstName': firstName })
        isValid = False

    elif  any(char.isdigit() for char in firstName):
        otherFName = flash('First name cannot contain number')
        session['your_errors'].insert(1,{'otherFName': otherFName })
        isValid = False


    if len(lastName) < 1 :
        lastName = flash("Please enter your Last Name")
        session['your_errors'].insert(2,{'lastName': lastName })
        isValid = False

    elif  any(char.isdigit() for char in lastName):
        otherLName = flash('last name cannot contain number')
        session['your_errors'].insert(2,{'otherLName': otherLName })
        isValid = False


    if len(password) < 1 :
        password = flash("Please enter your Password")
        session['your_errors'].insert(3,{'password': password })
        isValid = False

    elif len(password) < 3:
        passwordlen = flash("Password must be more than 8 characters")
        session['your_errors'].insert(3,{'passwordlen': passwordlen })
        isValid = False

    elif password != confirmPass:
        otherPword1 = flash("Your confirmation password and password must match!")
        session['your_errors'].insert(6,{'otherPword1': otherPword1 })
        isValid = False

    if isValid is False:
        return redirect('/')
    else:
        flash("Sucess!")
        return redirect('/')

app.run(debug=True)
