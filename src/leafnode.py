from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(value, tag, props, None) 
    def to_html(self):
        if not isinstance(self.value, str) or len(self.value) < 1:
            raise ValueError('All leaf nodes require a value!')
        if self.tag:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        return self.value
