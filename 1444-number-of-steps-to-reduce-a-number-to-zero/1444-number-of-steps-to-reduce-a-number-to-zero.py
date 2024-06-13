class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        def numModder(num, steps):
            print(num, steps)
            if num == 0:
                return steps + 0
            elif num % 2 == 0:
                num = num // 2
                steps += 1
                return numModder(num, steps)

            else:
                num = num - 1
                steps += 1
                return numModder(num, steps)
            
    
            
        return numModder(num, steps)
        
