def strStr(haystack:str, needle:str)->int:
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)]==needle:
            return i
    return -1

def strStr(haystack: str, needle: str) -> int:
    if needle == "":
        return 0

    # 1) สร้าง LPS ของ needle
    def build_lps(p: str):
        lps = [0] * len(p)
        j = 0  # ความยาว prefix/suffix ที่แมตช์อยู่
        for i in range(1, len(p)):
            while j > 0 and p[i] != p[j]:
                j = lps[j - 1]
            if p[i] == p[j]:
                j += 1
                lps[i] = j
        return lps

    lps = build_lps(needle)

    # 2) วิ่งหาใน haystack
    j = 0  # index ใน needle
    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = lps[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j == len(needle):
            return i - j + 1  # ตำแหน่งที่เจอครั้งแรก
    return -1



print(strStr("sadbutsad","sad"))