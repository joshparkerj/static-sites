from textnode import TextNode
from directoryhelper import make_copy
from generatehelper import generate_page

def main():
 text_node = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
 print(text_node)
 make_copy('static', 'public')
 generate_page('content/index.md', 'template.html', 'public/index.html')


main()
