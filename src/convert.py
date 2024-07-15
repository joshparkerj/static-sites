from re import split, sub

from textnode import TextNode
from textnodehelper import split_nodes_link, split_nodes_image, split_nodes_delimiter


def parentify(text_node: TextNode):
    if isinstance(text_node.text, list):
        return TextNode(
            [parentify(node) for node in text_node.text],
            text_node.text_type,
            text_node.url,
        )
    textnodes = text_to_textnodes(text_node.text)
    if len(textnodes) > 1:
        return TextNode(textnodes, text_node.text_type, text_node.url)
    return text_node


def text_to_textnodes(text):
    link_splitted = split_nodes_link([TextNode(text, "text")])
    image_splitted = split_nodes_image(link_splitted)
    code_splitted = split_nodes_delimiter(image_splitted, "`", "code")
    bold_splitted = split_nodes_delimiter(code_splitted, "**", "bold")
    bold_resplitted = split_nodes_delimiter(bold_splitted, "__", "bold")
    italic_splitted = split_nodes_delimiter(bold_resplitted, "*", "italic")
    italic_resplitted = split_nodes_delimiter(italic_splitted, "_", "italic")
    if len(italic_resplitted) > 1:
        return [parentify(text_node) for text_node in italic_resplitted]
    return italic_resplitted


def text_to_html_nodes(text):
    return textnodes_to_html_nodes(text_to_textnodes(text))


def textnodes_to_html_nodes(text_nodes):
    return [x.to_html_node() for x in text_nodes]


def textnodes_to_html(text_nodes):
    return "".join(x.to_html() for x in textnodes_to_html_nodes(text_nodes))


def markdown_to_blocks(markdown):
    # handling headings as a special case for now
    markdown = sub(r"(?m)(^\s*#{1,6})", r"\n\1", markdown)
    return [
        sub(r"(?m)^\s+", "", block)
        for block in split(r"\s*\n\s*\n\s*", markdown.strip())
    ]
