class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            match (i % 3 == 0, i % 5 == 0):
                case (True, True):
                    answer.append("FizzBuzz")
                case (True, False):
                    answer.append("Fizz")
                case (False, True):
                    answer.append("Buzz")
                case (False, False):
                    answer.append(str(i))
        return answer
