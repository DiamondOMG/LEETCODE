def addBinary(a: str, b: str) -> str:
    i,j =len(a)-1,len(b)-1
    out=[]
    carry=0
    while i>-1 or j>-1 or carry:
        x = int(a[i])if i >=0 else 0
        y = int(b[j])if j >=0 else 0
        s = x + y + carry
        c = s%2
        out.append(str(c))
        carry = s // 2
        i -= 1
        j -= 1
    return "".join(reversed(out))




print(addBinary("101010","111"))