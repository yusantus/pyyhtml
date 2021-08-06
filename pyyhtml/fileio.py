from .components import html

def html_to_file(filepath: str, html: html, docstring: list = None):
    with open(filepath, "w", encoding="UTF-8") as writefile:
        writefile.write("<!doctype html>\n")
        if docstring:
            for comment in docstring:
                writefile.write(comment.get_text() + "\n")
        for line in html.get_html_list():
            writefile.write(line + "\n")