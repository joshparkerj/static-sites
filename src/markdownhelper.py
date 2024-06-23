from parentnode import ParentNode
from blockhelper import block_to_node
from convert import markdown_to_blocks

def markdown_to_html_node(markdown):
    top_level_node = ParentNode([
       block_to_node(block) 
       for block in
       markdown_to_blocks(markdown)
    ], 'div')
    return top_level_node

