from pyyhtml.content import FromFile
from pyyhtml.comment import comment

class tag:
    def __init__(self, tagname: str, components = None, dont_close: bool = False, *args, **kwargs):
        if not tagname:
            raise Exception("tagname can't be empty!")
        self.tagname = tagname

        if dont_close and components:
            raise Exception("Only elements with closed brackets can hold components")
        self.components = list()
        if components:
            if type(components) is list:
                self.components.extend(components)
            else:
                self.components.append(components)
        self.dont_close = dont_close
        self.kwargs = kwargs
    
    def add(self, component):
        if type(component) is list:
            self.components.extend(component)
        else:
            self.components.append(component)
    
    def __iadd__(self, other):
        if type(other) is tag or isinstance(other, tag):
            self.add(other)
        elif type(other) is list:
            for component in other:
                if type(component) is tag or isinstance(component, tag):
                    self.add(component)
                else:
                    raise Exception("Only can add tags.")
        elif isinstance(other, Template):
            self.add(other.get_tag())
            
        elif isinstance(other, comment):
            self.add(other.get_text())
        else:
            raise Exception("Only can add tags.")
            
        return self

    def get_tag(self):
        options = ""
        for key, value in self.kwargs.items():
            if key == "klass":
                key = "class"
            key = key.replace("_", "-")
            options += ' %s="%s"' % (key, value)
        tag = f"<{self.tagname}" + options + ">"
        return tag

    def get_html_list(self):
        html_list = [self.get_tag()]
        for component in self.components:
            if type(component) is tag or isinstance(component, tag):
                html_list.extend(component.get_html_list())
            elif type(component) is FromFile:
                html_list.extend(component.get_content_list())
            else:
                html_list.append(component)
        if not self.dont_close:
            html_list.append(f"</{self.tagname}>")
        return html_list


class Template(tag):
    def __init__(self, tag):
        super().__init__(tagname=tag.tagname, components=tag.components, dont_close = tag.dont_close, *{}, **tag.kwargs)