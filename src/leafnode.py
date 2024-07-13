from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(value, tag, props, None) 

    def to_html(self):
        if self.tag:
            return f'<{self.tag}{self.props_to_html()}>{self.value if isinstance(self.value, str) else "".join(v.to_html_node().to_html() for v in self.value)}</{self.tag}>'
        return self.value
