from unittest import TestCase, main

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(TestCase):
    def test_one_text_child(self):
        child_node = LeafNode('hello')
        parent_node = ParentNode([child_node], 'div')
        self.assertEqual(parent_node.to_html(), '<div>hello</div>')
    def test_one_p_child(self):
        child_node = LeafNode('hello', 'p')
        parent_node = ParentNode([child_node], 'section')
        self.assertEqual(parent_node.to_html(), '<section><p>hello</p></section>')
    def test_four_leaf_children(self):
        node = ParentNode([
            LeafNode('Bold Text', 'b'),
            LeafNode('Normal Text'),
            LeafNode('Italic Text', 'i'),
            LeafNode('More Normal Text')
        ],
        'p')
        self.assertEqual(node.to_html(), '<p><b>Bold Text</b>Normal Text<i>Italic Text</i>More Normal Text</p>')
    def test_nested_parents(self):
        node = ParentNode([
            ParentNode([
                ParentNode([
                    ParentNode([
                        LeafNode('hi')
                        ], 'div'),
                    ], 'div'),
                ], 'div'),
            ], 'div')
        self.assertEqual(node.to_html(), '<div><div><div><div>hi</div></div></div></div>')
    def test_nested_parents_props(self):
        node = ParentNode([
            ParentNode([
                ParentNode([
                    LeafNode('a', 'a', {'href': 'https://en.wikipedia.org/'}),
                    LeafNode('b', 'b')
                ], 'div', {'class': 'incantation', 'id': 'wizard-spell'}),
            ], 'div', {'class': 'indented', 'style': 'margin: 0'}),
            ParentNode([
                LeafNode('c', 'c'),
                LeafNode('d', 'd'),
                LeafNode('e', 'e')
                ], 'div', {'class': 'water'}),
            ], 'div', {'class': 'info'})
        self.assertEqual(node.to_html(), '<div class="info"><div class="indented" style="margin: 0"><div class="incantation" id="wizard-spell"><a href="https://en.wikipedia.org/">a</a><b>b</b></div></div><div class="water"><c>c</c><d>d</d><e>e</e></div></div>')

    def test_empty_tag(self):
        node = ParentNode([LeafNode('sup')], '')
        self.assertRaises(Exception, node.to_html)
    def test_bad_children(self):
        node = ParentNode(['hi'], 'div')
        self.assertRaises(Exception, node.to_html)
    def test_leaf_parent_mixed(self):
        node = ParentNode([
            ParentNode([
                ParentNode([
                    LeafNode('elephant', 'span'),
                    LeafNode('finch', 'span')
                ], 'div'),
                LeafNode('duck', 'span')
            ], 'div'),
            LeafNode('alligator', 'span'),
            ParentNode([
                LeafNode('crocodile', 'span')
            ], 'div'),
            LeafNode('buffalo', 'span')
        ], 'div', {'class': 'highlight finished declaration'})
        self.assertEqual(node.to_html(), '<div class="highlight finished declaration"><div><div><span>elephant</span><span>finch</span></div><span>duck</span></div><span>alligator</span><div><span>crocodile</span></div><span>buffalo</span></div>')

if __name__ == '__main__':
    main()

