from re import search

from parentnode import ParentNode
from blockhelper import block_to_node
from convert import markdown_to_blocks


def markdown_to_html_node(markdown):
    top_level_node = ParentNode(
        [block_to_node(block) for block in markdown_to_blocks(markdown)], "div"
    )
    return top_level_node


def extract_title(markdown):
    title = search(r"(?m)^\s*#(?P<title>.*)$", markdown)
    if not title or not title.group("title"):
        raise Exception("all pages need a single h1 header")
    return title.group("title").strip()
