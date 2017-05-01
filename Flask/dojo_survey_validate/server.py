from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'ch11'

@app.route('/')
def return_survey():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def returnPage():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']

    if len(request.form['name']) < 1:
        print 'name not here'
        flash("name cannot be empty")
        return redirect('/')

    if len(request.form['comments']) > 121:
        print 'comments works'
        flash('comments cannot longer than 120 characters')
        return redirect('/')

    elif len(request.form['comments']) < 1:
        print 'comments works'
        flash('comments cannot be empty')
        return redirect('/')


    else:
        return render_template('results.html', name=name,  comments=comments, location=location, language=language)

app.run(debug=True)
