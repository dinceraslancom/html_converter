""" A converter for HTML """

import json
import pprint

from html.parser import HTMLParser
from html5lib.serializer import serialize as html5lib_serialize
from html5lib.html5parser import parse
from typing import Union


class CostumeObject(object):
    """ Created to provide special abilities. """

    def pretty_print(self, indent=4) -> None:
        pprint.PrettyPrinter(indent=indent).pprint(self)

    def to_dict(self) -> Union['CostumeList', 'CostumeDict']:
        return self

    def to_json(self) -> str:
        return json.dumps(self)

    def to_str(self):
        raise NotImplementedError


class CostumeList(list, CostumeObject):
    """ Created to provide special abilities. """

    def to_str(self) -> str:
        return ' '.join(i['text'] + i['inner'].to_str() for i in self)


class CostumeDict(dict, CostumeObject):
    """ Created to provide special abilities. """

    def to_str(self) -> str:
        return self['text'] + ' '.join(
            i['text'] + i['inner'].to_str() for i in self['inner'])


class Node:
    """ Created to connect nodes. """

    __slots__ = ('current', 'previous',)

    def __init__(self, current, previous):
        self.current = current
        self.previous = previous


class HtmlSerializer:
    def __init__(self, html):
        """ Closes open tags. """

        token_stream = parse(html)
        self.data = html5lib_serialize(token_stream, omit_optional_tags=False)


class HtmlToDictParser(HTMLParser):
    """ Convert from html to dict. """

    def __init__(self):
        super(HtmlToDictParser, self).__init__()

        self.tree = CostumeList()
        self.node = CostumeList()

    @staticmethod
    def parse_attr(attrs: tuple) -> dict:
        """ Parse attributes. """

        _attrs = {}
        for attr in attrs:
            attribute, value = attr
            if attribute == 'class':
                _attrs[attribute] = value.split()
            else:
                _attrs[attribute] = value
        return _attrs

    def make_tag(self, tag: str, attrs: tuple) -> dict:
        """ Create dict tags. """

        return CostumeDict({
            'tag': tag,
            'attrs': self.parse_attr(attrs),
            'text': '',
            'inner': CostumeList()
        })

    def handle_starttag(self, tag, attrs) -> None:
        """ Go to the next node. """

        node = self.tree if not self.tree else self.node.current
        node.append(self.make_tag(tag, attrs))
        self.node = Node(current=node[-1]['inner'], previous=self.node)

    def handle_endtag(self, tag) -> None:
        """ Go back to the previous node. """

        self.node = self.node.previous

    def handle_data(self, data) -> None:
        """ Add the tag text attribute. """
        self.node.previous.current[-1]['text'] = data.strip()

    def handle_comment(self, data) -> None:
        """ Add the tag comment attribute. """

        self.node.previous.current[-1]['comment'] = data

    def __reset(self) -> None:
        self.tree = CostumeList()
        self.node = CostumeList()

    def process(self, html: str) -> CostumeList:
        """ Convert from html to dict.

        Args:
          html: A html text.

        Returns:
          The created dict.

        """

        self.feed(data=html)
        self.close()
        result = self.tree
        self.__reset()
        return result


class HtmlToDict(object):
    """ Convert from html to dict.

    To use:
    >>> html_data = '<html><head><title>Test</title></head><body></body></html>'
    >>> converter = HtmlToDict()
    >>> converter.convert(html_data)
    [{'tag': 'html', 'attrs': {}, 'text': '', 'inner': [{'tag': 'head', 'attrs': {}, 'text': '', 'inner': [{'tag': 'title', 'attrs': {}, 'text': 'Test', 'inner': []}]}, {'tag': 'body', 'attrs': {}, 'text': '', 'inner': []}]}]

    """

    service_klass = HtmlToDictParser
    serializer_klass = HtmlSerializer

    def convert(self, html: str, serialize: bool = True) -> CostumeList:
        """ Convert from html to dict.

        Args:
          html: An html text.
          serialize: An html serialization setting, use False for faster performance.

        Returns:
          The created item.

        """
        if serialize:
            html = self.serializer_klass(html).data
        return self.service_klass().process(html)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
