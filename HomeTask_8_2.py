"""HomeTask_8.

Given the list of integers ( positive , negative, zeros)
Find max multiplication of three values in list
l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]

Input: [-1, 1, 2, 0, 3, 12, 4, 5, -1, 6]
Output: Max value = "360". Nums are: (12, 5, 6)

Input: [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
Output: Max value = "2016". Nums are: (-7, 12, -24)
"""

l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
i = 0
l2 = [abs(num) for num in l1]
l2.sort(reverse=True)
max_list = []
max_value = 1
while i < 3:
    i = i + 1
    r = l2.pop(0)
    max_list = max_list + [r]
    max_value = max_value * r
# finding the nums with original sign
orig_nums = []
for num1 in l1:
    for num2 in max_list:
        mult = num1 * num2
        if mult == num2 * num2 or mult == num2 * -num2:
            orig_nums = orig_nums + [num1]
print(f'Max value = {max_value}. Nums are: {tuple(orig_nums)}')
# _________________8_2__________________
