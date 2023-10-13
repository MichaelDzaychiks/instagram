from flask_wtf import FlaskForm
from flask_wtf import FileField
from wtforms import StringField, EmailField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from application.utils import exist_email,not_exist_email, exist_username

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    fullname = StringField("full name", validators=[DataRequired(), Length(min=6)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')

class ResetPasswordForm(FlaskForm):
    old_password = PasswordField("old password", validators=[DataRequired(), Length(min=8)])
    new_password = PasswordField("new password", validators=[DataRequired(), Length(min=8)])
    confirm_new_password = PasswordField("confirm new password", validators=[DataRequired(),Length(min=8),EqualTo])
    submit = SubmitField("reset password")

class forgot_password(FlaskForm):
    email = EmailField("email", validators=[DataRequired(), not_exist_email])
    recaptcha = RecaptchaField()
    submit = SubmitField("send link verification to email")

class VerificationResetPasswordForm(FlaskForm):
    password = PasswordField("new password", validators=[DataRequired(),Length(min=8)])
    confirm_password = PasswordField("confirm new password", validators=[DataRequired(),Length(min=8), EqualTo("password")])
    submit = SubmitField("reset password")

class EditProfile(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    bio = TextAreaField('Bio')
    submit = SubmitField('Save Changes')

class CreatePost(FlaskForm):
    # title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    # content = TextAreaField('Content', validators=[DataRequired()])
    # image = FileField('terakomari3.jpg')
    # submit = SubmitField('Create Post')
    post_pic = FileField("picture", validators=[DataRequired(), FileAllowed(["jpg", "png", "jpeg"])])
    caption = TextAreaField("caption")
    submit = SubmitField("post")

class EditPost(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    image = FileField('terakomari3.jpg')
    submit = SubmitField('Save Changes')
