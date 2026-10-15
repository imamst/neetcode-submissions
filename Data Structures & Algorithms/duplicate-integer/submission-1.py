class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Using hash set
        # seen = set()

        # for x in nums:
        #     if x in seen:
        #         return True

        #     seen.add(x)

        # return False

        # More simpler wth
        return len(set(nums)) < len(nums)