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
 
if __name__ == '__main__':
 main()
