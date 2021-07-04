from .interfaces import FromFile

class tag:
    def __init__(self, tagname: str, components = None, dont_close: bool = False, *args, **kwargs):
        if not tagname:
            raise Exception("tagname can't be empty.")
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
        else:
            raise Exception("Only can add tags.")
            
        return self

    def get_tag(self):
        options = ""
        for key, value in self.kwargs.items():
            if key == "klass":
                key = "class"
            options += ' %s="%s"' % (key, value)
        tag = f"<{self.tagname}" + options + ">"
        return tag

    def get_html_list(self):
        html_list = [self.get_tag()]
        for component in self.components:
            if type(component) is tag or isinstance(component, tag):
                html_list.extend(component.get_html_list())
            elif isinstance(component, FromFile):
                html_list.extend(component.get_content_list())
            else:
                html_list.append(component)
        if not self.dont_close:
            html_list.append(f"</{self.tagname}>")
        return html_list