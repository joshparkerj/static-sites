from unittest import TestCase, main

from convert import text_to_textnodes, textnodes_to_html

class TestTextConvert(TestCase):
    def test_each_type_to_textnodes(self):
        text = 'plain *bold* **italic** `code` [link anchor text](link href) ![image alt text](image src)'
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 11)
        self.assertEqual(textnodes_to_html(nodes), 'plain <b>bold</b> <i>italic</i> <code>code</code> <a href="link href">link anchor text</a> <img src="image src" alt="image alt text"></img>')
    def test_empty_text_to_textnodes(self):
        text = ''
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(textnodes_to_html(nodes), '')
    def test_invalid_text_to_textnodes(self):
        text = 'hi there how* is it goin'
        self.assertRaises(Exception, text_to_textnodes, text)

if __name__ == '__main__':
    main()
