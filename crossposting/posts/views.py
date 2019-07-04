from flask import abort, render_template, flash, redirect, url_for
from . import posts_page
from ..models import Post
from .. import db


@posts_page.route('/posts', methods=['GET', 'POST'])
def list_posts():
    """
    List all posts
    """
    posts = Post.query.all()

    try:
        return render_template('posts/posts.html', posts=posts, title="Posts")
    except:
        abort(404)


@posts_page.route('/posts/delete/<int:id>', methods=['GET', 'POST'])
def delete_post(id):
    """
    Delete a post from the database
    """
    posts = Post.query.get_or_404(id)
    db.session.delete(posts)
    db.session.commit()
    flash('You have successfully deleted the post.')

    # redirect to the posts page
    return redirect(url_for('posts_page.list_posts'))