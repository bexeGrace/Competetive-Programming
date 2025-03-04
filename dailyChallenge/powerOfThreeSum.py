class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        remainder = f'{n % 3}'
        quotient = n // 3

        while quotient > 0:
            remainder = f'{quotient % 3}' + remainder
            quotient = quotient // 3
        
        if '2' in remainder:
            return False
        return True