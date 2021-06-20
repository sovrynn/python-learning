# https://leetcode.com/problems/truncate-sentence/
class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        words = s.split()
        ans = ""
        for i in range(k):
            ans += words[i]
            if i < k - 1:
                ans += " "
        return ans
