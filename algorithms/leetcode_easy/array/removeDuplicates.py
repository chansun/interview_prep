class Solution:
    def removeDuplicates(self, nums):
        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        nums = nums[:index+1]
        print(nums)
        return index + 1
        
a = Solution()
temp = [0,0,1,1,1,2,2,3,3,4]
print(a.removeDuplicates(temp))