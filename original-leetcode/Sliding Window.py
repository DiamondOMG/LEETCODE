"""
    โจทย์:
    ให้ nums เป็น list ของจำนวนเต็ม และมีตัวเลข k
    ให้หาผลรวมมากที่สุดของ subarray ที่มีความยาวเท่ากับ k

    ตัวอย่าง Input/Output:

    Input: nums = [2, 1, 5, 1, 3, 2], k = 3
    Output: 9 (เพราะ subarray [5,1,3] มีผลรวม = 9 มากที่สุด)

    Input: nums = [2, 3, 4, 1, 5], k = 2
    Output: 7 (subarray [3,4] = 7)

"""
def slide_window_1(nums:list[int],k:int)->int:
    max=0
    for i in range(len(nums)-k+1):
        if i == 0:
            max = sum(nums[i:i+k])
        if sum(nums[i:i+k]) > max :
            max = sum(nums[i:i+k])

    return max

# print(slide_window_1([2, 1, 5, 1, 3, 2],3))
# print(slide_window_1([2, 3, 4, 1, 5],2))
"""
        โจทย์:

    ให้ nums เป็น list ของจำนวนเต็ม และมีตัวเลข k
    ให้หาค่า ค่าเฉลี่ยมากที่สุด ของ subarray ที่มีความยาวเท่ากับ k

    ตัวอย่าง Input/Output:

    Input: nums = [1, 12, -5, -6, 50, 3], k = 4
    Output: 12.75 (เพราะ subarray [-5, -6, 50, 3] มีค่าเฉลี่ย = 12.75 มากที่สุด)
"""

def slide_window_2(nums:list[int],k:int)->int:
    max_av = sum(nums[:k])/k
    for i in range(k,len(nums)):
        cur_av = max_av + (nums[i]-nums[i-k])/k
        max_av = max(cur_av,max_av)
    return max_av

# print(slide_window_2([1, 12, -5, -6, 50, 3],4))
# print(slide_window_2([5, 5, 5, 5],2))

"""
        โจทย์:

        ให้ nums เป็น list ของจำนวนเต็ม + และมีตัวเลข k
        ให้หาจำนวน subarray ที่มีผลรวม ≤ k

        ตัวอย่าง Input/Output:

        Input:

        nums = [1, 2, 1, 0, 1, 1, 0], k = 4

        Output:

        23

        (มีทั้งหมด 23 subarray ที่ผลรวม ≤ 4)
""" 

def subarray(nums: list[int], target: int) -> int:
    count = 0
    R = 0
    window_sum = 0
    n = len(nums)
    for L in range(n):
        # ขยาย R เท่าที่ยังไม่เกิน target
        while R < n and window_sum + nums[R] <= target:
            window_sum += nums[R]
            R += 1
        count += R - L 
        print("count =",count,"L =",L,"R=",R)
        # เก็บให้ window_sum เป็น sum(nums[L+1:R])
        if R > L:
            window_sum -= nums[L]
        else:
            # ถ้า R == L ให้เลื่อนไปข้างหน้าเพื่อรักษา invariant
            R = L + 1
    return count

        
        
    return count

#print(subarray([1, 2, 1, 0, 1, 1, 0],4))
"""
โจทย์ 1

ให้ nums เป็น list ของจำนวนเต็ม + และมีตัวเลข k
หาผลรวม น้อยที่สุด ของ subarray ที่มีความยาวเท่ากับ k
"""
def min_sum_subarray (nums:list[int],k:int)->int:
    min_sum_subarray=sum(nums[:k])
    n=len(nums)
    for i in range(k,n):
        curr_sum_subarray=min_sum_subarray+nums[i] - nums[i-k]
        min_sum_subarray=min(curr_sum_subarray,min_sum_subarray)

    return min_sum_subarray

#print(min_sum_subarray([1, 2, 1, 0, 1, 1, 0],4))