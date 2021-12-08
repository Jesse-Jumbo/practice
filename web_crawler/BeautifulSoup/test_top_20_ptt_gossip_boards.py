import pytest
import requests

from top_20_ptt_gossip_boards import *

def response(url):
    res = requests.get(url)
    return res.status_code

def test_response():
    assert requests.codes.OK == response(url)