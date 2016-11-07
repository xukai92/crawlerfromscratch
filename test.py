# This is the test file for this web crawler.
# Author: Kai Xu
# Date: 05/11/2016


from spider import clean, valid, HTMLParser


class Test(object):
    def __init__(self):
        print "[Test] start testing"

    def test_clean(self):
        assert clean("http://google.com/#123123") == "http://google.com"
        assert clean("gocardless.com/") == "http://gocardless.com"
        print "[Test] test_clean() pass"

    def test_valid(self):
        assert valid("http://google.com") is False
        assert valid("http://google.com/www.gocardless.com") is False
        assert valid("http://google.gocardless.com") is True
        assert valid("http://abc-ef.gocardless.com") is True
        print "[Test] test_valid() pass"

    def test_HTMLParser_handle_starttag(self):
        parser = HTMLParser()
        parser.url = ""     # save root path
        parser.urls = []    # init return list
        f = open("view-source_https___gocardless.com.html", "r")
        parser.feed(f.read())
        f.close()
        print "[Test] HTMLParser.handle_starttag() pass"

    def test_all(self):
        self.test_clean()
        self.test_valid()
        self.test_HTMLParser_handle_starttag()
        print "[Test] all tests pass"
        print "[Test] finish testing"

    # TODO: add test cases for Spider


if __name__ == "__main__":
    test = Test()
    test.test_all()
