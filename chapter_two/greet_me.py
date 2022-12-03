# create a func that prints out a greeting to any names
# passed to the func
def greet_me(a_name):
    print("Hello "+a_name)

# create var named author
author = "Susan E. McGregor"

# create var named editor
editor = "Jeff Bleiel"

# use custom func greet_me to output hello msg to each person
greet_me(author)
greet_me(editor)

# messing with the syntax of the custom func greet_me
greet_me()
greet_me(author,editor)
greet_me("Sam")
greet_me(1328)
