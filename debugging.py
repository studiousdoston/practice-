''' Packages & Debugging
    1. Python Packages & Core Package
    2. Package Manager & External Package
    3. Debugging
'''
from PIL import Image
import turtle
print("===== Python Packages & Core Package ======")
''' Python Package/Modules: Core🐍, File📒 and External➡️ '''


# Core Package
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)
t.circle(100)

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
    your_content = your_file.read()
    print("your_content:", your_content)

print("DONE")


print("===== Package Managers & External Package ======")

'''Package Managers
   Python > pip pipenv
   NodeJs > npm yarn
   PHP    > composer
   MacOS  > brew
'''
# External Package > pypi.org

with Image.open("materials/pillow.jpg") as img_obj:
    resized_img = img_obj.resize((200, 300))
    resized_img.show()
    resized_img.save("materials/sample.jpg")


print("===== Debugging =====")


def get_summary(*args):
    total_amount = 0
    for a in args:
        total_amount += a
        return total_amount # find the bug

test = 100
result = get_summary(1,2,4,56,3,2,45)
print("result:", result)