# A Web Crawler from Scratch using Python

This repo implements a Python version of web crawler from scratch, i.e. without using any libraries for the purpose of web crawling.

## How to use

1. Clone this repo
2. Run the crawler by `python crawler.py -c [target_website]`

Note: this web crawler is developed and only tested in Python 2.7.10.

### Other usage

- `python crawler.py -test` to run the tests
- `python crawler.py -help` for a short help message

## Note on development

The final product is designed to be a command line tool which can be used as above. The system is decomposed to the command line file `crawler.py`, the core file `spider.py` and some helper functions `helper.py`. Also, the test file `test.py` is used for the test-driven development purpose. 

### How to crawl

In order to crawl, you firstly need to bend your knee ... wait, it's how to **crawl a web**.

OK, let's try again. In order to crawl a web, you need a **spider** - I'm not kidding this time. All you need to do is guide a spider to walk around the web.

The basic guide of web crawl for the spider is (BTW I promise I will not make any joke in the reamining contents)

1. Visit a website
2. Fetch all links from the website
3. Visit these links

But wait, if there is a **cycle**, i.e. website A contains a link to B and B contains a link to A as well, the crawl will never terminate (and our spider will die). So we also need to remember which websites we have already visited and avoid visiting them again - easy, just cache them somehow. So the complete flow would be

0. Put the first url to `to_vist`
1. Get one url from `to_visit` and add it to `visted`
2. Visit the url, fetch all links and add those neither `visted` nor `to_visit` to `to_visit`
3. Go back to 1 until `to_visit` is empty

### Parsing HTMLs

HTMLs are in form of strings, which is parsed by checking the `<a>` tag for links and every `href` attributes for static files. The parser will return a list of links in the target url.

#### Handling unexpected fail

In the development, there are some unexpected exceptions cacusing failure in handshake - these could be caused by unsuppoer SSL certificates or some websites not allowing web crawl. Such websites will be simply skipped in this web crawler.

### Processing URLs

URLs are needed to be processed for several purposes.

#### Unique keys

As we cache URLs using their string representation, we need make sure no stupid things like visiting `example.com` and `example.com/` both. A straightforward way to aovid this is always removing the last `/`.

Always, element jumpying with `#` doesn't change the content of the website - so removing them as well.

**Note**: parameter passing using `?` may change the content of website so they cannot be removed.

#### Within domain?

Ideally if the target URL is a root domain, I will suppose the user also want to visit its sub-domains. This check is done by regular expression matching in the source code.

#### Is static?

Static files detection is done by a manually written regular expression which aims to find some common static files like images, web source files and text files. 

### Testing

Tests can be run by either `python crawler.py -test` or `python test.py`.
