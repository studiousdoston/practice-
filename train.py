'''K-TASK (PYTHON)

Shunday function yozing, u string qabul qilsin va string ichidagi eng uzun sozni qaytarsin.
MASALAN: find_longest("I come from Uzbekistan") return "Uzbekistan"'''

# ⭐️ Masalaning yechimi
def find_longest(text):
  words = text.split()
  longest = ''
  for word in words:
    if len(word)>len(longest):
      longest = word
  return longest

print(find_longest("I come from Uzbekistan"))

  
'''Steps:
1.split the string into each words
2.compare the length of the word with the previous one
3. return the longest
'''

'''I-TASK (PYTHON)

Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
MASALAN: get_digits("m14i1t") return qiladi "141"
'''
'''
# ⭐️ Masalaning yechimi
def get_digits(string):
  empty_list = []
  for num in string:
    if num.isdigit():
      empty_list.append(num)
  
  return "".join(empty_list)

print(get_digits("m14i1t46j9"))
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
