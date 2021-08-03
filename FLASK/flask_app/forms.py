from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email



# 회원가입 폼
class MemberCreateForm(FlaskForm):
    member_email = EmailField('회원 이메일', validators=[DataRequired(), Length(min=3, max=25)])
    member_password = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('member_password2', '비밀번호가 일치하지 않습니다')])
    member_password2 = PasswordField('member_password2', validators=[DataRequired()])
    member_favorite = StringField('선호 음식', validators=[DataRequired(), Length(min=3, max=25)])

# 로그인 폼
class MemberLoginForm(FlaskForm):
    member_email = EmailField('회원 이메일', validators=[DataRequired(), Length(min=3, max=25)])
    member_password = PasswordField('비밀번호', validators=[DataRequired()])

# 게시판 폼
class FreeBoardCreate(FlaskForm):
    board_restaurant = StringField('음식점', validators=[DataRequired(), Length(min=3, max=25)])
    board_comment = StringField('COMMENT', validators=[DataRequired(), Length(min=3, max=25)])

class FreeBoardUpdate(FlaskForm):
    board_restaurant = StringField('음식점', validators=[DataRequired(), Length(min=3, max=25)])
    board_comment = StringField('COMMENT', validators=[DataRequired(), Length(min=3, max=25)])

#----------------------- [플라스크 예제] ----------------------
# 회원가입 폼
class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])


# 로그인 폼 
class UserLoginForm(FlaskForm): #클래스 상속 
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])