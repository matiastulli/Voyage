import pytest
from unittest.mock import patch, MagicMock
from flask import Flask, request
from app.controllers.user_controller import UserController
from app.schemas.user import User
from app.controllers.database_controller import database_controller

# Mocking the Flask app for testing
@pytest.fixture
def app():
    app = Flask(__name__)
    return app

class TestUserController:

    @patch('app.controllers.user_controller.database_controller')
    def test_profile(self, mock_database_controller, app):
        with app.test_request_context('/?mail=example@example.com'):
            # Mocking the database session
            session_mock = MagicMock()
            user_mock = User('example@example.com')
            session_mock.query().filter_by().first.return_value = user_mock
            mock_database_controller.new_session.return_value = session_mock

            # Initialize the UserController and call the method
            user_controller = UserController()
            result = user_controller.profile()

            # Assertions
            assert result.mail == 'example@example.com'

            # Verify that the database methods were called with the appropriate arguments
            mock_database_controller.new_session.assert_called_once()
            session_mock.query.assert_called_once_with(User)
            session_mock.query().filter_by.assert_called_once_with(mail='example@example.com')
            session_mock.close.assert_called_once()

