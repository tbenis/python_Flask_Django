from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ch1ckdatc0d3s'

@app.route('/')
def thePage():
    if session.get('counter') == None:
        session['counter'] = 0
    else:
        session['counter'] +=1
    return render_template('index.html')

@app.route('/ninjas', methods=['POST'])
def ninja():
    session['counter'] += 2
    return render_template('index.html')


@app.route('/hackers', methods=['POST'])
def hacker():
    session['counter'] =1
    return render_template('index.html')


app.run(debug=True)
