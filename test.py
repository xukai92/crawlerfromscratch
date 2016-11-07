# This is the test file for this web crawler.
# Author: Kai Xu
# Date: 05/11/2016


from helper import clean, get_domain, valid, contain_static
from spider import HTMLParser


class Test(object):
    def __init__(self):
        print "[Test] start testing"

    def test_clean(self):
        assert clean("http://google.com/#123123") == "http://google.com"
        assert clean("gocardless.com/") == "http://gocardless.com"
        print "[Test] test_clean() pass"

    def test_get_domain(self):
        assert get_domain("http://gocardless.com") == "gocardless.com"
        print "[Test] test_get_domain() pass"

    def test_valid(self):
        assert valid("http://google.com", "gocardless.com") is False
        assert valid("http://google.com/www.gocardless.com", "gocardless.com") is False
        assert valid("http://google.gocardless.com", "gocardless.com") is True
        assert valid("http://abc-ef.gocardless.com", "gocardless.com") is True
        print "[Test] test_valid() pass"

    def test_contain_static(self):
        assert contain_static("http://google.com/me.png") is True
        print "[Test] test_contain_static() pass"

    def test_HTMLParser_handle_starttag(self):
        parser = HTMLParser()
        parser.domain = ""
        parser.url = ""
        parser.urls = []
        f = open("view-source_https___gocardless.com.html", "r")
        parser.feed(f.read())
        f.close()
        print "[Test] test_HTMLParser_handle_starttag() pass"

    def test_all(self):
        self.test_clean()
        self.test_get_domain()
        self.test_valid()
        self.test_contain_static
        self.test_HTMLParser_handle_starttag()
        print "[Test] all tests pass"
        print "[Test] finish testing"


if __name__ == "__main__":
    test = Test()
    test.test_all()
