import pytest
from main import app


def test_app():
    response = app.test_client().get('/api/posts')
    a = response.json()
    print(a)