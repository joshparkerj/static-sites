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
 def invalid_type(self):
  node = TextNode('this is a div', 'div')
  self.assertRaises(Exception, node.to_html_node)
 # now testing split
 def test_split_bold_zero(self):
  node = TextNode('this is text', 'text')
  splitted = node.split_on_delimiter('*', 'bold')
  self.assertEqual(len(splitted), 1)
  self.assertEqual(''.join(x.to_html_node().to_html() for x in splitted), 'this is text')
 def test_split_bold_one(self):
     node = TextNode('this is *text', 'text')
     self.assertRaises(Exception, node.split_on_delimiter, '*', 'bold')
 def test_split_bold_two_edge(self):
     node = TextNode('this is *text*', 'text')
     splitted = node.split_on_delimiter('*', 'bold')
     self.assertEqual(len(splitted), 3)
     self.assertEqual(''.join(x.to_html_node().to_html() for x in splitted), 'this is <b>text</b>')
 def text_split_bold_two_mid(self):
     node = TextNode('this *is* text', 'text')
     splitted = node.split_on_delimiter('*', 'bold')
     self.assertEqual(len(splitted), 3)
     self.assertEqual(''.join(x.to_html_node().to_html() for x in splitted), 'this <b>is</b> text')
 def text_split_bold_two_start(self):
     node = TextNode('*this is* text', 'text')
     splitted = node.split_on_delimiter('*', 'bold')
     self.assertEqual(len(splitted), 3)
     self.assertEqual(''.join(x.to_html_node().to_html() for x in splitted), '<b>this is</b> text')
 def text_split_bold_three(self):
     node = TextNode('this *is *text*', 'text')
     self.assertRaises(Exception, node.split_on_delimiter, '*', 'bold')
 def text_split_bold_four(self):
     node = TextNode('th*is* is *te*xt', 'text')
     splitted = node.split_on_delimiter('*', 'bold')
     self.assertEqual(len(splitted), 5)
     self.assertEqual(''.join(x.to_html_node().to_html() for x in splitted), 'th<b>is</b> is <b>te</b>xt')
 def text_split_italic_six(self):
     node = TextNode('this **is** my **very** elegant **text!**', 'text')
     splitted = node.split_on_delimiter('**', 'italic')
     self.assertEqual(len(splitted), 7)
     self.assertEqual(''.join(x.to_html_node().to_html() for x in splitted), 'this <i>is</i> my <i>very</i> elegant <i>text!</i>')
 def text_split_code_four(self):
     node = TextNode('`this is code can\'t you tell?` now here is my non-code prose... `(code again)`', 'text')
     splitted = node.split_on_delimiter('`', 'code')
     self.assertEqual(len(splitted), 5)
     self.assertEqual(''.join(x.to_html_node().to_html() for x in splitted), '<code>this is code can\'t you tell?</code> now here is my non-code prose... <code>(code again)</code>')
 
if __name__ == '__main__':
 main()
