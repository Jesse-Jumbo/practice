import pytest
import requests

from top_20_ptt_gossip_boards import *

def response(url):
    res = requests.get(url)
    return res.status_code

def test_response():
    assert requests.codes.OK == response(url)


def top_20_article_hyper_links(href):
    # hyper_links = requests.get(href.get('href'))
    return href.status_code


def test_top_20_article_hyper_links():
    assert requests.codes.OK == top_20_article_hyper_links(the_top_20_article_hyper_links)