from nose.tools import assert_true
import requests

def test_request_response():
    # send a request to the API server and store the response
    # There is no authentication required here.
    response = requests.get(url='http://jsonplaceholder.typicode.com/todos')\\

    # Confirm the request-response cycle completed successfully
    assert_true(response.ok)

