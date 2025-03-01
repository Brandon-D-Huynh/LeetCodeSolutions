from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # This is a simple problem. The naive approach is to take each element and iterate
        # over the array until we find a duplicate, but this has a chance of being O(n^n)
        # since we would be iterating over the array (n) n times. 

        # A better solution is to use a hashmap data structure, which would allow us to simply
        # iterate over the array one time. This is because every time we add an element to our 
        # hashmap O(1), we can add it to the hashmap O(1), and we can also check that element
        # against the hashmap O(1) to see if the element has already appeared. This also uses
        # O(n) memory since the hashmap can be as potentially big as the array.

        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)

        return False