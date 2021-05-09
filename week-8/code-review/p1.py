# https://leetcode.com/problems/count-the-number-of-consistent-strings/
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        for word in words:
            is_consistent = True
            for c in word:
                if c not in allowed:
                    is_consistent = False
            if is_consistent:
                ans += 1
        return ans
