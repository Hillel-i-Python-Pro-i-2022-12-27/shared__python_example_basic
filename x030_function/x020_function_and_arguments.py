# Function can accept some arguments.
# ->
def greeting_function(name: str, color: str = "Blue") -> str:
    return f"Hello, {name}. Your color is {color}."


# You can send arguments by "position".
print(greeting_function("Aleksandr", "Yellow"))

# If the sequence is wrong, there will be a bad result.
print(
    greeting_function(
        "Red",
        "Aleksandr",
    )
)

# Or you can send arguments by "keys".
print(greeting_function(name="Aleksandr", color="Green"))
print(greeting_function(color="Orange", name="Aleksandr"))

# Also, you can use "default values".
print(greeting_function(name="Aleksandr"))

print(greeting_function(name="Aleksandr"))
