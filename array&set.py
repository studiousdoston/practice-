'''Array & Set
    1. Array
    2. Set
    3. Specific operators with set
'''

from array import array
print("===== Array =====")
numbers = array('i', [1, 4, 7, 9, 5, 42])
print('numbers before:', numbers)
numbers.append(100)
numbers.insert(0, 13)
print('numbers:', numbers)


numbers.remove(5)
numbers.pop()
print('numbers after remove and pop:', numbers)

del numbers[0:2]
print('numbers after del [0:2]:', numbers)
