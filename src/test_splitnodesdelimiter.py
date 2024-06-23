from unittest import TestCase, main

from splitnodesdelimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode

class TestSplitNodesDelimiter(TestCase):
    def test_split_nodes_delimiter(self):
        original_text = '**Hi!** It\'s a *very* good, **valid** and *well-thought-out* Markdown! (a `code` language, used for `formatting`.) Let\'s **see**!'
        original_node = TextNode(original_text, 'text')
        italic_splitted = split_nodes_delimiter([original_node], '**', 'italic')
        self.assertEqual(len(italic_splitted), 7)
        self.assertEqual(''.join(x.to_html_node().to_html() for x in italic_splitted), '<i>Hi!</i> It\'s a *very* good, <i>valid</i> and *well-thought-out* Markdown! (a `code` language, used for `formatting`.) Let\'s <i>see</i>!')

        bold_splitted = split_nodes_delimiter(italic_splitted, '*', 'bold')
        self.assertEqual(len(bold_splitted), 11)
        actual_bold_html = ''.join(x.to_html_node().to_html() for x in bold_splitted)
        expected_bold_html = '<i>Hi!</i> It\'s a <b>very</b> good, <i>valid</i> and <b>well-thought-out</b> Markdown! (a `code` language, used for `formatting`.) Let\'s <i>see</i>!'
        self.assertEqual(actual_bold_html, expected_bold_html)
        
        code_splitted = split_nodes_delimiter(bold_splitted, '`', 'code')
        self.assertEqual(len(code_splitted), 15)
        actual_code_html = ''.join(x.to_html_node().to_html() for x in code_splitted)
        expected_code_html = '<i>Hi!</i> It\'s a <b>very</b> good, <i>valid</i> and <b>well-thought-out</b> Markdown! (a <code>code</code> language, used for <code>formatting</code>.) Let\'s <i>see</i>!'
        self.assertEqual(actual_code_html, expected_code_html)
    def test_split_nodes_image(self):
        original_text = '*a* ![b](c) *c*'
        original_node = TextNode(original_text, 'text')
        image_splitted = split_nodes_image([original_node])
        self.assertEqual(len(image_splitted), 3)
        self.assertEqual(''.join(x.to_html_node().to_html() for x in image_splitted), '*a* <img src="c" alt="b"></img> *c*')
    def test_split_nodes(self):
        original_text = '![a](b) [c](d) *e* `f` `g` ![h](i) ![j](k) `l` **m** **n** *o* `p` ![q](r) `s` ![t](u) [v](w) ![x](y) `z`'
        original_node = TextNode(original_text, 'text')
        image_splitted = split_nodes_image([original_node])
        self.assertEqual(len(image_splitted), 13)
        actual_image_html = ''.join(x.to_html_node().to_html() for x in image_splitted)
        expected_image_html = '<img src="b" alt="a"></img> [c](d) *e* `f` `g` <img src="i" alt="h"></img> <img src="k" alt="j"></img> `l` **m** **n** *o* `p` <img src="r" alt="q"></img> `s` <img src="u" alt="t"></img> [v](w) <img src="y" alt="x"></img> `z`'
        self.maxDiff = None
        self.assertEqual(actual_image_html, expected_image_html)

        italic_splitted = split_nodes_delimiter(image_splitted, '**', 'italic')
        self.assertEqual(len(italic_splitted), 17)
        actual_italic_html = ''.join(x.to_html_node().to_html() for x in italic_splitted)
        expected_italic_html = '<img src="b" alt="a"></img> [c](d) *e* `f` `g` <img src="i" alt="h"></img> <img src="k" alt="j"></img> `l` <i>m</i> <i>n</i> *o* `p` <img src="r" alt="q"></img> `s` <img src="u" alt="t"></img> [v](w) <img src="y" alt="x"></img> `z`'
        self.assertEqual(actual_italic_html, expected_italic_html)

        code_splitted = split_nodes_delimiter(italic_splitted, '`', 'code')
        self.assertEqual(len(code_splitted), 29)
        actual_code_html = ''.join(x.to_html_node().to_html() for x in code_splitted)
        expected_code_html = '<img src="b" alt="a"></img> [c](d) *e* <code>f</code> <code>g</code> <img src="i" alt="h"></img> <img src="k" alt="j"></img> <code>l</code> <i>m</i> <i>n</i> *o* <code>p</code> <img src="r" alt="q"></img> <code>s</code> <img src="u" alt="t"></img> [v](w) <img src="y" alt="x"></img> <code>z</code>'
        self.assertEqual(actual_code_html, expected_code_html)

        link_splitted = split_nodes_link(code_splitted)
        self.assertEqual(len(link_splitted), 33)
        actual_link_html = ''.join(x.to_html_node().to_html() for x in link_splitted)
        expected_link_html = '<img src="b" alt="a"></img> <a href="d">c</a> *e* <code>f</code> <code>g</code> <img src="i" alt="h"></img> <img src="k" alt="j"></img> <code>l</code> <i>m</i> <i>n</i> *o* <code>p</code> <img src="r" alt="q"></img> <code>s</code> <img src="u" alt="t"></img> <a href="w">v</a> <img src="y" alt="x"></img> <code>z</code>'
        self.assertEqual(actual_link_html, expected_link_html)

        bold_splitted = split_nodes_delimiter(link_splitted, '*', 'bold')
        self.assertEqual(len(bold_splitted), 37)
        actual_bold_html = ''.join(x.to_html_node().to_html() for x in bold_splitted)
        expected_bold_html = '<img src="b" alt="a"></img> <a href="d">c</a> <b>e</b> <code>f</code> <code>g</code> <img src="i" alt="h"></img> <img src="k" alt="j"></img> <code>l</code> <i>m</i> <i>n</i> <b>o</b> <code>p</code> <img src="r" alt="q"></img> <code>s</code> <img src="u" alt="t"></img> <a href="w">v</a> <img src="y" alt="x"></img> <code>z</code>'
        self.assertEqual(actual_bold_html, expected_bold_html)


        
if __name__ == '__main__':
    main()

