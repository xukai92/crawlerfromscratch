from spider import clean, valid

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

    def test_all(self):
        self.test_clean()
        self.test_valid()
        print "[Test] all tests pass"
        print "[Test] finish testing"


if __name__ == "__main__":
    test = Test()
    test.test_all()
