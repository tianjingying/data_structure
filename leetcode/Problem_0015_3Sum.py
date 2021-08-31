class Solution:
    
    def twoSum(self, nums, end, target):
        # 先判断两和是否等于 target   target=0-nums[i]  
        sum = 0
        left = 0
        right = end
        ans_list = []

        
        while(left != right):
            if nums[left] + nums[right] < target:
                left += 1
                
            elif nums[left] + nums[right] > target:
                right -= 1
                
            else:
                if left == 0 or nums[left] != nums[left-1]:
                    cur = []
                    cur.append(nums[left])
                    cur.append(nums[right])
                    ans_list.append(cur)
                    
                left += 1                    
            
        return ans_list
    
    def threeSum(self, nums):
        if not nums:
            return []
        
        if nums[0] == 0 and len(nums) == 1:
            return []
        
        return_list = []
        
        nums.sort()  # 降序排序
        
        for i in range(len(nums)-1, 1, -1):
            print(f"i: {i}")
            if i != len(nums) - 1 and nums[i] == nums[i+1]:
                # 从后往前遍历，如果当前元素等于后一个元素，不进行运算
                continue
               
            two_sum_list = self.twoSum(nums, i-1, 0 - nums[i])
            for j in range(len(two_sum_list)):
                two_sum_list[j].append(nums[i])
                return_list.append(two_sum_list[j])
                
        return return_list
            
            
if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    print(Solution().threeSum(nums))
