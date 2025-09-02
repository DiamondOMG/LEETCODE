def plusOne(digits: list[int]) -> list[int]:
    i=1
    if digits[len(digits)-i] == 9:
        while digits[len(digits)-i] == 9:
            digits[len(digits)-i]=0
            if digits[len(digits)-i-1]:
                digits[len(digits)-i-1]+=1
            else :
                digits.insert(0,1)
            i=i+1
        return digits
    digits[len(digits)-i]=digits[len(digits)-i]+1
    return digits

def plusOne2(digits: list[int]) -> list[int]:
    for i in range(len(digits)-1,-1,-1):
        if digits[i]< 9:
            digits[i] = digits[i]+1
            return digits
        digits[i] = 0
    return [1]+digits
    

print(plusOne2([9]))