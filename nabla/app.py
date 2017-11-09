#!/usr/bin/env python
from flask import Flask, render_template, request
import pandas as pd
import os
import transcript_string_matcher as tsm

app = Flask(__name__)
# DATA_DIR = os.environ('DATA_DIR')  # update the directory path to use env variables
urlpath = 'nabla'

def startserver(path):
    """starts the webservice with specified prefix
    """
    global urlpath
    urlpath = path
    app.run(debug=True, host='0.0.0.0', port=4444)

@app.route('/')
@app.route('/index')
def index():
    """
    The 'home' page route
    """
    return render_template('index.html', name=urlpath)



@app.route('/<string:var>/input', methods =['POST', 'GET'])
def yabs_input(var):
    """
    The input route for inputting yabla source
    """
    return render_template('input.html', var=var)



@app.route('/<string:var>/result', methods =['POST', 'GET'])
def yabs_answers(var):
    if request.method == 'POST':
        html = request.form['html']
    """
    The result route for displaying the yabla transcript.
    """
    chunklist = tsm.extract_transcript(html)
    transcript = tsm.format_transcript(chunklist)
    return render_template('result.html', var=var, transcript=transcript)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4444)
