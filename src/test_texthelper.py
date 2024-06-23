from unittest import TestCase, main

from texthelper import extract_markdown_images, extract_markdown_links

class TestTextHelper(TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        extracted = extract_markdown_images(text)
        self.assertEqual(len(extracted), 2)
        self.assertEqual(extracted[0]['alt'], 'image')
        self.assertEqual(extracted[0]['src'], 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png')
        self.assertEqual(extracted[1]['alt'], 'another')
        self.assertEqual(extracted[1]['src'], 'https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png')
    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        extracted = extract_markdown_links(text)
        self.assertEqual(len(extracted), 2)
        self.assertEqual(extracted[0]['a_text'], 'link')
        self.assertEqual(extracted[0]['href'], 'https://www.example.com')
        self.assertEqual(extracted[1]['a_text'], 'another')
        self.assertEqual(extracted[1]['href'], 'https://www.example.com/another')
    def test_both_extracts(self):
        text = "This text has ![one image in it](https://an-image.lava-magic.com/img1.png) and it has [one link as well](https://a-doc.lava-magic.com/doc1.txt)"
        extracted_images = extract_markdown_images(text)
        self.assertEqual(len(extracted_images), 1)
        self.assertEqual(extracted_images[0]['alt'], 'one image in it')
        self.assertEqual(extracted_images[0]['src'], 'https://an-image.lava-magic.com/img1.png')
        extracted_links = extract_markdown_links(text)
        self.assertEqual(len(extracted_links), 1)
        self.assertEqual(extracted_links[0]['a_text'], 'one link as well')
        self.assertEqual(extracted_links[0]['href'], 'https://a-doc.lava-magic.com/doc1.txt')

if __name__ == '__main__':
    main()

