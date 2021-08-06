from .tag import tag

## closed brackets

class html(tag):
    def __init__(self, components = None, *args, **kwargs):
        super().__init__("html", components, *args, **kwargs)

class head(tag):
    def __init__(self, components = None, *args, **kwargs):
        super().__init__("head", components, *args, **kwargs)

class body(tag):
    def __init__(self, components = None, *args, **kwargs):
        super().__init__("body", components, *args, **kwargs)

class div(tag):
    def __init__(self, components = None, *args, **kwargs):
        super().__init__("div", components, *args, **kwargs)
    
class p(tag):
    def __init__(self, components = None, *args, **kwargs):
        super().__init__("p", components, *args, **kwargs)
    
class a(tag):
    def __init__(self, components = None, *args, **kwargs):
        super().__init__("a", components, *args, **kwargs)
    
class script(tag):
    def __init__(self, components = None, *args, **kwargs):
        super().__init__("script", components, *args, **kwargs)

class title(tag):
    def __init__(self, components = None, *args, **kwargs):
        super().__init__("title", components, *args, **kwargs)

class style(tag):
    def __init__(self, components = None, *args, **kwargs):
        super().__init__("style", components, *args, **kwargs)

class button(tag):
    def __init__(self, components = None, *args, **kwargs):
        super().__init__("button", components, *args, **kwargs)

class span(tag):
    def __init__(self, components = None, *args, **kwargs):
        super().__init__("span", components, *args, **kwargs)

class ul(tag):
    def __init__(self, components = None, *args, **kwargs):
        super().__init__("ul", components, *args, **kwargs)

class li(tag):
    def __init__(self, components = None, *args, **kwargs):
        super().__init__("li", components, *args, **kwargs)



## open brackets

class br(tag):
    def __init__(self, *args, **kwargs):
        super().__init__("br", dont_close=True, *args, **kwargs)

class meta(tag):
    def __init__(self, *args, **kwargs):
        super().__init__("meta", dont_close=True, *args, **kwargs)
    
class link(tag):
    def __init__(self, *args, **kwargs):
        super().__init__("link", dont_close=True, *args, **kwargs)
        