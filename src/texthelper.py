from re import finditer

def extract_markdown_images(text):
    alt_re = r'!\[(?P<alt>[^\]]*)\]'
    src_re = r'\((?P<src>[^\)]*)\)'
    images = [{ 'alt': m.group('alt'), 'src': m.group('src'), 'md': m.group(0) } for m in finditer(alt_re + src_re, text)]
    return images

def extract_markdown_links(text):
    link_re = r'(?m)(^|[^!])(\[(?P<a_text>[^\]]*)\]\((?P<href>[^\)]*)\))'
    links = [{ 'a_text': m.group('a_text'), 'href': m.group('href'), 'md': m.group(2) } for m in finditer(link_re, text)]
    return links

