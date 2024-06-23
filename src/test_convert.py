from unittest import TestCase, main
from re import fullmatch

from convert import text_to_textnodes, textnodes_to_html, markdown_to_blocks

class TestTextConvert(TestCase):
    def test_each_type_to_textnodes(self):
        text = 'plain **bold** *italic* `code` [link anchor text](link href) ![image alt text](image src)'
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
    def test_markdown_to_blocks(self):
        text = '''
        # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.



* This is a list item
* This is another list item                     

This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
        '''
        blocks = markdown_to_blocks(text)
        self.assertEqual(len(blocks), 6)
        self.assertTrue(all(fullmatch(r'(?s)\S.*\S', block) for block in blocks))

if __name__ == '__main__':
    main()
