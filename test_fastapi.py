from fastapi.testclient import TestClient
from main import app

# Create a test client
client = TestClient(app)


def test_root():
    result = client.get('/')
    print(result.json())
    assert result.status_code==200
    result_dict = result.json()
    assert result_dict['Hello'] == 'World'


def test_post_message():
    result = client.post('/messages/1?message=hello')
    assert result.status_code==200
    result = client.get('/messages/1')
    assert result.status_code==200
    print(result.json())
    result_dict = result.json()
    assert result_dict['1']=='hello'


def test_get_all_messages():
    result = client.get('/messages/')
    assert result.status_code==200
    print(result.json())


def test_body_message():
    result = client.post('/messages/body/1',
                         json={
                             'message': 'hello',
                             'meta': {'a': [1,2,3]}
                         }
                         )
    assert result.status_code == 200
    result = client.get('/messages/1')
    print(result.json())



def test_body_message_error():
    result = client.post('/messages/body/1',
                         json={
                             'meta': {'a': [1,2,3]}
                         }
                         )
    assert result.status_code == 422
    print(result.json()) # missing message error



