from unittest import TestCase, main
from re import fullmatch

from convert import text_to_textnodes, textnodes_to_html, markdown_to_blocks


class TestTextConvert(TestCase):
    def test_each_type_to_textnodes(self):
        text = 'plain **bold** *italic* `code` [link anchor text](link href) ![image alt text](image src)'
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 10)
        self.assertEqual(textnodes_to_html(nodes), 'plain <b>bold</b> <i>italic</i> <code>code</code> <a href="link href">link anchor text</a> <img src="image src" alt="image alt text"></img>')

    def test_home_link(self):
        text = 'plain **bold** [Back Home](/)'
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 4)
        self.assertEqual(textnodes_to_html(nodes), 'plain <b>bold</b> <a href="/">Back Home</a>')

    def test_empty_text_to_textnodes(self):
        text = ''
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 0)
        self.assertEqual(textnodes_to_html(nodes), '')

    def test_invalid_text_to_textnodes(self):
        text = 'hi there how* is it goin'
        self.assertRaises(Exception, text_to_textnodes, text)

    def test_markdown_to_blocks(self):
        text = '''
        # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside.



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

    def test_headings(self):
        headings = '\n# First Heading\n\n ## Sub Heading\n'
        blocks = markdown_to_blocks(headings)
        self.assertEqual(len(blocks), 2)

    def test_link_with_underscore(self):
        text = 'look at this link [(it has an underscore in it)](https://lotr.fandom.com/wiki/Main_Page)'
        textnodes = text_to_textnodes(text)
        self.assertEqual(len(textnodes), 2)
        self.assertEqual(textnodes_to_html(textnodes), 'look at this link <a href="https://lotr.fandom.com/wiki/Main_Page">(it has an underscore in it)</a>')

    def test_emphasized_link(self):
        text = 'look at this link *(it is italicized) [here it is!](href)*'
        textnodes = text_to_textnodes(text)
        self.assertEqual(len(textnodes), 2)
        self.assertEqual(textnodes_to_html(textnodes), 'look at this link <i>(it is italicized) <a href="href">here it is!</a></i>')

    def test_link_with_emphasis(self):
        text = '[I am a link with an *emphasized* word](href)'
        text_nodes = text_to_textnodes(text)
        self.assertEqual(len(text_nodes), 1)
        self.assertEqual(textnodes_to_html(text_nodes), '<a href="href">I am a link with an <i>emphasized</i> word</a>')


if __name__ == '__main__':
    main()
