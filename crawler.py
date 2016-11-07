# This is the main index file of the web crawler.
# It will run or test the web crawler according to the arguments from the command line.
# Author: Kai Xu
# Date: 04/11/2016


import sys  # for handling arguments
from spider import Spider
from test import Test


HELPMSG = ("----------------- Usage ----------------\n"
           "1. Crawl a website:\n"
           "    python crawler.py -c [target_website]\n"
           "2. Run tests:\n"
           "    python crawler.py -test\n"
           "3. Help:\n"
           "    python crawler.py -help\n"
           "----------------------------------------\n")


def print_help(warning=False):
    if warning:
        print "---------------- Warning ---------------"
        print "Arguments unrecoginized, plz check usage"
    else:
        print "----------------------------------------"
        print "Welcome to this web crawler coded by Kai"
    print HELPMSG


def main():
    # Fetch the arguments; the first elements in sys.argv is this python file itself - so ignore
    args = sys.argv[1:]

    # Execute function depending on arguments
    if len(args) == 1:
        if args[0] == "-test":      # test
            test = Test()
            test.test_all()
        elif args[0] == "-help":    # help
            print_help()
        else:
            print_help(True)
    elif len(args) == 2:
        if args[0] == "-c":         # crawl
            url = args[1]
            print "[crawler.py] start crawling"
            spider = Spider()
            spider.crawl(url)
            print "[crawler.py] crawling done"
        else:
            print_help(True)
    else:
        print_help(True)


if __name__ == "__main__":
    main()
