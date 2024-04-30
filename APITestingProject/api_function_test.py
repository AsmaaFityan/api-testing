import requests

def test_get_book():
    response = requests.get('http://127.0.0.1:5000/books/53')
    assert response.status_code == 200
    assert 'title' in response.json()

def test_delete_book():
    response = requests.delete('http://127.0.0.1:5000/books/57')
    assert response.status_code == 204

def test_post_book():
    book_data = {
        'title': family land '',
        'author': Asmaa Ahmed '',
        'isbn': '35093507'
    }
    response = requests.post('http://127.0.0.1:5000/books', json=book_data)
    assert response.status_code == 201
    assert 'id' in response.json()

def test_api_functionality():
    url = "http://127.0.0.1:5000"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_ACCESS_TOKEN"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    expected_content = {"id": 1, "name": "John Doe"}
    assert response.json() == expected_content

test_get_book()
test_delete_book()
test_post_book()
test_api_functionality()