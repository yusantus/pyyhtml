from .components import body, head
from .interface import tag
from .fileio import list_to_file

class HTML:
    def __init__(self, head: head = head(), body: body = body(), *args, **kwargs):
        self.object_list = list()
        self.object_list.extend(head)
        self.object_list.extend(body)

        self.content = list()
        self.content.append("<!doctype html>")
        self.content.extend(tag("html", self.object_list, *args, **kwargs))
    
    def to_list(self):
        return self.content

    def export(self, filename: str):
        with open(filename, "w", encoding="UTF-8") as writefile:
            for line in self.content:
                print(line)
                line = line + "\n"
                writefile.write(line)