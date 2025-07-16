def find(nums,l,r):
    if l>r:
        return
    mid = (l+r)//2
    if len(nums) == 1:
        return nums[0]

    if mid !=0 and mid != len(nums)-1:
        if nums[mid+1]!= nums[mid] and nums[mid-1]!=nums[mid]:
            return nums[mid]
    elif mid==0:
        if nums[mid+1]!= nums[mid]:
            return nums[mid]
    else:
        if nums[mid-1]!=nums[mid]:
            return nums[mid]
    a = find(nums , mid+1 , r)
    b = find(nums, l , mid-1)
    print(a,b)
    return a if b == None else b


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return find(nums,0,len(nums)-1)