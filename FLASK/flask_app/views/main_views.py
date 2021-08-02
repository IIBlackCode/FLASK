from flask_app.models import User
from flask_app.forms import MemberLoginForm
from flask import Blueprint, url_for, render_template, flash, request, session, g
from flask_app.forms import MemberCreateForm
from flask_app.models import Member
from flask_app import db
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect


bp = Blueprint('main', __name__, url_prefix='/')

@bp.before_app_request
def load_logged_in_user():
    member_id = session.get('member_id')
    print("session : ",member_id)
    if member_id is None:
        g.user = None
        print("현재 세션 없음")
    else:
        # g.user = User.query.get(1)
        g.user = Member.query.get(member_id)
        print("세션 저장 완료 :",g.user.member_email)

@bp.route('/')
def foody_blog_index():
    return render_template('foody_blog/index.html')
@bp.route('/404')
def foody_blog_404():
    return render_template('foody_blog/404.html')
@bp.route('/about')
def foody_blog_about():
    return render_template('foody_blog/about.html')
@bp.route('/categories-grid')
def foody_blog_categories_grid():
    return render_template('foody_blog/categories-grid.html')
@bp.route('/categories-list')
def foody_blog_categories_list():
    return render_template('foody_blog/categories-list.html')
@bp.route('/contact')
def foody_blog_contact():
    return render_template('foody_blog/contact.html')
@bp.route('/freeBoard')
def foody_blog_freeBoard():
    return render_template('foody_blog/freeBoard/freeBoardList.html')
@bp.route('/main')
def foody_blog_main():
    return render_template('foody_blog/main.html')

@bp.route('/signin', methods=('GET', 'POST'))
def foody_blog_signin():
    form = MemberCreateForm()
    if request.method == 'POST':
        print("입력한 E-mail : ",form.member_email.data)
        print("입력한 password : ",form.member_password.data)
        print("입력한 member_favorite : ",form.member_favorite.data)
        member = Member.query.filter_by(member_email=form.member_email.data).first()
        #print('user ::::: ',user)
        if not member:
            print("회원가입 성공")
            member = Member(
                member_email=form.member_email.data,
                # member_password=generate_password_hash(form.member_password.data),
                member_password=(form.member_password.data),
                member_favorite = form.member_favorite.data
                )
            db.session.add(member)
            db.session.commit()
            return render_template('foody_blog/signin.html',form = form)
        else:
            print("회원가입 실패")
            flash('이미 존재하는 사용자입니다.')
            return render_template('foody_blog/signin.html',form = form)
    return render_template('foody_blog/signin.html',form = form)

@bp.route('/login', methods=('GET', 'POST'))
def foody_blog_login():
    form = MemberLoginForm()
    # if request.method == 'POST' and form.validate_on_submit():
    if request.method == 'POST':
        error = None
        member = Member.query.filter_by(member_email=form.member_email.data).first()
        print("입력한 E-mail : ",form.member_email.data)
        print("입력한 password : ",form.member_password.data)
        print("member : ",member)
        if not member:
            error = "login : 존재하지 않는 사용자입니다."
            print("error : ",error)
            return render_template('foody_blog/signin.html',form = form)
        # elif not check_password_hash(member.member_email, form.member_email.data):
        elif member.member_email != form.member_email.data:
            print("저장된 E-mail : ",member.member_email)
            print("저장된 비밀번호 : ",member.member_password)
            error = "비밀번호가 올바르지 않습니다."
            print("error : ",error)
            return render_template('foody_blog/signin.html',form = form)
        if error is None:
            print("error is None ")
            session.clear()
            # session['member_email'] = member.member_email
            session['member_id'] = member.member_id
            flash(error)
            return redirect(url_for('main.foody_blog_index'))
            # return render_template('foody_blog/index.html',form = form)
    
    # return render_template('foody_blog/index.html',form = form)
@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.foody_blog_index'))

@bp.route('/single-post')
def foody_blog_single_post():
    return render_template('foody_blog/single-post.html')
@bp.route('/typography')
def foody_blog_typography():
    return render_template('foody_blog/typography.html')