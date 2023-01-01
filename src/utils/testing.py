class MockResponse:
    def __init__(self, response_data: dict):
        self.response_data = response_data

    def json(self) -> dict:
        return self.response_data


def mock_request_method(response_data: dict) -> MockResponse:
    mock_response = MockResponse(response_data)

    return mock_response
