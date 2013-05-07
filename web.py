from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import os
import tools

app = Flask(__name__)
app.config.from_object('config.FlaskConfig')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
    data, posts = tools.getPosts()
    return render_template('index.html', data=data, posts=posts)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'GET':
        return render_template('new_post.html')
    elif request.method == 'POST':
        tools.newPost(request.form['title'], request.form['content'])
        return url_for('/')

if __name__ == '__main__':
  app.run(host='0.0.0.0')
