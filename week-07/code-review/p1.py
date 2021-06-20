# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        ans = 0
        for start_index in range(len(arr)):
            arr_len = 1
            while start_index + arr_len <= len(arr):
                subarray = arr[start_index:start_index + arr_len]
                subarray_sum = sum(subarray)
                ans += subarray_sum
                arr_len += 2
        return ans
