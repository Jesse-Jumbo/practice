import crawl_news
import pytest


def reporters():
    all_reporters = []
    for news in crawl_news.save_news:
        all_reporters.append(news['reporter'])
    return all_reporters

def test_reporter():
    for reporter in reporters():
        assert len(reporter) == 3


def parse_reporter_name(origin_text:str):
    if "記者" in origin_text:
        return origin_text.lstrip("記者").rstrip(origin_text[origin_text.find('／'):])
    else:
        return origin_text.lstrip(origin_text[:origin_text.find('／')+1])



def test_parse_reporter_name():
    origin_text =""
    assert "" == parse_reporter_name(origin_text)
    assert "蔡玟君" == parse_reporter_name("記者蔡玟君／綜合報導")
    assert "a蔡玟君" == parse_reporter_name("記者a蔡玟君／綜合報導")
    assert "台南先生" == parse_reporter_name("文、圖／台南先生")