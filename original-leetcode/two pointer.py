"""
    โจทย์:
    ให้ nums เป็น list ของจำนวนเต็มที่เรียงจากน้อยไปมาก และมี target เป็นผลรวมที่ต้องการ
    เขียนฟังก์ชันหาว่า index ของตัวเลข 2 ตัวใดใน nums รวมกันแล้วได้ค่าเท่ากับ target

    ตัวอย่าง Input/Output:

    print(two_pointer([1, 2, 3, 4, 6], 6))  # ➝ [1, 3]  เพราะ nums[1]=2, nums[3]=4
    print(two_pointer([2, 3, 4], 6))        # ➝ [0, 2]
    print(two_pointer([2, 3, 4], 8))        # ➝ []
"""

def two_pointer(nums:list[int],target:int)->list[int]:
    L = 0
    R = len(nums)-1
    while L < R:
        if nums[L] + nums[R] == target:
            return [L,R]
        if nums[L] + nums[R] > target:
            R -=1
        if nums[L] + nums[R] < target:
            L +=1

    return []


#print(two_pointer([1, 2, 3, 4, 6], 6))

"""
    โจทย์:
    ให้ nums เป็น list ของจำนวนเต็มที่เรียงจากน้อยไปมาก (อาจมีค่าติดลบได้)
    เขียนฟังก์ชันคืนค่า list ของ ค่ากำลังสองทั้งหมด แล้วเรียงจากน้อยไปมาก

    ตัวอย่าง Input/Output:

    Input: [-4, -1, 0, 3, 10]  
    Output: [0, 1, 9, 16, 100]  

    Input: [-7, -3, 2, 3, 11]  
    Output: [4, 9, 9, 49, 121]  


    ใช้ two pointer เพื่อทำให้ได้ O(n) ไม่ใช่ O(n log n)
"""

def two_pointer2(nums:list[int])->list[int]:
    L = 0
    R = len(nums)-1
    return []

##print(two_pointer([-4, -1, 0, 3, 10]))

    """โจทย์ 3:

ให้ nums เป็น list ของจำนวนเต็มที่เรียงจากน้อยไปมาก
เขียนฟังก์ชันหาคู่ (i, j) ทั้งหมด ที่ทำให้ nums[i] + nums[j] < target และคืนค่า จำนวนคู่ที่เป็นไปได้

ตัวอย่าง Input/Output:

Input: nums = [-1, 1, 2, 3], target = 3  
Output: 5   # คู่ที่เป็นไปได้คือ (-1,1), (-1,2), (-1,3), (1,2), (1,3)
    """
def two_pointer3(nums:list[int],target:int)->int:
    L=0
    R=len(nums)-1
    count=0
    while L < R :
        if nums[L]+nums[R] < target:
            count= count + R - L
            L+=1
        if nums[L]+nums[R] >= target:
            R-=1
    return count

#print(two_pointer3([-1, 1, 2, 3],4))
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        L, R = i + 1, n - 1
        target = -nums[i]
        while L < R:
            s = nums[L] + nums[R]
            if s == target:
                res.append([nums[i], nums[L], nums[R]])
                L += 1; R -= 1
                while L < R and nums[L] == nums[L-1]: L += 1
                while L < R and nums[R] == nums[R+1]: R -= 1
            elif s < target:
                L += 1
            else:
                R -= 1
    return res

# ตัวอย่าง
#print(three_sum([-1,0,1,2,-1,-4]))  


