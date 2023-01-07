from flask import Flask, request, render_template, jsonify
import werkzeug
import logging
from api import get_posts_all
from api import get_posts_by_user
from api import get_comments_by_post_id
from api import search_for_posts
from api import get_post_by_pk

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
app = Flask(__name__)


@app.route("/")
def page_index():
    return render_template('index.html', title='Home', posts=get_posts_all())


@app.route("/posts/<post_id>")
def comments(post_id):
    comments = get_comments_by_post_id(post_id)
    return render_template('post.html', title='Home', post=get_post_by_pk(post_id), len=len(comments),comments=comments)



@app.route("/search/")
def search():
    posts = search_for_posts(request.args.get("s"))
    return render_template('search.html', title=f'search by {request.args.get("s")}', len=len(posts), posts=posts)


@app.route("/users/<poster_name>")
def search_by_name(poster_name):
    posts = get_posts_by_user(poster_name)
    return render_template('user-feed.html', title=f'search by {poster_name}', len=len(posts), posts=posts)


@app.route("/api/posts")
def api_posts():
    logging.info('request api posts')
    return jsonify(get_posts_all())


@app.route("/api/posts/<post_id>")
def api_the_post(post_id):
    logging.info(f'request api the post {post_id}')
    return jsonify(get_post_by_pk(post_id))


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    logging.warning(e)
    return 'статус-код 404', 404


@app.errorhandler(werkzeug.exceptions.InternalServerError)
def handle_serverError(e):
    logging.error(e)
    return 'статус-код 500', 500


app.register_error_handler(404, handle_bad_request)
app.register_error_handler(500, handle_serverError)

app.config['JSON_AS_ASCII'] = False

app.run()