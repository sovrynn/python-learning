# https://leetcode.com/problems/count-good-triplets/
class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        ans = 0
        arr_len = len(arr)
        for i1 in range(arr_len):
            for i2 in range(i1 + 1, arr_len):
                for i3 in range(i2 + 1, arr_len):
                    if abs(arr[i1] - arr[i2]) <= a and abs(arr[i2] - arr[i3]) <= b and abs(arr[i1] - arr[i3]) <= c:
                        ans += 1
        return ans