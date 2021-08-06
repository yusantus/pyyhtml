class comment:
    
    def __init__(self, text):
        self.text = text
    def get_text(self):
        return f"<!-- {self.text} -->"