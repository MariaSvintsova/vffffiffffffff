
import pytest
import json

from main import app


def test_app():
    response = app.test_client().get('/api/posts')
    res = response.json
    assert type(res) is list
    assert 'poster_name' in res[0]
    assert 'poster_avatar' in res[0]
    assert 'pic' in res[0]
    assert 'content' in res[0]
    assert 'pk' in res[0]
    assert 'views_count' in res[0]
    assert 'likes_count' in res[0]



def test_app1():
    response = app.test_client().get('/api/posts/1')
    res = response.json
    assert type(res) is dict
    assert 'poster_name' in res
    assert 'poster_avatar' in res
    assert 'pic' in res
    assert 'content' in res
    assert 'pk' in res
    assert 'views_count' in res
    assert 'likes_count' in res

