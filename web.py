from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import os

app = Flask(__name__)
config = os.path.join(app.root_path, 'FTS_CONFIG')
app.config.from_pyfile(config)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
  app.run(host='0.0.0.0')
