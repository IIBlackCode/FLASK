from flask import Blueprint, render_template, request

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

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
@bp.route('/main')
def foody_blog_main():
    return render_template('foody_blog/main.html')
@bp.route('/signin', methods=('GET', 'POST'))
def foody_blog_signin():
    if request.method == 'POST':
        print(request)
        return render_template('foody_blog/signin.html')
    return render_template('foody_blog/signin.html')
@bp.route('/single-post')
def foody_blog_single_post():
    return render_template('foody_blog/single-post.html')
@bp.route('/typography')
def foody_blog_typography():
    return render_template('foody_blog/typography.html')