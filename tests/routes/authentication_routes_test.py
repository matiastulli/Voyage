import unittest
import json
from voyage import app  # Assuming your Flask app is created and imported as 'app'

class TestAuthenticationRoutes(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()

    def test_register(self):
        data = {
            # Add the required data for the registration endpoint
            # Example: 'username': 'example_user',
            #          'password': 'example_password'
        }
        response = self.app.post('/register', json=data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)  # Adjust the status code as per your implementation

    def test_login(self):
        data = {
            # Add the required data for the login endpoint
            # Example: 'username': 'example_user',
            #          'password': 'example_password'
        }
        response = self.app.post('/login', json=data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)  # Adjust the status code as per your implementation

if __name__ == '__main__':
    unittest.main()
