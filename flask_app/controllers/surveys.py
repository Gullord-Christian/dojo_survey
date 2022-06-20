from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.survey import Survey

@app.route('/')
def home():
    return render_template("home.html")

@app.route ('/create/survey', methods =['POST'])
def create_survey():
    if Survey.is_valid(request.form): 
        Survey.save(request.form)
        return redirect('/results')
    return redirect('/')

@app.route('/results')
def show():
    return render_template('result.html', survey = Survey.get_last_survey())