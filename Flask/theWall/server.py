from flask import Flask, render_template, session, flash, request, redirect, url_for
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
app = Flask(__name__)
app.secret_key = 'ch1ckdatc0d3s'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app,'thewall')
bcrypt = Bcrypt(app) # instantiating the bycrypt object

@app.route('/')
def disp_err():
    session['your_errors'] = []
    return render_template('index.html')

@app.route('/registration', methods=["GET", "POST"])
def regUser():
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
    else :

        password = request.form['password']
        pw_hash = bcrypt.generate_password_hash(password)
        email = request.form['email']

        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : email,
            'password' : pw_hash
        }

        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name, :last_name, :email, :password, NOW(), NOW())"


        session['user_id'] = mysql.query_db(query, data) # grabs users id at log in
        session['first_name'] = request.form['first_name']

        return redirect('/wall')
@app.route('/login', methods=['POST'])
def login():
    error = False

    if len(request.form['email']) < 1:
        flash('You must enter an email')
        error = True
    if len(request.form['password']) < 1:
        flash('You must enter Your password')
        error = True
    if error :
        return redirect('/')
    else:
        password = request.form['password']
        email = request.form['email']

        data = {
            'email' : email
        }

        query = "SELECT * FROM users WHERE email= :email"

        user = mysql.query_db(query, data) #this returns a list

    if len(user) == 0:
            flash('User does not exist')
            return redirect('/')

    if bcrypt.check_password_hash(user[0]['password'], password):
        session['user_id'] = user[0]['id']
        session['first_name'] = user[0]['first_name']
        return redirect('/wall')
    else:
        flash('Incorrect email or password')
        return redirect('/')

@app.route('/post_message', methods=['POST'])
def post_message():
    query = 'INSERT INTO messages (message, created_at, updated_at, users_id) VALUES(:message, NOW(), NOW(), :user_id)'
    data = {
        'message' : request.form['message'],
        'user_id' : session['user_id'] #person currently logged in
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/post_comment', methods=['POST'])
def post_comments():
    query = "INSERT INTO comments (comment, created_at, updated_at, users_id, messages_id) VALUES (:comment, NOW(), NOW(), :user_id, :message_id)"

    data = {
        'comment' : request.form['comment'],
        'user_id' : session['user_id'],
        'message_id' : request.form['message_id']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/wall')
def show_wall():
        query = "SELECT users.id AS user_id, users.first_name, users.last_name, messages.message, messages.id AS message_id, DATE_FORMAT(messages.created_at, '%M %D %Y') as created_at FROM users JOIN messages ON users.id = messages.users_id ORDER BY messages.created_at DESC"

        session['messages'] = mysql.query_db(query)

        query2 = "SELECT users.id AS users_id, users.first_name, users.last_name, comments.comment, comments.messages_id AS message_id, DATE_FORMAT(comments.created_at, '%M %D %Y') as created_at FROM users JOIN comments ON users.id = comments.users_id"

        session['comments'] = mysql.query_db(query2)

        return render_template('thewall.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
