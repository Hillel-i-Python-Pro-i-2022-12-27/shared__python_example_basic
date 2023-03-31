# Also you can build string by "concatenation".

my_string = "This is " + "text" + "," + "what built by concatenation."

print(my_string)

# More complex example:
name = "Aleksandr"
text = "Some text"

another_string = f'Hello, {name}. {text + "!"}' + " " + "Concatenated text"

print(another_string)
