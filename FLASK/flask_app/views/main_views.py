from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return render_template('foody_blog/index.html')

#------------------------------ [Theme] ------------------------------#

@bp.route('/theme/index')
def theme_index():
    return render_template('theme/index.html')
@bp.route('/theme/404')
def theme_404():
    return render_template('theme/404.html')
@bp.route('/theme/about')
def theme_about():
    return render_template('theme/about.html')
@bp.route('/theme/categories-grid')
def theme_categories_grid():
    return render_template('theme/categories-grid.html')
@bp.route('/theme/categories-list')
def theme_categories_list():
    return render_template('theme/categories-list.html')
@bp.route('/theme/contact')
def theme_contact():
    return render_template('theme/contact.html')
@bp.route('/theme/main')
def theme_main():
    return render_template('theme/main.html')
@bp.route('/theme/signin')
def theme_signin():
    return render_template('theme/signin.html')
@bp.route('/theme/single-post')
def theme_single_post():
    return render_template('theme/single-post.html')
@bp.route('/theme/typography')
def theme_typography():
    return render_template('theme/typography.html')
