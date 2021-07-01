from abc import ABC, abstractmethod

class tag(ABC):
    def __init__(self, tagname: str, content = None, dont_close: bool = False, *args, **kwargs):
        self.tagname = tagname
        self.content = content
        self.options = dict()
        if kwargs:
            for key, value in kwargs.items():
                self.options[key] = value
        self.dont_close = dont_close

    def to_list(self):
        object_list = list()
        tag = f"<{self.tagname}"
        if self.options:
            for option_key, option_val in self.options.items():
                if option_key=="klass":
                    option_key="class"
                if type(option_val) is not list:
                    tag += f' {option_key}="{option_val}"'
                if type(option_val) is list:
                    flag = False
                    tag += f' {option_key}="'
                    for option in option_val:
                        if flag:
                            tag += " "
                        tag += option
                        flag = True
                    tag += '"'
        tag += ">"
        object_list.append(tag)
        if self.content and not self.dont_close:
            if type(self.content) is list:
                object_list.extend(self.content)
            elif type(self.content) is str:
                object_list.append(self.content)
            elif type(self.content) is float or int:
                object_list.append(str(self.content))
        if self.content and self.dont_close:
            raise Exception("Cant not close tag if content")
        if not self.dont_close:
            object_list.append(f"</{self.tagname}>")
        return object_list
    
    def __iter__(self):
        return iter(self.to_list())
    
    def __str__(self):
        return str(self.to_list())