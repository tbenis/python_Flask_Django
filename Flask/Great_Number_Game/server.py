
from flask import Flask, session, redirect, request, render_template
import random
app = Flask(__name__)
app.secret_key = 'ch1ckdatc0d3s'
@app.route('/')
def game():
    session['random_number'] = random.randrange(1,101)
    return render_template('game.html')

@app.route('/submit', methods=['POST'])
def guess():

    session['guess']= int(request.form['guess'])
    if session['random_number'] == session['guess']:
        return redirect('/right')
    else:
        return redirect('wrong')


@app.route('/wrong')

def low_number():
    if session['guess'] != session['random_number']:
        return render_template('wrong.html')
        # session.pop('guess')


@app.route('/right')
def right_number():
    if session['guess'] == session['random_number']:
        return render_template('right.html')
        session.pop('guess')

    # return render_template('game.html')


app.run(debug=True)
