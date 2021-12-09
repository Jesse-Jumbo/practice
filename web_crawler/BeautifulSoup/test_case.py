def ip_location(ip: str):
    temp = ip.rstrip(ip[ip.rfind(' ('):])
    return temp.lstrip(ip[:ip.rfind(': ')])

def test_ip_location():
    ip = "※ 發信站: 批踢踢實業坊(ptt.cc), 來自: 114.34.125.248 (臺灣)\n"
    assert ip_location(ip) == "114.34.125.248"


def comments_object_time(comment):
    return comment[comment.rfind("/")-2:]


def test_comments_time():
    comment = " 180.217.30.36 12/08 21:22"
    print(comments_object_time(comment))
    assert comments_object_time(comment) == "12/08 21:22"


def comments_object_ip(comment):
    return comment[1:comment.find(comments_object_time(comment))-1]


def test_comments_ip():
    comment = " 180.217.30.36 12/08 21:22"
    print(comments_object_ip(comment))
    assert comments_object_ip(comment) == "180.217.30.36"