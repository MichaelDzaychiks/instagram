from wtforms.validators import ValidationError

from application import login_manager
from application.models import User

@login_manager.user_loader
def load_user(user_id):
    user = User.query.filter_by(email = email.data).first()
    if user:
        raise ValidationError("email already exists. please use a different email")
    # return User.query.get(int(user_id))
def exist_username(form,username):
    user = user.query.filter_by(username=username.data).first()
    if user:
        raise ValidationError("email already exists. please use a different email")
    
    def exist_username