from flask import Flask, render_template, request, redirect, session, flash
app =Flask(__name__)

@app.route('/')
def mainPage():
    return render_template('nonINJA.html')

@app.route('/ninja')
def main_ninja():
    return render_template('index.html')

@app.route('/ninja/<color>')
def handler_function(color):
  if color == 'blue':
     return render_template('leonardo.html', color=color)
  if color == 'orange':
      return render_template('michelangelo.html', color=color)
  if color == 'red':
      return render_template('raphael.html', color=color)
  if color == 'purple':
      return render_template('donatello.html', color=color)
  else:
      return render_template('notapril.html', color=color)
  # return render_template('index.html', color=color)
app.run(debug=True)
