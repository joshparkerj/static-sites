class HTMLNode:
    def __init__(self, value=None, tag=None, props=None, children=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("implement me")

    def props_to_html(self):
        if self.props:
            return "".join(f' {key}="{self.props[key]}"' for key in self.props)
        return ""

    def __repr__(self):
        return f"HTMLNode (tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
