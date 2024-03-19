from unittest.mock import patch
import unittest
from handlers import merge_requests


class TestMergeRequests(unittest.TestCase):
    @patch('requests.get')
    def test_merge_requests_none(self, get_mock):
        get_mock.return_value.json.return_value = [{"iid": 1, "title": "title", "web_url": "url"}]
        expected_res = [{"num": 1, "title": "title", "link": "url"}]
        res = merge_requests.get_merge_requests()
        self.assertEqual(res, expected_res)

    @patch('requests.get')
    def test_merge_requests_opened(self, get_mock):
        get_mock.return_value.json.return_value = [{"iid": 1, "title": "title", "web_url": "url"}]
        expected_res = [{"num": 1, "title": "title", "link": "url"}]
        res = merge_requests.get_merge_requests(state="opened")
        self.assertEqual(res, expected_res)

    @patch('requests.get')
    def test_merge_requests_verified(self, get_mock):
        get_mock.return_value.json.return_value = [
            {"iid": 1, "title": "title", "web_url": "url", "id": 1, "status": "success"}]
        expected_res = [{"num": 1, "title": "title", "link": "url"}]
        res = merge_requests.get_merge_requests(state="verified")
        self.assertEqual(res, expected_res)

    @patch('requests.get')
    def test_merge_requests_work(self, get_mock):
        get_mock.return_value.json.return_value = [
            {"title": "title", "iid": 1, "web_url": "url", "id": 1, "status": "failed"}]
        expected_res = [{"title": "title", "num": 1, "link": "url"}]
        res = merge_requests.get_merge_requests(state="needs work")
        self.assertEqual(res, expected_res)

    def setUp(self):
        '''Init'''

    def tearDown(self):
        '''Finish'''


if __name__ == "__main__":
    unittest.main()
