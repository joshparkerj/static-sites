from directoryhelper import make_copy
from generatehelper import generate_pages_recursive


def main():
    make_copy('static', 'public')
    generate_pages_recursive('content', 'template.html', 'public')


main()
