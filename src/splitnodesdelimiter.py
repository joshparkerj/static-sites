from functools import reduce

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return reduce(lambda acc, text_node: acc + text_node.split_on_delimiter(delimiter, text_type), old_nodes, [])

