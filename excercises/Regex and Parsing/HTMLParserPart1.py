from html.parser import HTMLParser


def print_attributes(attrs):
    for name, value in attrs:
        print("->", name, ">", value)


class MyHTMLParser(HTMLParser):
    def error(self, message):
        print(message)

    def handle_starttag(self, tag, attrs):
        print("{0:6s}: {1:s}".format("Start", tag))
        print_attributes(attrs)

    def handle_endtag(self, tag):
        print("{0:6s}: {1:s}".format("End", tag))

    def handle_startendtag(self, tag, attrs):
        print("{0:6s}: {1:s}".format("Empty", tag))
        print_attributes(attrs)


# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

for _ in range(int(input())):
    parser.feed(input())
