from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def return_survey():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def returnPage():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    return render_template('results.html', name=name, location=location, language=language, comments=comments)
app.run(debug=True)
