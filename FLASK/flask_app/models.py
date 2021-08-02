from sqlalchemy.ext.declarative import declarative_base
from flask_app import db
from datetime import datetime
# from sqlalchemy import Column, Integer, String, DateTime

# --------------------------------- [TEST]
# Base = declarative_base()
# class User(Base):
#     idx = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))

#     # 클래스의 객체를 print하는 방법
#     def __repr__(self):
#         return '<User {}>'.format(self.username)

# # TEST
# from flask_app.models import User
# u = User(username='susan', email='susan@example.com')
# print(u)
# # 출력값 : <User susan>

# --------------------------------- [Project Model]] ---------------------------------- #
class Member(db.Model):
    # PK
    member_id = db.Column(db.Integer, primary_key=True)

    member_email = db.Column(db.String(50), unique=True)
    member_password = db.Column(db.String(200), nullable=False)
    member_favorite = db.Column(db.String(120), nullable=True)
    member_tier = db.Column(db.String(10), default='회원', nullable=True)
    # member_date = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=False)

class Board(db.Model):
    #PK
    board_number = db.Column(db.Integer, primary_key=True) # 게시글 넘버
    #FK
    member_id = db.Column(db.Integer, db.ForeignKey('member.member_id'))

    board_comment = db.Column(db.String(200), nullable=False) #리뷰 내용
    board_restaurant = db.Column(db.String(20), nullable=False) #리뷰 식당
    board_date = db.Column(db.DateTime(), nullable=False) #작성 날짜
    #board_views = db.Column(db.String(200), nullable=False) #조회 수 컬럼

    


# --------------------------------- [Pybo 예제] ---------------------------------- #
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
# --------------------------------------------------------------------------- #

