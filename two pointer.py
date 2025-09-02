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
    while nums[L] + nums[R] != target:
        if target < nums[L] or L > len(nums)-1:
            return "Not found"
        if nums[L] + nums[R] > target:
            R -=1
        if nums[L] + nums[R] < target:
            L +=1
    return [L,R]

def two_pointer2(nums:list[int],target:int)->list[int]:
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


print(two_pointer([1, 2, 3, 4, 6], 6))