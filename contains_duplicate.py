class Solution(object):
    def containsDuplicate(self, nums):
        check = set()

        for i in nums:
            if i not in check:
                check.add(i)
            else:
                return True
        return False