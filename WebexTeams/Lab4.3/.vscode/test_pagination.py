#!/bin/env python3

# Testing pagination on Webex Teams API. Created mock requests module in mock requests.py
# First we provided a precoded example of an API call to webex teams (mocked).
# A rel="next" header will be present if another page of results is available.
# We will use the 'bbeforeMessage' cursor (which points to a message id), not 'before' (which is a date cursor)

from lib import mock_requests
from messenger import Messenger
import unittest
from pprint import pprint
import json

class MessageTest(unittest.TestCase):
    def setUp(self):
        self.msg = Messenger(requests=mock_requests)

    def test_get_messages(self):
        # check if any messages exist
        pass

    def test_has_next_page(self):
        # Chcek if there are more pages of messages available
        pass

    def test_get_next_page(self):
        # Get the first page

        # Get the next page
        pass
