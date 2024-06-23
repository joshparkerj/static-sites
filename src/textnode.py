from enum import Enum

from leafnode import LeafNode

class TextNode:
 def __init__(self, text, text_type, url=None):
  self.text = text
  self.text_type = text_type
  self.url = url
  self.valid_types = ('text', 'bold', 'italic', 'code', 'link', 'image')
 
 def __eq__(self, other):
  return (
   self.text == other.text 
   and self.text_type == other.text_type
   and self.url == other.url)

 def __repr__(self):
  return f'TextNode({self.text}, {self.text_type}, {self.url})'

 def to_html_node(self):
     if not self.text_type in self.valid_types:
         raise Exception(f'invalid type! valid types are: {self.valid_types}')
     if self.text_type == 'text':
         return LeafNode(self.text)
     if self.text_type == 'bold':
         return LeafNode(self.text, 'b')
     if self.text_type == 'italic':
         return LeafNode(self.text, 'i')
     if self.text_type == 'code':
         return LeafNode(self.text, 'code')
     if self.text_type == 'link':
         return LeafNode(self.text, 'a', { 'href': self.url })
     if self.text_type == 'image':
         return LeafNode('', 'img', { 'src': self.url, 'alt': self.text })

