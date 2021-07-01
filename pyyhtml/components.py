from .interface import tag


class FromFile:
    def __init__(self, filepath: str):
        with open(filepath, "r") as readfile:
            self.lines = readfile.read()
            print(self.lines)
    def __str__(self):
        return str(self.lines)




class head(tag):
    def __init__(self, content = None, *args, **kwargs):
        super().__init__("head", content, *args, **kwargs)

class body(tag):
    def __init__(self, content = None, *args, **kwargs):
        super().__init__("body", content, *args, **kwargs)
    





