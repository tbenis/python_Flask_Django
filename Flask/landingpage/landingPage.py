from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def greeting():
    return render_template('greeting.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def dojo():
    return render_template('dojo.html')

app.run(debug=True)                       
