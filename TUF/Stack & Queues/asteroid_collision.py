"""We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet."""

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:  # a < 0
        # Destroy the previous positive one(s).
                while stack and stack[-1] > 0 and stack[-1] < -a:
                    stack.pop()
                    if not stack or stack[-1] < 0:
                        stack.append(a)
                    elif stack[-1] == -a:
                        stack.pop()  # Both asteroids explode.
                    else:  # stack[-1] > the current asteroid.
                        pass  # Destroy the current asteroid, so do nothing.

        return stack