from textnode import TextNode
from directoryhelper import make_copy

def main():
 text_node = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
 print(text_node)
 make_copy('static', 'public')

main()
