def lengthOfLastWord(s: str) -> int:
    sp=s.split()
    result=sp[len(sp)-1]
    return len(result)



print(lengthOfLastWord("Hello World"))