def ip_location(ip: str):
    temp = ip.rstrip(ip[ip.rfind(' ('):])
    return temp.lstrip(ip[:ip.rfind(': ')])

def test_ip_location():
    ip = "※ 發信站: 批踢踢實業坊(ptt.cc), 來自: 114.34.125.248 (臺灣)\n"
    assert ip_location(ip) == "114.34.125.248"
    ip = "※ 發信站: 批踢踢實業坊(ptt.cc), 來自: 1.200.57.2 (臺灣)\n"
    assert ip_location(ip) == "1.200.57.2"
    ip = "※ 發信站: 批踢踢實業坊(ptt.cc), 來自: 114.136.92.77 (臺灣)\n"
    assert ip_location(ip) == "114.136.92.77"


def comments_object_time(comment):
    return comment[comment.rfind("/")-2:-1]


def test_comments_time():
    comment = " 180.217.30.36 12/08 21:22\n"
    assert comments_object_time(comment) == "12/08 21:22"
    comment = " 1.168.238.130 12/08 21:23\n"
    assert comments_object_time(comment) == "12/08 21:23"
    comment = " 219.85.10.242 12/08 21:24\n"
    assert comments_object_time(comment) == "12/08 21:24"


def comments_object_ip(comment):
    return comment[1:comment.find(comments_object_time(comment))-1]


def test_comments_ip():
    comment = " 180.217.30.36 12/08 21:22"
    assert comments_object_ip(comment) == "180.217.30.36"
    comment = " 1.168.238.130 12/08 21:22"
    assert comments_object_ip(comment) == "1.168.238.130"
    comment = " 219.85.10.242 12/08 21:22"
    assert comments_object_ip(comment) == "219.85.10.242"


def context_reset(context):
    return context[2:]


def test_context():
    context = ": 不熟啦 哪次熟了"
    assert context_reset(context) == "不熟啦 哪次熟了"
    context = ": 三國無雙"
    assert context_reset(context) == "三國無雙"
    context = ": 哇三立耶 切切切起來"
    assert context_reset(context) == "哇三立耶 切切切起來"


def reply_reset(reply):
    if "推" in reply:
        return "推"
    if "→" in reply:
        return "→"
    if "噓" in reply:
        return "噓"


def test_reply():
    reply_1 = "898推"
    assert reply_reset(reply_1) == "推"
    reply_2 = "89→"
    assert reply_reset(reply_2) == "→"
    reply_3 = "98噓"
    assert reply_reset(reply_3) == "噓"