class Solution:
    def minimumSum(self, num: int) -> int:
      digits = []
      for i in range(4):
        digits.append(num%10)
        num //= 10
      digits.sort()

      num1 = digits[0]*10 + digits[2]
      num2 = digits[1]*10 + digits[3]

      return num1 + num2