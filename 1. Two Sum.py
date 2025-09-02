def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i in range(len(nums)):
        need = target-nums[i]
        
        
        if need in seen :
            return [i,seen[need]]
        seen[nums[i]]=i
        print("need = ",need,"seen=",seen,"i = ",i)


print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
# print(twoSum([3,3],9))