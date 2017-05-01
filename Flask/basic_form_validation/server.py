from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ch1ckdatc0d3s'

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1:
        flash('Name cannot be empty')
    else:
        flash('{} is a genuis '.format(request.form['name']))
    return redirect('/')

app.run(debug=True)
