HTML Converter Tool
--------------------

Support Html to Dict, JSON, Str


Installing
------------

Install and update using `pip3`_:

.. code-block:: text

    $ pip3 install html_converter

Python 3 and newer.

.. _pip3: https://pip.pypa.io/en/stable/quickstart/


Simple Usage
----------------

.. code-block:: python

    if __name__ == '__main__':
        import pprint
        from html_converter import HtmlToDict

        html_data = '<html><body>test text</body></html>'
        converter = HtmlToDict()
        data = converter.convert(html_data, serialize=False)

        pp = pprint.PrettyPrinter(indent=1)
        pp.pprint(converter.convert(html_data, serialize=False).to_dict())
        [{'attrs': {},
          'inner': [{'attrs': {}, 'inner': [], 'tag': 'body', 'text': 'test text'}],
          'tag': 'html',
          'text': ''}]

        print(converter.convert(html_data, serialize=False).to_json())
        '[{"tag": "html", "attrs": {}, "text": "", "inner": [{"tag": "body", "attrs": {}, "text": "fd", "inner": []}]}]'

        print(converter.convert(html_data).to_str())
        test text

Support
---------

*   Python 3.x
*   Supports all operating systems

Links
-------

*   License: `MIT License <https://github.com/dinceraslancom/html_converter/blob/master/LICENSE>`_
*   Code: https://github.com/dinceraslancom/html_converter
