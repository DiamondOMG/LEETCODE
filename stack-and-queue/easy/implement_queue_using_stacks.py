"""LeetCode 232: Implement Queue using Stacks | สร้างคิวด้วยสแตก

Problem (EN): Implement a FIFO queue using only stack operations. Support
push, pop, peek, and empty.
โจทย์ (TH): สร้างคิวแบบ FIFO โดยใช้การทำงานของ stack รองรับ push, pop,
peek และ empty

Examples / ตัวอย่าง:
1) push(1), push(2), peek() -> 1
2) pop() -> 1
3) empty() after removing all -> True
4) push(3), peek() -> 3
"""


class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())   # 1
print(queue.pop())    # 1
print(queue.pop())    # 2
print(queue.empty())  # True
queue.push(3)
print(queue.peek())   # 3
