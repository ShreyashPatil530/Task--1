import pytest
from app import create_app, db
from models import Task

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        db.drop_all()
        db.create_all()

        task = Task(title="Test Task")
        db.session.add(task)
        db.session.commit()

    return app.test_client()


def test_create_comment(client):
    res = client.post('/tasks/1/comments', json={"content": "Hello"})
    assert res.status_code == 201
    assert res.json['content'] == "Hello"


def test_get_comments(client):
    client.post('/tasks/1/comments', json={"content": "Hello"})
    res = client.get('/tasks/1/comments')
    assert res.status_code == 200
    assert len(res.json) == 1   # FIXED ✔️


def test_update_comment(client):
    client.post('/tasks/1/comments', json={"content": "Test"})
    res = client.put('/comments/1', json={"content": "Updated"})
    assert res.json['content'] == "Updated"


def test_delete_comment(client):
    client.post('/tasks/1/comments', json={"content": "Delete Me"})
    res = client.delete('/comments/1')
    assert res.status_code == 200
