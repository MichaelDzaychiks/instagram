from application import db
from datetime import datetime

class User(db.Model):
    tablename = "users"
    id = db.Column(db.Integer, primary_key = True)
    username    = db.Column(db.String(128), nullable = False)
    password    = db.Column(db.String(128), nullable = False)
    fullname    = db.Column(db.String(128), nullable = False)
    profile_pic = db.Column(db.String(128), default="9ec0ad2773d76b805b7b59850ca6fec6.jpg")
    bio         = db.Column(db.String(128))
    join_data   = db.Column(db.DateTime, default=datetime.utcnow)
    status      = db.Column(db.Boolean, default=True)

class Relation(db.Model):
    tablename = "relations"
    id            = db.Column(db.Integer, primary_key = True)
    id_follower   = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    id_following  = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    status        = db.Column(db.Boolean, default=True)
    relation_data = db.Column(db.DateTime, default=datetime.utcnow)

class Post(db.Model):
    tablename = "posts"
    id        = db.Column(db.Integer, primary_key = True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    photo     = db.Column(db.String(128), nullable = False)
    caption   = db.Column(db.String(128), default="")
    status    = db.Column(db.Boolean, default=True)
    post_date = db.Column(db.DateTime, default=datetime.utcnow)


class Comment(db.Model):
    tablename = "comments"
    id           = db.Column(db.Integer, primary_key = True)
    text         = db.Column(db.Text, nullable = False)
    commenter_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    post_id      = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable = False)
    hidden       = db.Column(db.Boolean, default=False)
    comment_date = db.Column(db.DateTime, default=datetime.utcnow)  

class Like(db.Model):
    tablename = "likes"
    id        = db.Column(db.Integer, primary_key = True)
    like_id   = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    post_id   = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable = False)
    status    = db.Column(db.Boolean, default=True)
    like_date = db.Column(db.DateTime, default=datetime.utcnow)