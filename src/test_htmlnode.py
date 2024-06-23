from unittest import TestCase, main

from htmlnode import HTMLNode

tag = "p"
value = "hi"
children = []
props = { "class": "info" }

class TestHTMLNode(TestCase):
    def test_repr(self):
        node = HTMLNode(value, tag, props, children)
        self.assertEqual(str(node), f'HTMLNode (tag={tag}, value={value}, children={children}, props={props})')
    def test_props(self):
        node = HTMLNode(value, tag, props, children)
        self.assertEqual(node.props_to_html(), ' class="info"') # Do not forget the leading space!

if __name__ == '__main__':
    main()
