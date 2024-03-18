"""Write your code here"""
import os

TOKEN = os.getenv("TOKEN")
HEADERS = {'Authorization': f'Bearer {TOKEN}'}


def get_merge_requests(state=None):
    """
    Example of return:
    [
        {"title": "Homework1", "num": 56, "link": "https://google.com"},
        {"title": "Homework2", "num": 57, "link": "https://tut.by"},
    ]
    """

    return []
