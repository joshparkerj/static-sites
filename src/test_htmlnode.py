from unittest import TestCase, main

from htmlnode import HTMLNode

tag = "p"
value = "hi"
children = []
props = {"class": "info"}


class TestHTMLNode(TestCase):
    def test_repr(self):
        node = HTMLNode(value, tag, props, children)
        self.assertEqual(
            str(node),
            f"HTMLNode (tag={tag}, value={value}, children={children}, props={props})",
        )

    def test_props(self):
        node = HTMLNode(value, tag, props, children)
        self.assertEqual(
            node.props_to_html(), ' class="info"'
        )  # Do not forget the leading space!

    def test_values(self):
        node = HTMLNode(value, tag, props, children)
        self.assertEqual(node.tag, tag)
        self.assertEqual(node.value, value)
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, props)

    def test_to_html(self):
        node = HTMLNode(value, tag, props, children)
        self.assertRaises(NotImplementedError, node.to_html)


if __name__ == "__main__":
    main()
