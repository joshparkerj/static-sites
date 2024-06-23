from re import sub
from os.path import dirname, join, isfile
from os import makedirs, listdir

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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for e in listdir(dir_path_content):
        src_path = join(dir_path_content, e)
        dst_path = join(dest_dir_path, e)
        if isfile(src_path) and src_path.endswith('.md'):
            generate_page(src_path, template_path, sub(r'(?m)\.md$', '.html', dst_path))
        else:
            generate_pages_recursive(src_path, template_path, dst_path)

