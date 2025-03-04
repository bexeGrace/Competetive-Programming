from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        hi, lo = len(s) - 1, 0
        while hi > lo:
            s[hi], s[lo] = s[lo], s[hi]
            lo += 1
            hi -= 1
        


word = "abceabce"
arrayDictionary = [0]*26
offset = ord('a') # 'a' has ASCII value of 97
for char in word:
    ascii = ord(char)
    arrayDictionary[ascii - offset] += 1
print(arrayDictionary)