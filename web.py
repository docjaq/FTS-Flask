from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import os
import tools

app = Flask(__name__)
app.config.from_object('config.FlaskConfig')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0')
