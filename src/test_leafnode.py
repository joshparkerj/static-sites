from unittest import TestCase, main

from leafnode import LeafNode

class TestLeafNode(TestCase):
    def test_p(self):
        node = LeafNode('This is a paragraph of text.', 'p')
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')
    def test_a(self):
        node = LeafNode('Click Me!', 'a', {'href': 'https://www.google.com'})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click Me!</a>')
    def test_text(self):
        node = LeafNode('just text')
        self.assertEqual(node.to_html(), 'just text')
    def test_b(self):
        node = LeafNode('an emphasized text', 'b', {'class':'emphasis', 'id': 'emphasized-text'})
        self.assertEqual(node.to_html(), '<b class="emphasis" id="emphasized-text">an emphasized text</b>')

if __name__ == '__main__':
    main()
