class Solution:
    def addBinary(self, a: str, b: str) -> str:
        intA = int(a, 2)
        intB = int(b, 2)

        intSum = intA + intB

        return bin(intSum)[2:]
        