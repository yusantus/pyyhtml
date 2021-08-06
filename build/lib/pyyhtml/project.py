from .fileio import html_to_file
from .components import html
from .comment import comment

class Project:
    def __init__(self, author: str = None, email: str = None, github: str = None, year: int = None, license: str = None, copyright: str = None):
        self.author = author
        self.email = email
        self.github = github
        self.year = year
        self.license = license
        self.copyright = copyright
        self.files = list()
        
    def get_docstring(self):
        docstring = list()
        docstring.append(comment(5*"*" + " docstring of pyyhtml " + 5*"*"))
        docstring.append(comment("pyyhtml: https://pypi.org/project/pyyhtml/"))
        if self.author:
            docstring.append(comment(f"Author: {self.author}"))
        if self.email:
            docstring.append(comment(f"E-Mail: {self.email}"))
        if self.github:
            docstring.append(comment(f"GitHub: {self.github}"))
        if self.year:
            docstring.append(comment(f"Year: {self.year}"))
        if self.license:
            docstring.append(comment("License:"))
            docstring.append(comment(self.license))
        if self.copyright:
            docstring.append(comment("Copyright:"))
            docstring.append(comment(self.copyright))
        docstring.append(comment(60*"*"))
        return docstring
        
    
    def add(self, html: html, filename: str):
        self.files.append({"filename": filename, "html": html})
        
    def create(self, path: str = None):
        for htmlfile in self.files:
            if path:
                full_path = path + htmlfile["filename"]
            else:
                full_path = htmlfile["filename"]
            html_to_file(full_path, htmlfile["html"], self.get_docstring())
        

            
            