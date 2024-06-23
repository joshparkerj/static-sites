from re import split

from textnode import TextNode
from textnodehelper import split_nodes_link, split_nodes_image, split_nodes_delimiter

def text_to_textnodes(text):
    link_splitted = split_nodes_link([TextNode(text, 'text')])
    image_splitted = split_nodes_image(link_splitted)
    code_splitted = split_nodes_delimiter(image_splitted, '`', 'code')
    italic_splitted = split_nodes_delimiter(code_splitted, '**', 'italic')
    bold_splitted = split_nodes_delimiter(italic_splitted, '*', 'bold')
    return bold_splitted

def textnodes_to_html(text_nodes):
    return ''.join(x.to_html_node().to_html() for x in text_nodes)

def markdown_to_blocks(markdown):
    return split(r'\s*\n\s*\n\s*', markdown.strip())
    
