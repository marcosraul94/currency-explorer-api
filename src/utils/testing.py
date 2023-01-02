from unittest import TestCase
from src.common.app import session, context


class MockResponse:
    def __init__(self, response_data: dict):
        self.response_data = response_data

    def json(self) -> dict:
        return self.response_data


def mock_request_method(response_data: dict) -> MockResponse:
    mock_response = MockResponse(response_data)

    return mock_response


class E2ETest(TestCase):
    def setUp(self) -> None:
        with context():
            session.execute("""
            DELETE FROM bank;
            DELETE FROM exchange;
            """)
            session.commit()
