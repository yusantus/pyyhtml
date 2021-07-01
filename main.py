from pyyhtml import *

htmlfile = HTML(head(), body(FromFile("text.txt"), background_color="#cccccc", klass="container div"),  lang="de")
htmlfile.export("index.html")
