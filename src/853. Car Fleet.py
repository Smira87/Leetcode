from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pairs)[::-1]: # Reverse sorted order
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
sol = Solution()
print(sol.carFleet(target, position, speed))