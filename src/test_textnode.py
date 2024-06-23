from unittest import TestCase, main

from textnode import TextNode

text = 'This is a text node'
text_type = 'bold'

class TestTextNode(TestCase):
 def test_eq(self):
  node = TextNode(text, text_type)
  node2 = TextNode(text, text_type)
  self.assertEqual(node, node2)
 def test_not_eq_url(self):
  node = TextNode(text, text_type)
  node2 = TextNode(text, text_type, 'boot.dev')
  self.assertNotEqual(node, node2)
 def test_eq_url(self):
  url = 'https://www.crummy.com/software/BeautifulSoup/'
  node = TextNode(text, text_type, url)
  node2 = TextNode(text, text_type, url)
  self.assertEqual(node, node2)
 def test_not_eq_text(self):
  node = TextNode(text, text_type)
  node2 = TextNode(text + 'lol', text_type)
  self.assertNotEqual(node, node2)
 def test_not_eq_text_type(self):
  node = TextNode(text, text_type)
  node2 = TextNode(text, text_type + 'jk')
  self.assertNotEqual(node, node2)
 # Now testing the to_html method
 def test_plain_text(self):
  node = TextNode('this is a text node', 'text')
  self.assertEqual(node.to_html_node().to_html(), 'this is a text node')
 def test_bold_text(self):
  node = TextNode('this is a bold node', 'bold')
  self.assertEqual(node.to_html_node().to_html(), '<b>this is a bold node</b>')
 def test_italic_text(self):
  node = TextNode('this is an italicized node', 'italic')
  self.assertEqual(node.to_html_node().to_html(), '<i>this is an italicized node</i>')
 def test_code_node(self):
  node = TextNode('this is a code node', 'code')
  self.assertEqual(node.to_html_node().to_html(), '<code>this is a code node</code>')
 def test_link(self):
  node = TextNode('this is a link', 'link', 'https://site.co/')
  self.assertEqual(node.to_html_node().to_html(), '<a href="https://site.co/">this is a link</a>')
 def test_image(self):
  node = TextNode('this is an image', 'image', 'https://www.crummy.com/software/BeautifulSoup/10.1.jpg')
  self.assertEqual(node.to_html_node().to_html(), '<img src="https://www.crummy.com/software/BeautifulSoup/10.1.jpg" alt="this is an image"></img>')
 
if __name__ == '__main__':
 main()
