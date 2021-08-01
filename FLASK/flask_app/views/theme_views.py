from flask import Blueprint, render_template

bp = Blueprint('theme', __name__, url_prefix='/theme')

#------------------------------ [Theme] ------------------------------#
@bp.route('/index')
def theme_index():
    return render_template('theme/index.html')
@bp.route('/404')
def theme_404():
    return render_template('theme/404.html')
@bp.route('/about')
def theme_about():
    return render_template('theme/about.html')
@bp.route('/categories-grid')
def theme_categories_grid():
    return render_template('theme/categories-grid.html')
@bp.route('/categories-list')
def theme_categories_list():
    return render_template('theme/categories-list.html')
@bp.route('/contact')
def theme_contact():
    return render_template('theme/contact.html')
@bp.route('/main')
def theme_main():
    return render_template('theme/main.html')
@bp.route('/signin')
def theme_signin():
    return render_template('theme/signin.html')
@bp.route('/single-post')
def theme_single_post():
    return render_template('theme/single-post.html')
@bp.route('/typography')
def theme_typography():
    return render_template('theme/typography.html')