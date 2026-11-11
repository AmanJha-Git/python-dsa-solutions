class Solution(object):
    def containsDuplicate(self, nums):
       # Since a Python set automatically removes duplicate elements, you can simply compare the length of the set to the length of the original list 
       # return len(set(nums)) != len(nums)
        
        # 2nd method:
        checker = set()
        for num in nums:
            if num in checker:
                return True
            checker.add(num)
        return False
        
        
        """
        :type nums: List[int]
        :rtype: bool
        """
        