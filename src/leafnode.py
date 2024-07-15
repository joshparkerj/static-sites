from re import sub
from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None, in_code=False):
        super().__init__(value, tag, props, None)
        self.in_code = in_code

    def to_html(self):
        if self.tag:
            return f'<{self.tag}{self.props_to_html()}>{self.fix_whitespace() if isinstance(self.value, str) else "".join(v.to_html_node().to_html() for v in self.value)}</{self.tag}>'
        return self.fix_whitespace()

    def fix_whitespace(self):
        if self.tag == "code" or self.in_code:
            return self.value
        return sub(r"(\s+|\n\s*>)", " ", self.value)
