from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, children, tag, props=None):
        super().__init__(None, tag, props, children)
    def to_html(self):
        if not self.tag:
            raise ValueError('tag is required in parent node')
        if not self.children:
            raise ValueError('children are required in parent node')
        return f'<{self.tag}{self.props_to_html()}>{''.join(child.to_html() for child in self.children)}</{self.tag}>'
