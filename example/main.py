from pyyhtml import *

myhtml = html(lang="en")

myhead = head()

myhead.add(title("Title of your website"))


mybody = body()

mybody += [p("I'm a paragraph"), br(), a("I'm a link")]

mybody += div(FromTXT("text.txt"), klass="container")




mybody += tag("span", "I'm a custom span.")

myhtml += [myhead, mybody]

write_list_to_file("index.html", myhtml.get_html_list())