class Solution:
    def minimumSum(self, num: int) -> int:
      digits = list(str(num))
      digits.sort()

      num1 = digits[0] + digits[2]
      num2 = digits[1] + digits[3]

      return int(num1) + int(num2)