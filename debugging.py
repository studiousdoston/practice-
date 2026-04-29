''' Packages & Debugging
    1. Python Packages & Core Package
    2. Package Manager & External Package
    3. Debugging
'''
import turtle
print("===== Python Packages & Core Package ======")
''' Python Package/Modules: Core🐍, File📒 and External➡️ '''


# # Core Package
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(1)
# t.circle(100)

# turtle.done()

print("----------")
my_file = open("materials/message.txt", "r")
try:
  context = my_file.read()
  print("content:", context)
finally:
  my_file.close()

# with - Context Manager
with open("materials/message.txt", "r") as your_file:
  your_content  = your_file.read()
  print("your_content:", your_content)

print("DONE")
