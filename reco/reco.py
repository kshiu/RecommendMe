from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from reco.auth import login_required
from reco.db import get_db
from .mediaTypes import YouTube

bp = Blueprint('reco', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT r.id, sent, message, link, u.username, title'
        ' FROM recommendations r'
        ' JOIN user u ON r.user_id_Recommender = u.id'
    ).fetchall()
    # look up
    return render_template('reco/index.html', posts=posts)

@bp.route('/new', methods=('GET','POST'))
def create():
    if request.method == 'POST':
        user_id_Recommendee = request.form['recommendee1']
        link = request.form['link']
        message = request.form['message']
        error = None

        if not link:
            error = 'Link is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            video_title = YouTube.get_video_title(link)
            db.execute(
                'INSERT INTO recommendations (user_id_Recommender, user_id_Recommendee, link, message, media_type, title)'
                ' VALUES (?, ?, ?, ?, ?, ?)',
                (g.user['id'], user_id_Recommendee, link, message, 1, video_title)
            )
            db.commit()
            return redirect(url_for('reco.index'))

    return render_template('reco/create.html')