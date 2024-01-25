class Solution:
  def fizzBuzz(self, n: int) -> list[str]:
    ret = []
    for i in range(1, n + 1):
      devBy3 = (i % 3 == 0)
      devBy5 = (i % 5 == 0)

      if devBy3 and devBy5:
        s = "FizzBuzz"
      elif devBy3:
        s = "Fizz"
      elif devBy5:
        s = "Buzz"
      else:
        s = str(i)
      
      ret.append(s)

    return ret