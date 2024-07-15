from unittest import TestCase, main

from markdownhelper import markdown_to_html_node, extract_title


markdown = """
        # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

1. correct ordered list
2. correct ordered list
3. correct ordered list
4. correct ordered list
5. correct ordered list
6. correct ordered list
7. correct ordered list
8. correct ordered list
9. correct ordered list

1. invalid ordered list (according to strict rules described at https://www.boot.dev/lessons/719ee1ae-19b6-4572-9b40-c8530dcbfa4f
1. (this is usually allowed i think)
1. but not this time!
1. (we can always go back and change it later I suppose)

     ## leading spaces should be ignored

####### too many hashes will get this interpreted as a paragraph, not heading

* This is a list item
* This is another list item                     

This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items

- list using dashes
- (should be treated the same as stars)
- and they can be mixed:

    - mixed dashes and stars in this list
    * we can alternate
    - or whatever
    * more list
    - more list
    * more list
    - more list
    * more list
    - more list
    * more list
    - more list
    * more list
    - more list
    * more list
    - more list


```
 this is code
 this is code
 this is code
 this is code
 this is code
 this is code
 this is code
```

a - 
s
i
n
g
l
e - 
p
a
r
a
g
r
a
p
h
        """
expected_html = (
    "<div><h1>This is a heading</h1>"
    + "<p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p>"
    + "<ol><li>correct ordered list</li><li>correct ordered list</li><li>correct ordered list</li><li>correct ordered list</li><li>correct ordered list</li><li>correct ordered list</li><li>correct ordered list</li><li>correct ordered list</li><li>correct ordered list</li></ol>"
    + "<p>1. invalid ordered list (according to strict rules described at https://www.boot.dev/lessons/719ee1ae-19b6-4572-9b40-c8530dcbfa4f 1. (this is usually allowed i think) 1. but not this time! 1. (we can always go back and change it later I suppose)</p>"
    + "<h2>leading spaces should be ignored</h2>"
    + "<p>####### too many hashes will get this interpreted as a paragraph, not heading</p>"
    + "<ul><li>This is a list item</li><li>This is another list item</li></ul>"
    + "<p>This is <b>bolded</b> paragraph</p>"
    + "<p>This is another paragraph with <i>italic</i> text and <code>code</code> here This is the same paragraph on a new line</p>"
    + "<ul><li>This is a list</li><li>with items</li></ul>"
    + "<ul><li>list using dashes</li><li>(should be treated the same as stars)</li><li>and they can be mixed:</li></ul>"
    + "<ul><li>mixed dashes and stars in this list</li><li>we can alternate</li><li>or whatever</li><li>more list</li><li>more list</li><li>more list</li><li>more list</li><li>more list</li><li>more list</li><li>more list</li><li>more list</li><li>more list</li><li>more list</li><li>more list</li><li>more list</li></ul>"
    + "<pre><code>this is code\nthis is code\nthis is code\nthis is code\nthis is code\nthis is code\nthis is code</code></pre>"
    + "<p>a - s i n g l e - p a r a g r a p h</p></div>"
)


class TestMarkdownHelper(TestCase):
    def test_markdown_to_html_node(self):
        node = markdown_to_html_node(markdown)
        self.maxDiff = None
        actual_html = node.to_html()
        self.assertEqual(actual_html, expected_html)

    def test_paragraph_link(self):
        node = markdown_to_html_node("[Back Home](/)")
        self.assertEqual(node.to_html(), '<div><p><a href="/">Back Home</a></p></div>')

    def test_extract_title(self):
        self.assertEqual(extract_title(markdown), "This is a heading")

    def test_no_title(self):
        self.assertRaises(Exception, extract_title, "")

    def test_headings(self):
        headings = "\n# First Heading\n\n## Sub Heading\n"
        node = markdown_to_html_node(headings)
        self.assertEqual(
            node.to_html(), "<div><h1>First Heading</h1><h2>Sub Heading</h2></div>"
        )

    def test_more_headings(self):
        headings = "# First Heading\n## Sub Heading"
        node = markdown_to_html_node(headings)
        self.assertEqual(
            node.to_html(), "<div><h1>First Heading</h1><h2>Sub Heading</h2></div>"
        )

    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_eq_double(self):
        actual = extract_title(
            """
# This is a title

# This is a second title that should be ignored
"""
        )
        self.assertEqual(actual, "This is a title")

    def test_eq_long(self):
        actual = extract_title(
            """
# title

this is a bunch

of text

* and
* a
* list
"""
        )
        self.assertEqual(actual, "title")

    def test_none(self):
        try:
            extract_title(
                """
no title
"""
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass


if __name__ == "__main__":
    main()
