import json
import os


def load_posts():
    # загрузит данные из файла
    with open(os.path.join('data', 'posts.json'), 'r', encoding='utf-8') as dat:
        data = json.load(dat)
        return data


def load_comments():
    # загрузит данные из файла
    with open(os.path.join('data', 'comments.json'), 'r', encoding='utf-8') as dat:
        data = json.load(dat)
        return data


def get_posts_all():
    return load_posts()


def get_posts_by_user(user_name):
    posts_with_name = []
    for post in load_posts():
        if post['poster_name'].lower().find(user_name.lower()) >= 0:
            posts_with_name.append(post)
    return posts_with_name


def get_comments_by_post_id(post_id):
    comments = []
    for comment in load_comments():
        if comment['post_id'] == int(post_id):
            comments.append(comment)
    return comments


def search_for_posts(query):
    posts_with_word = []
    for post in load_posts():
        if post['content'].lower().find(query.lower()) >= 0:
            posts_with_word.append(post)
    return posts_with_word


def get_post_by_pk(pk):
    for post in load_posts():
        if post['pk'] == int(pk):
            return post
