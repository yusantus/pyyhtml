from .interfaces import FromFile


class FromTXT(FromFile):
    def __init__(self, filepath, new_lines = False):
        super().__init__(filepath)
        with open(self.filepath, "r") as readfile:
            self.lines = readfile.readlines()
            if new_lines:
                for i in range(len(self.lines)):
                    self.lines[i] = self.lines[i].replace("\n", "<br>")
            else:
                self.lines.remove("\n")
    def get_content_list(self):
        return self.lines