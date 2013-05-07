from flaskext.mongoalchemy import MongoAlchemy
from flask import Flask
import time, uuid, math

app = Flask(__name__)
app.config.from_object('config.DatabaseConfig')

app.config['MONGOALCHEMY_DATABASE'] = app.config['MONGOALCHEMY_DATABASE']
app.config['MONGOALCHEMY_SERVER_AUTH'] = app.config['MONGOALCHEMY_SERVER_AUTH']
app.config['MONGOALCHEMY_USER'] = app.config['MONGOALCHEMY_USER']
app.config['MONGOALCHEMY_PASSWORD'] = app.config['MONGOALCHEMY_PASSWORD']
app.config['MONGOALCHEMY_SERVER'] = app.config['MONGOALCHEMY_SERVER']
app.config['MONGOALCHEMY_PORT'] = app.config['MONGOALCHEMY_PORT']

db = MongoAlchemy(app)

#
# Define class documents:
#
class Post(db.Document):
    id = db.StringField()
    date = db.IntField()
    title = db.StringField()
    content = db.StringField()

def newPost(title, content):
    post = Post()
    post.id = str(uuid.uuid4())        
    post.date = Math.floor(time.time())

