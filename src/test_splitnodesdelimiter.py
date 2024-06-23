from unittest import TestCase, main

from splitnodesdelimiter import split_nodes_delimiter
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
if __name__ == '__main__':
    main()

