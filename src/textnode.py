from leafnode import LeafNode

from texthelper import extract_markdown_images, extract_markdown_links

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
     if self.text_type not in self.valid_types:
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

 def split_on_delimiter(self, delimiter, text_type):
     if self.text_type != 'text':
         return [self]
     nodes = self.text.split(delimiter)
     if len(nodes) % 2 != 1:
         raise Exception('invalid Markdown syntax')
     return [TextNode(node, 'text' if i % 2 == 0 else text_type) for i, node in enumerate(nodes)]

 def split_image(self):
     if self.text_type != 'text':
         return [self]
     markdown_images = extract_markdown_images(self.text)
     nodes = [TextNode(self.text, 'text')]
     for markdown_image in markdown_images:
         node = nodes.pop()
         texts = node.text.split(markdown_image['md'])
         nodes += [TextNode(texts[0], 'text'), TextNode(markdown_image['alt'], 'image', markdown_image['src']), TextNode(texts[1], 'text')]
     return nodes

 def split_link(self):
     if self.text_type != 'text':
         return [self]
     markdown_links = extract_markdown_links(self.text)
     nodes = [TextNode(self.text, 'text')]
     for markdown_link in markdown_links:
         node = nodes.pop()
         texts = node.text.split(markdown_link['md'])
         nodes += [TextNode(texts[0], 'text'), TextNode(markdown_link['a_text'], 'link', markdown_link['href']), TextNode(texts[1], 'text')]
     return nodes

