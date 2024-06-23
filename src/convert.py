from re import split, sub

from textnode import TextNode
from textnodehelper import split_nodes_link, split_nodes_image, split_nodes_delimiter

def text_to_textnodes(text):
    link_splitted = split_nodes_link([TextNode(text, 'text')])
    image_splitted = split_nodes_image(link_splitted)
    code_splitted = split_nodes_delimiter(image_splitted, '`', 'code')
    bold_splitted = split_nodes_delimiter(code_splitted, '**', 'bold')
    italic_splitted = split_nodes_delimiter(bold_splitted, '*', 'italic')
    return italic_splitted 

def text_to_html_nodes(text):
    return textnodes_to_html_nodes(text_to_textnodes(text))

def textnodes_to_html_nodes(text_nodes):
    return [x.to_html_node() for x in text_nodes]

def textnodes_to_html(text_nodes):
    return ''.join(x.to_html() for x in textnodes_to_html_nodes(text_nodes))

def markdown_to_blocks(markdown):
    return [sub(r'(?m)^\s+', '', block) for block in split(r'\s*\n\s*\n\s*', markdown.strip())]
    
