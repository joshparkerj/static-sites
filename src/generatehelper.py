from re import sub
from os.path import dirname, join, isfile, isdir
from os import makedirs, listdir

from markdownhelper import markdown_to_html_node, extract_title


def generate_nav(dir_path):
    nav_links = []
    for dir in listdir(dir_path):
        if isdir(join(dir_path, dir)):
            index_path = join(dir_path, dir, "index.md")
            if isfile(index_path):
                with open(index_path) as f:
                    index_string = f.read()
                nav_item = (extract_title(index_string), f"./{dir}")
                nav_link = f'<li><a href="{nav_item[1]}">{nav_item[0]}</a></li>'
                nav_links.append(nav_link)
    return f'<ul class="nav"><li><a href="/">HOME</a></li>{"".join(nav_links)}</ul>'


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        file_content_string = f.read()
    with open(template_path) as f:
        template_content_string = f.read()
    node = markdown_to_html_node(file_content_string)
    html_string = node.to_html()
    title = extract_title(file_content_string)
    template_with_nav = sub(
        r"{{ Nav }}", generate_nav(dirname(from_path)), template_content_string
    )
    titled_template = sub(r"{{ Title }}", title, template_with_nav)
    titled_template_with_content = sub(r"{{ Content }}", html_string, titled_template)
    makedirs(dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(titled_template_with_content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for e in listdir(dir_path_content):
        src_path = join(dir_path_content, e)
        dst_path = join(dest_dir_path, e)
        if isfile(src_path) and src_path.endswith(".md"):
            generate_page(src_path, template_path, sub(r"(?m)\.md$", ".html", dst_path))
        else:
            generate_pages_recursive(src_path, template_path, dst_path)
