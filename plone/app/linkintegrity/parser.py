from HTMLParser import HTMLParser


class LinkParser(HTMLParser):
    """ a simple html parser for link and image urls """
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
    
    def getLinks(self):
        """ return all links found during parsing """
        return tuple(self.links)
    
    def handle_starttag(self, tag, attrs):
        """ override the method to remember all links """
        if tag == 'a':
            self.links.extend(search_attr('href', attrs))
        if tag == 'img':
            self.links.extend(search_attr('src', attrs))
    

def search_attr(name, attrs):
    """ search named attribute in a list of attributes """
    for attr, value in attrs:
        if attr == name:
            return [value]
    return []


def extractLinks(data):
    """ parse the given html and return all links """
    parser = LinkParser()
    parser.feed(data)
    parser.close()
    return parser.getLinks()
