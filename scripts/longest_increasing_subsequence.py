from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums) -> int:
        # tails[i] is the smallest tail of any increasing subsequence of length i + 1.
        tails = []
        for number in nums:
            index = bisect_left(tails, number)
            if index == len(tails):
                tails.append(number)
            else:
                tails[index] = number
        return len(tails)
