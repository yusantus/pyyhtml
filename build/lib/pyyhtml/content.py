class FromFile:
    def __init__(self, filepath, new_lines = False):
        self.filepath = filepath
        with open(self.filepath, "r") as readfile:
            self.lines = readfile.readlines()
            if new_lines:
                for i in range(len(self.lines)):
                    self.lines[i] = self.lines[i].replace("\n", "<br>")
            else:
                for i in range(len(self.lines)):
                    self.lines[i] = self.lines[i].replace("\n", "")
    def get_content_list(self):
        return self.lines