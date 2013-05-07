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
    post.date = int(math.floor(time.time()))
    post.title = title
    post.content = content
    post.save()
    return True

def getPosts(pageNo = 1):
    posts = Post.query.paginate(page=pageNo, per_page=10)
    post_list = []
    data = {}
    data['next'] = posts.has_next()
    data['prev'] = posts.has_prev()
    data['page'] = pageNo
    data['total_pages'] = posts.pages
    for post in posts.items:
        p = {}
        p['id'] = post.id
        p['date'] = post.date
        p['title'] = post.title
        p['content'] = post.content
        post_list.append(p)
    sorted_posts = sorted(post_list, key=lambda k: k['date'], reverse=True)
    return (data, sorted_posts)
