class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers = {
            'M':1000,
            'D':500,
            'C':100,
            'L':50,
            'X':10,
            'V':5,
            'I':1,
            }
        int_s = 0
        prev_number = 0

        for i in reversed(s):
            if roman_numbers[i] < prev_number:
                int_s -= roman_numbers[i]
           
            else:
                int_s += roman_numbers[i]
            
            prev_number = roman_numbers[i]

        return int_s