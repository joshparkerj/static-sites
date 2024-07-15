from re import fullmatch, finditer, match, sub

from parentnode import ParentNode
from convert import text_to_html_nodes


def block_to_block_type(block):
    if fullmatch(r"(?s)#{1,6} \w.*", block):
        return "heading"
    if fullmatch(r"(?s)```.*```", block):
        return "code"
    if fullmatch(r">.*(\n>.*)*", block):
        return "quote"
    if fullmatch(r"[-\*] .*(\n[-\*] .*)*", block):
        return "unordered_list"
    if fullmatch(r"\d+\. .*(\n\d+\. .*)*", block) and all(
        m.group(0) == str(i + 1) for i, m in enumerate(finditer(r"(?m)^\d+", block))
    ):
        return "ordered_list"
    return "paragraph"


def block_to_node(block):
    block_type = block_to_block_type(block)
    if block_type == "heading":
        return heading_block_to_node(block)
    if block_type == "code":
        return code_block_to_node(block)
    if block_type == "quote":
        return quote_block_to_node(block)
    if block_type == "unordered_list":
        return unordered_list_block_to_node(block)
    if block_type == "ordered_list":
        return ordered_list_block_to_node(block)
    if block_type == "paragraph":
        return paragraph_block_to_node(block)
    raise Exception("block type not found")


def heading_block_to_node(block):
    heading_number = len(match(r"#+", block).group(0))
    text_content = block[heading_number:].strip()
    return ParentNode(text_to_html_nodes(text_content), f"h{heading_number}")


def code_block_to_node(block):
    text_content = sub(r"```", "", block).strip()
    return ParentNode(
        [ParentNode(text_to_html_nodes(text_content, in_code=True), "code")], "pre"
    )


def quote_block_to_node(block):
    text_content = sub(r"(?m)^>\s*", "", block).strip()
    return ParentNode(text_to_html_nodes(text_content), "blockquote")


def unordered_list_block_to_node(block):
    list_items = [
        ParentNode(text_to_html_nodes(list_item.group(1).strip()), "li")
        for list_item in finditer(r"(?m)[-\*](.*)$", block)
    ]
    return ParentNode(list_items, "ul")


def ordered_list_block_to_node(block):
    list_items = [
        ParentNode(text_to_html_nodes(list_item.group(1).strip()), "li")
        for list_item in finditer(r"(?m)\d+\.(.*)$", block)
    ]
    return ParentNode(list_items, "ol")


def paragraph_block_to_node(block):
    html_nodes = text_to_html_nodes(block)
    return ParentNode(html_nodes, "p")
