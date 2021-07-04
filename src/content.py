from .interfaces import FromFile


class FromTXT(FromFile):
    def __init__(self, filepath):
        super().__init__(filepath)
        with open(self.filepath, "r") as readfile:
            self.lines = readfile.readlines()
            for i in range(len(self.lines)):
                self.lines[i] = self.lines[i].replace("\n", "<br>")
    def get_content_list(self):
        return self.lines