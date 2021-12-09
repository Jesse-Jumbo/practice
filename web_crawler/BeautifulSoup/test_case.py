def ip_location(ip: str):
    temp = ip.rstrip(ip[ip.rfind(' ('):])
    return temp.lstrip(ip[:ip.rfind(': ')])

def test_ip_location():
    ip = "※ 發信站: 批踢踢實業坊(ptt.cc), 來自: 114.34.125.248 (臺灣)\n"
    assert ip_location(ip) == "114.34.125.248"


def comments_object_time(comment):
    return comment[comment.rfind("/")-2:-1]


def test_comments_time():
    comment = " 180.217.30.36 12/08 21:22\n"
    print(comments_object_time(comment))
    assert comments_object_time(comment) == "12/08 21:22"


def comments_object_ip(comment):
    return comment[1:comment.find(comments_object_time(comment))-1]


def test_comments_ip():
    comment = " 180.217.30.36 12/08 21:22"
    print(comments_object_ip(comment))
    assert comments_object_ip(comment) == "180.217.30.36"


def context_reset(context):
    return context[2:]


def test_context():
    context = ": 不熟啦 哪次熟了"
    assert context_reset(context) == "不熟啦 哪次熟了"


def reply_reset(reply):
    good_reply = ''.join([x for x in reply if not x.isdigit()])
    return good_reply


def test_reply():
    reply = "898推"
    assert reply_reset(reply) == "推"