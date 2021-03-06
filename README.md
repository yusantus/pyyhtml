# Table of content:
- [Introduction](#Introduction)
- [Installation](#Installation)
- [Project Structure](#Project-Structure)
- [Components](#Components)
- [Project](#Project)

# Introduction
### Why pyyhtml
- simpler than HTML
- create Projects with automatically generated docstrings for your source files
- create dynamic Template classes once and use multiple times for better productivity
- use Python loops, functions etc. for faster development

# Installation
Install **pyyhtml** with ```pip install pyyhtml```

# Project Structure
```
/
|
|--- content/
|
|--- pages/
|
|--- templates/
|
|--- web/
|     |
|     |--- assets/
|     |
|
|--- main.py
```

- **content/**: Here you can store plain text files which you want to include in your website or some configuration JSON's.
- **pages/**: Create your Python source files here.
- **templates/**: Write your templates in this folder.
- **web/**: After creating your HTML source files, they will appear in the **web/** folder. Also store your assets in the subfolder. Later you can use the **web** folder as your ready website.

# Components
## Pyyhtml components:

**```pyyhtml.tag.tag```**:
-  Create simple HTML tag's, often used tags are stored in ```pyyhtml.components```.
- you can create a tag and place other tags as inner components with ```tag.add(other_tag)``` or just use the ```+=``` operator: ```mytag += oher_tag```

**```pyyhtml.tag.Template```**:
- Create your Template, create your own class and derive from ```pyyhtml.tag.Template```, for example a Template Navbar: 
```py
class TemplateNavbar(Template):
    def __init__(self, title: str, navbar_logo_path: str = None, links: list = None):
        navbar = tag("nav", ...)
        for link in links:
            navbar += ...
        super().__init__(tag=navbar)
```

**```pyyhtml.content.FromFile```**:
- outsource text in files and use ````pyyhtml.content.FromFile``` to place the content of text files in your HTML
- better and cleaner code with less plain text
- use the file path as parameter:
```py
FromFile("yourtext.txt")
```

# Project

Start your first project in the ```main.py```, you can add an **Author**, **E-Mail**, **GitHub Username**, **Year**, **License** and **Copyright** to your project. Pyyhtml will add a docstring with your information to all HTML source files.
```py
from pyyhtml.project import Project

# import your python page files
import pages

# add your information to th eproject
p = Project(author="John Doe")

# add the html tags of your python files and your filename
p.add(pages.index.html, "index.html")
p.add(pages.aboutus.html, "aboutus.html")

# create source files in the web folder
p.create(path="web/")
```