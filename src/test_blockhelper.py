from unittest import TestCase, main

from blockhelper import block_to_block_type, paragraph_block_to_node
from convert import markdown_to_blocks

markdown = '''
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

####### too many hashes will get this interpreted as paragraph, not heading

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
        '''
class TestBlockHelper(TestCase):
    def test_block_to_block_type(self):
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 14)
        expected_types = ['heading', 'paragraph', 'ordered_list', 'paragraph', 'heading', 'paragraph', 'unordered_list', 'paragraph', 'paragraph', 'unordered_list', 'unordered_list', 'unordered_list', 'code', 'paragraph']
        actual_types = [block_to_block_type(block) for block in blocks]
        types = zip(expected_types, actual_types)
        all_types_are_equal = all(expected_type == actual_type for expected_type, actual_type in types)
        self.assertTrue(all_types_are_equal)
    def test_paragraph_block_to_node(self):
        paragraph_block = '[Back Home](/)'
        self.assertEqual(paragraph_block_to_node(paragraph_block).to_html(), '<p><a href="/">Back Home</a></p>')

if __name__ == '__main__':
    main()

