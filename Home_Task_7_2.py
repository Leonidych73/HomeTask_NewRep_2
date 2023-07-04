"""HomeTask_7.

Convert a non-negative integer num to its English words representation.
Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

let's take that number always > 100 and only three digits
100 <= num <= 999
"""
number = 215

num_words = {
    0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
    7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve',
    13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
    18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
    50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
}

hundreds = number // 100
tens = (number % 100) // 10 * 10
ones = number % 10

words_hundreds = num_words[hundreds] + ' Hundred'
words_tens = num_words[tens]
words_ones = num_words[ones]
words_tins = num_words[tens + ones] if tens == 10 else num_words[0]

result = f'{words_hundreds} {words_tins}' if tens == 10 else f'{words_hundreds} {words_tens} {words_ones}'

assert 100 <= number <= 999, "Error! The number should be >= 100 and <= 999"
print(result)
