# splitting a string "literal" and then printing the result
split_world = "Hello World!".split()
print(split_world)

# assign a string to a var then print the result after calling 'split()' method
world_msg = "Hello World!"
print(world_msg.split())

# the following will throw an error bc the 'split()' method can only
# be called on a string
split("Hello World!")

# the following will throw an error bc the 'split()' method is not
# available for numbers
print(5.split())
