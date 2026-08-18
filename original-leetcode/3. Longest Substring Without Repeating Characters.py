def lengthOfLongestSubstring( s: str) -> int:
    last = {}           # char -> last index
    L = 0
    ans = 0
    for R, ch in enumerate(s):
        if ch in last and last[ch] >= L:
            L = last[ch] + 1           # กระโดด L ข้ามตัวซ้ำ
        last[ch] = R
        ans = max(ans, R - L + 1)
    return ans

print(lengthOfLongestSubstring("abcabcbb"))