'''I-TASK (PYTHON)

Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
MASALAN: get_digits("m14i1t") return qiladi "141"
'''
# ⭐️ Masalaning yechimi
def get_digits(string):
  empty_list = []
  for num in string:
    if num.isdigit():
      empty_list.append(num)
  
  return "".join(empty_list)

print(get_digits("m14i1t46j9"))




'''STEPS
  1.receive string
  2. create empty list
  2.convert that string into list
  3. check individual element of the new list for numbers
  4. append those numbers into the empty list
  5. turn that list into string and return it
  '''
''' G-TASK(PYTHON)
Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: get_highest_index([5,  12, 21, 8]) return qiladi 1 sonini.
'''
'''Masalaning yechimi


#  ⭐️ Masalaning yechimi
def get_highest_index(num_list):
    max_num = max(num_list)
    return num_list.index(max_num)

print(get_highest_index([5, 12, 21, 8]))
'''
