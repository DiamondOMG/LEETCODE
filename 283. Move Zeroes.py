def moveZeroes( nums: list[int]) -> None:
    for i in range(len(nums)-1,-1,-1):
        if nums[i]==0:
            nums.append(nums.pop(i))
        print(nums)

def moveZeroes2( nums: list[int]) -> None:
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
        print(nums)

print(moveZeroes2([0,0,0,0,0,1,0,3,12]))