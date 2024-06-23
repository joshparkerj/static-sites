from re import sub
from os.path import dirname
from os import makedirs

from markdownhelper import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path) as f:
        file_content_string = f.read()
    with open(template_path) as f:
        template_content_string = f.read()
    node = markdown_to_html_node(file_content_string)
    html_string = node.to_html()
    title = extract_title(file_content_string)
    titled_template = sub(r'{{ Title }}', title, template_content_string)
    titled_template_with_content = sub(r'{{ Content }}', html_string, titled_template)
    makedirs(dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(titled_template_with_content)

