def parent(s: str) -> bool:
    parent_map = {"[":"]", "(":")", "{":"}"}
    stack = []
    
    for char in s:
        if char in parent_map:  
            stack.append(char)  # เจอวงเล็บเปิด → push
        else:
            if not stack:  # เจอปิดแต่ไม่มีเปิด
                return False
            top = stack.pop()
            if parent_map[top] != char:  # วงเล็บเปิดล่าสุด ไม่ match กับที่ปิด
                return False
    return not stack  # ถ้า stack ว่าง = ครบคู่


def parent2(s:str)->bool:
    parent_map = {"[":"]", "(":")", "{":"}"}
    stack = []
    for char in s:
        if char in parent_map:
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if parent_map[top] != char
                return False
    return not stack

