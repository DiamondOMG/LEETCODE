from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                # ข้าม node ซ้ำ
                current.next = current.next.next
            else:
                # เลื่อนไปข้างหน้า
                current = current.next
        return head

head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

sol = Solution()
new_head = sol.deleteDuplicates(head)

def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

printList(new_head)