from unittest import TestCase, main

from textnodehelper import split_nodes_delimiter, split_nodes_image, split_nodes_link
from convert import textnodes_to_html
from textnode import TextNode


class TestSplitNodesDelimiter(TestCase):
    def test_split_nodes_delimiter(self):
        original_text = "**Hi!** It's a *very* good, **valid** and *well-thought-out* Markdown! (a `code` language, used for `formatting`.) Let's **see**!"
        original_node = TextNode(original_text, "text")
        italic_splitted = split_nodes_delimiter([original_node], "**", "italic")
        self.assertEqual(len(italic_splitted), 6)
        self.assertEqual(
            textnodes_to_html(italic_splitted),
            "<i>Hi!</i> It's a *very* good, <i>valid</i> and *well-thought-out* Markdown! (a `code` language, used for `formatting`.) Let's <i>see</i>!",
        )

        bold_splitted = split_nodes_delimiter(italic_splitted, "*", "bold")
        self.assertEqual(len(bold_splitted), 10)
        actual_bold_html = textnodes_to_html(bold_splitted)
        expected_bold_html = "<i>Hi!</i> It's a <b>very</b> good, <i>valid</i> and <b>well-thought-out</b> Markdown! (a `code` language, used for `formatting`.) Let's <i>see</i>!"
        self.assertEqual(actual_bold_html, expected_bold_html)

        code_splitted = split_nodes_delimiter(bold_splitted, "`", "code")
        self.assertEqual(len(code_splitted), 14)
        actual_code_html = textnodes_to_html(code_splitted)
        expected_code_html = "<i>Hi!</i> It's a <b>very</b> good, <i>valid</i> and <b>well-thought-out</b> Markdown! (a <code>code</code> language, used for <code>formatting</code>.) Let's <i>see</i>!"
        self.assertEqual(actual_code_html, expected_code_html)

    def test_split_nodes_image(self):
        original_text = "*a* ![b](c) *c*"
        original_node = TextNode(original_text, "text")
        image_splitted = split_nodes_image([original_node])
        self.assertEqual(len(image_splitted), 3)
        self.assertEqual(
            textnodes_to_html(image_splitted), '*a* <img src="c" alt="b"></img> *c*'
        )

    def test_split_nodes(self):
        original_text = "![a](b) [c](d) *e* `f` `g` ![h](i) ![j](k) `l` **m** **n** *o* `p` ![q](r) `s` ![t](u) [v](w) ![x](y) `z`"
        original_node = TextNode(original_text, "text")
        image_splitted = split_nodes_image([original_node])
        self.assertEqual(len(image_splitted), 13)
        actual_image_html = textnodes_to_html(image_splitted)
        expected_image_html = '<img src="b" alt="a"></img> [c](d) *e* `f` `g` <img src="i" alt="h"></img> <img src="k" alt="j"></img> `l` **m** **n** *o* `p` <img src="r" alt="q"></img> `s` <img src="u" alt="t"></img> [v](w) <img src="y" alt="x"></img> `z`'
        self.maxDiff = None
        self.assertEqual(actual_image_html, expected_image_html)

        italic_splitted = split_nodes_delimiter(image_splitted, "**", "italic")
        self.assertEqual(len(italic_splitted), 16)
        actual_italic_html = textnodes_to_html(italic_splitted)
        expected_italic_html = '<img src="b" alt="a"></img> [c](d) *e* `f` `g` <img src="i" alt="h"></img> <img src="k" alt="j"></img> `l` <i>m</i> <i>n</i> *o* `p` <img src="r" alt="q"></img> `s` <img src="u" alt="t"></img> [v](w) <img src="y" alt="x"></img> `z`'
        self.assertEqual(actual_italic_html, expected_italic_html)

        code_splitted = split_nodes_delimiter(italic_splitted, "`", "code")
        self.assertEqual(len(code_splitted), 27)
        actual_code_html = textnodes_to_html(code_splitted)
        expected_code_html = '<img src="b" alt="a"></img> [c](d) *e* <code>f</code> <code>g</code> <img src="i" alt="h"></img> <img src="k" alt="j"></img> <code>l</code> <i>m</i> <i>n</i> *o* <code>p</code> <img src="r" alt="q"></img> <code>s</code> <img src="u" alt="t"></img> [v](w) <img src="y" alt="x"></img> <code>z</code>'
        self.assertEqual(actual_code_html, expected_code_html)

        link_splitted = split_nodes_link(code_splitted)
        self.assertEqual(len(link_splitted), 31)
        actual_link_html = textnodes_to_html(link_splitted)
        expected_link_html = '<img src="b" alt="a"></img> <a href="d">c</a> *e* <code>f</code> <code>g</code> <img src="i" alt="h"></img> <img src="k" alt="j"></img> <code>l</code> <i>m</i> <i>n</i> *o* <code>p</code> <img src="r" alt="q"></img> <code>s</code> <img src="u" alt="t"></img> <a href="w">v</a> <img src="y" alt="x"></img> <code>z</code>'
        self.assertEqual(actual_link_html, expected_link_html)

        bold_splitted = split_nodes_delimiter(link_splitted, "*", "bold")
        self.assertEqual(len(bold_splitted), 35)
        actual_bold_html = textnodes_to_html(bold_splitted)
        expected_bold_html = '<img src="b" alt="a"></img> <a href="d">c</a> <b>e</b> <code>f</code> <code>g</code> <img src="i" alt="h"></img> <img src="k" alt="j"></img> <code>l</code> <i>m</i> <i>n</i> <b>o</b> <code>p</code> <img src="r" alt="q"></img> <code>s</code> <img src="u" alt="t"></img> <a href="w">v</a> <img src="y" alt="x"></img> <code>z</code>'
        self.assertEqual(actual_bold_html, expected_bold_html)

    def test_split_nodes_list(self):
        text = "this is text with one **bolded** word"
        text_type = "text"
        node = TextNode(text, text_type)
        node_list = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            node_list,
            [
                TextNode("this is text with one ", "text"),
                TextNode("bolded", "bold"),
                TextNode(" word", "text"),
            ],
        )

    def test_split_nodes_twice_to_list(self):
        text = "this is text with two **bolded** words; here is the **second**"
        text_type = "text"
        node = TextNode(text, text_type)
        node_list = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            node_list,
            [
                TextNode("this is text with two ", "text"),
                TextNode("bolded", "bold"),
                TextNode(" words; here is the ", "text"),
                TextNode("second", "bold"),
            ],
        )

    def test_split_italic_nodes_list(self):
        text = "str with 1 *italic* word"
        text_type = "text"
        node = TextNode(text, text_type)
        node_list = split_nodes_delimiter([node], "*", "italic")
        self.assertListEqual(
            node_list,
            [
                TextNode("str with 1 ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word", "text"),
            ],
        )

    def test_split_bold_and_italic_list(self):
        text = "**bold** and 1 *italic*"
        text_type = "text"
        node = TextNode(text, text_type)
        node_list = split_nodes_delimiter([node], "**", "bold")
        node_list = split_nodes_delimiter(node_list, "*", "italic")
        self.assertListEqual(
            node_list,
            [
                TextNode("bold", "bold"),
                TextNode(" and 1 ", "text"),
                TextNode("italic", "italic"),
            ],
        )

    def test_code_list(self):
        text = "there is a `code block` in this str"
        text_type = "text"
        node = TextNode(text, text_type)
        node_list = split_nodes_delimiter([node], "`", "code")
        self.assertListEqual(
            node_list,
            [
                TextNode("there is a ", "text"),
                TextNode("code block", "code"),
                TextNode(" in this str", "text"),
            ],
        )


if __name__ == "__main__":
    main()
