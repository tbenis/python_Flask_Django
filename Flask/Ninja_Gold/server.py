import datetime
import random
from flask import Flask, redirect, render_template, session, request
app = Flask(__name__)
app.secret_key = 'ch1ckdatc0d3s'

@app.route('/', methods=['GET','POST'])
def main():
    if session.get('gold') == None:
        session['gold'] = 0
        session['arrayGold'] = []

    return render_template('main.html')

@app.route('/process_money', methods=['POST'])
def farm():

    if request.form['sub'] == 'farm':
        random_gold = random.randrange(10,21)
        location = 'farm'

    if request.form['sub'] == 'cave':
        random_gold= random.randrange(5,11)
        location = 'cave'

    if request.form['sub'] == 'house':
        random_gold= random.randrange(2,7)
        location = 'house'

    if request.form['sub'] == 'casino':
        random_gold= random.randrange(-50,51)
        location = 'casino'

    if random_gold < 0:
        color = 'danger'
        sentence = ("lost" +  str(random_gold) + "!" , ti.strftime("%I:%M:%S"))
        session['arrayGold'].insert(0, {'color': color, 'sentence': sentence})

    if random_gold >= 0:
        color = 'pass'
        sentence = ("earned " +  str(random_gold) +  " from the " + location + "!")
        session['arrayGold'].insert(0, {"color": color, "sentence": sentence})

    session['gold'] += random_gold
    return redirect('/')
#
# @app.route('/farm')
# def farm():
#     session['random_gold1'] = random.randrange(10,21)
#     session['gold'] += session['random_gold1']
#     return redirect('/')
# @app.route('/cave')
# def cave():
#     session['random_gold2'] = random.randrange(5,11)
#     session['gold'] += session['random_gold1']
#     return redirect('/')
#
# @app.route('/house')
# def home():
#     session['random_gold3'] = random.randrange(2,6)
#     session['gold'] += session['random_gold']
#     return redirect('/')
#
# @app.route('/casino')
# def cas():
#     session['random_gold4'] = random.randrange(0,51)
#     session['gold'] += session['random_gold4']
#     return redirect('/')
#
#
#

app.run(debug=True)
