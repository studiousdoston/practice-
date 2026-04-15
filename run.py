# Dunder (double underscores) __builtins__, __init__

message = "PYTHON: Everything is object!"
print(message)

result = type(message)
print("result:", result)

'''we can have multiple lines of comments with tripe single strings

  Built-in tools in Python
  1. TYPES => int, float, str, list, dict
  2. FUNCTIONS => print() len() input() type()
  3. CONSTANTS => True, False, None
'''
print(dir(__builtins__))