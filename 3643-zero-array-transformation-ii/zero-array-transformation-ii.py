class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        q = len(queries)
        if q == 0:
            return -1 if any(nums) else 0

       
        if all(val <= 0 for val in nums):
            return 0

        left = 0
        right = q - 1
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            diff = [0] * (n + 1)
            for i in range(mid + 1):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val

            current = 0
            valid = True
            for i in range(n):
                current += diff[i]
                if current < nums[i]:
                    valid = False
                    break

            if valid:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer + 1 if answer != -1 else -1
