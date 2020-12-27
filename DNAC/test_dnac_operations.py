##  Refresher on unit testing
#  https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

import pytest
from dnac_operations import get_token, HTTPError

# EXAMPLE-1 testing without fixtures
def test_get_token_len():
    assert len(get_token()) == 722

def test_get_token_string():
    assert type(get_token()) == type("string")

def test_exception_on_non_tuple_argument():
    with pytest.raises(HTTPError):
        get_token("blah", "blah")
