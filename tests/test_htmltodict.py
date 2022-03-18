import unittest

from html_converter import HtmlToDict


class HtmlToDictTestCase(unittest.TestCase):
    def setUp(self) -> None:
        html_data = None
        with open('test_files/test_html_to_dict.html') as file:
            html_data = file.read()
        self.converter = HtmlToDict()
        self.result = self.converter.convert(html_data)

    def test_parse_text(self):
        self.assertEqual(self.result, [{'attrs': {},
                                        'inner': [{'attrs': {},
                                                   'inner': [{'attrs': {},
                                                              'inner': [],
                                                              'tag': 'title',
                                                              'text': 'Test'}],
                                                   'tag': 'head',
                                                   'text': ''},
                                                  {'attrs': {},
                                                   'inner': [{'attrs': {
                                                       'class': ['class1',
                                                                 'class2'],
                                                       'none_attr': ''},
                                                       'inner': [],
                                                       'tag': 'h1',
                                                       'text': 'Parse me! 1'},
                                                       {'attrs': {},
                                                        'inner': [],
                                                        'tag': 'h2',
                                                        'text': 'Parse me! 2'}],
                                                   'tag': 'body',
                                                   'text': ''}],
                                        'tag': 'html',
                                        'text': ''}])

    def test_to_str(self):
        self.assertEqual(self.result.to_str(), 'Test Parse me! 1 Parse me! 2')
