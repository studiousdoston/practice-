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

print("===== Set =====")
# ? set of unique collection without keeping order!
new_numbers = array('i', [1, 4, 7, 4, 9, 5, 4,  42, 7, 5])
nums_set = set(new_numbers)

print('numbers set', nums_set, type(nums_set))

nums_set.add(200)
print('nums_set(1):', nums_set)

nums_set.add(5)
print('nums_set(2):', nums_set)

print('==== Specific operators with set ====')
# ?  (|)->uninion, (&)->intersaction, (-)->difference, (^)->Symmetric difference

a = { 10,20, 50}
b = {20,40}

result1 = a|b
result2 = a&b
result3 = a-b
result4 = a^b

print('result1:', result1)
print('result2:', result2)
print('result3:', result3)
print('result4:', result4)
