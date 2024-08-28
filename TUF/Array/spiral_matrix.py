class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []

        n = len(mat)
        m = len(mat[0])

        top = 0
        left = 0
        bottom = n - 1
        right = m - 1

        while top <= bottom and left <= right:
            # for moving left to right
            for i in range(left, right + 1):
                ans.append(mat[top][i])
            top += 1

            # for moving top to bottom
            for i in range(top, bottom + 1):
                ans.append(mat[i][right])
            right -= 1

            # for moving right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(mat[bottom][i])
                bottom -= 1

            # for moving bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(mat[i][left])
                left += 1

        return ans
