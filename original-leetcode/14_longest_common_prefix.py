def longest (strs:list[str])->str:
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while  not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix: 
                return ""
    return prefix

def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
    
    for i in range(len(strs[0])):   # loop ตามความยาวของ string แรก
        char = strs[0][i]
        for s in strs[1:]:
            # ถ้า string สั้นเกิน หรือเจอ char ไม่ตรง → return prefix ที่เจอก่อนหน้า
            if i >= len(s) or s[i] != char:
                return strs[0][:i]

print(longest(["flower", "flow", "flight"])  )