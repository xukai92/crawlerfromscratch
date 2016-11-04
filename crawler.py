# This is the main index file of the web crawler.
# It will run or test the web crawler according to the arguments from the command line.
# Author: Kai Xu
# Date: 04/11/2016

import sys  # for handling arguments

HELPMSG = "------------------Usage-----------------\n1. Crawl a website:\n    python crawler.py -t [target_website]\n2. Run tests:\n    python crawler.py -test\n3. Help:\n    python crawler.py -help"

def print_help(warning=False):
    if warning:
        print "-----------------Warning----------------\nArguments unrecoginized - please check the usage below"
    else:
        print "----------------------------------------\nWelcome to this web crawler coded by Kai"
    print HELPMSG

args = sys.argv[1:] # fetch the arguments; the first elements in sys.argv is this python file itself - so ignore

if len(args) == 1:
    if args[0] == "-test":
        print "[crawler.py] start testing"
        # call runtest.py
        print "[crawler.py] all tests pass"
    elif args[0] == "-help":
        print_help()
    else:
        print_help(True)
elif len(args) == 2:
    if args[0] == "-t":
        target_website = args[1]
        print "[crawler.py] start crawling"
        # call the main crawling routine
        print "[crawler.py] crawling done"
    else:
        print_help(True)
else:
    print_help(True)