
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
