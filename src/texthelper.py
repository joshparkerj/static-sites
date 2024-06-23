from re import finditer

def extract_markdown_images(text):
    alt_re = r'!\[(?P<alt>[^\]]*)\]'
    src_re = r'\((?P<src>[^\)]*)\)'
    images = [{ 'alt': m.group('alt'), 'src': m.group('src') } for m in finditer(alt_re + src_re, text)]
    return images

def extract_markdown_links(text):
    a_text_re = r'[^!]\[(?P<a_text>[^\]]*)\]'
    href_re = r'\((?P<href>[^\)]*)\)'
    links = [{ 'a_text': m.group('a_text'), 'href': m.group('href') } for m in finditer(a_text_re + href_re, text)]
    return links

