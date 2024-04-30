import unittest
from app import app

class LibraryAPIValidationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True

    def test_update_nonexistent_book(self):
        response = self.app.put('/books/999', json={'title': 'Updated Book', 'author': 'Author Name', 'isbn': '123456'})
        self.assertEqual(response.status_code, 404)

    def test_delete_nonexistent_book(self):
        response = self.app.delete('/books/999')
        self.assertEqual(response.status_code, 404)

    def test_get_book_unauthorized(self):
        response = self.app.get('/books/1', headers={'Authorization': 'InvalidToken'})
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
