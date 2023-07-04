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
# l1 = [-1, 1, 2, 0, 3, 12, 4, 5, -1, 6]
# l1 = [-1, -1, 1, 0, 3, 12, 12, -12, 12, 6]
# l1 = [-7, 12, 0]
# l1 = [-7, 12, 0, 0, 0]
# l1 = [0, 0, 0, 0]
# l1 = [-7, 7, -7]
# l1 = [-7, 7, -7, 9]
# l1 = [-7, 3]
assert len(l1) >= 3, "The list length should be >= 3"
sorted_l1 = sorted(l1, key=abs, reverse=True)  # Sort the list by absolute values in descending order
max_value = abs(sorted_l1[0] * sorted_l1[1] * sorted_l1[2])  # Find absolute max multiplication of three values in list
max_list = (sorted_l1[0], sorted_l1[1], sorted_l1[2])  # Create a list of maximum numbers with a sign
print(f'Max value = {max_value}. Nums are: {max_list}')

