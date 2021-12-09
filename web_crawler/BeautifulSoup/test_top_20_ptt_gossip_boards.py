import pytest
import requests

from top_20_ptt_gossip_boards import *


def response(url):
    res = requests.get(url)
    return res.status_code

def test_response():
    assert requests.codes.OK == response(url)


def top_20_article_hyper_links(href):
    return href.status_code


def test_top_20_article_hyper_links():
    assert requests.codes.OK == top_20_article_hyper_links(the_article_link)


def ip_location(ip: str):
    temp = ip.rstrip(ip[ip.rfind(' ('):])
    return temp.lstrip(ip[:ip.rfind(': ')])


def test_ip_location():
    ip = "※ 發信站: 批踢踢實業坊(ptt.cc), 來自: 114.34.125.248 (臺灣)\n"
    assert ip_location(ip) == "114.34.125.248"



