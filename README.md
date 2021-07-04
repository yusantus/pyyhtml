# Table of content:
- [Introduction](#Introduction)
- [Installation](#Installation)
- [How-to](#How-to)

# Introduction
Easily create HTML Files with Python. The usage is more simple and efficient as the usual HTML. 

# Installation
Install **pyyhtml** with ````pip install pyyhtml```

# How-to
Import all from **pyyhtml** package and start creating your first HTML File with **pyyhtml**.
You can add options to HTML elements via keyword arguments in Python.
```py
from pyyhtml import *
myhtml = html(lang="en") # options via keyword arguments
```

Every object has a list, containing objects. You can add objects to an object via:
```py
myhead = head()
myhead.add(title("Title of your website")) # add objects
```

You can also use the ```+=``` operator to add objects, also you can add multiple objects in a list:
```py
mybody = body()
mybody += [p("I'm a paragraph"), br(), a("I'm a link")]
```

If you want nice and clean code, keep long texts in text files and import them via ```FromTXT```:
```py
mybody += div(FromTXT("text.txt"), klass="container")
```

Not every HTML element is supported, if you want cutsom tags, use the ```tag``` object:
```py
mybody += tag("span", "I'm a custom span.")
```

Finally add the head and body to you HTML and create your first HTML file with:
```py
myhtml += [myhead, mybody]
write_list_to_file("index.html", myhtml.get_html_list())
```

The ```get_html_list()``` function returns a list with all objects and it's child objects.