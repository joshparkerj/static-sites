from functools import reduce
from textnode import TextNode
from operator import countOf


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):
    try:
        return reduce(
            lambda acc, text_node: acc
            + text_node.split_on_delimiter(delimiter, text_type),
            old_nodes,
            [],
        )
    except:
        nodes_to_split = (
            (node, i)
            for i, node in enumerate(old_nodes)
            if countOf(node.text, delimiter) % 2 == 1
        )
        first_node_to_split, first_idx = next(nodes_to_split)
        second_node_to_split, second_idx = next(nodes_to_split)
        first_split = first_node_to_split.text.split(delimiter)
        second_split = second_node_to_split.text.split(delimiter)
        first_type = first_node_to_split.text_type
        second_type = second_node_to_split.text_type
        first_url = first_node_to_split.url
        second_url = second_node_to_split.url
        return split_nodes_delimiter(
            old_nodes[:first_idx]
            + [TextNode(text, first_type, first_url) for text in first_split[:-1]]
            + [
                TextNode(
                    [TextNode(first_split[-1], first_type, first_url)]
                    + old_nodes[first_idx + 1 : second_idx]
                    + [TextNode(second_split[0], second_type, second_url)],
                    text_type,
                )
            ]
            + [TextNode(text, second_type, second_url) for text in second_split[1:]]
            + old_nodes[second_idx + 1 :],
            delimiter,
            text_type,
        )


def split_nodes_image(old_nodes):
    return reduce(lambda acc, text_node: acc + text_node.split_image(), old_nodes, [])


def split_nodes_link(old_nodes):
    return reduce(lambda acc, text_node: acc + text_node.split_link(), old_nodes, [])
