class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while cur != None:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        cur = self.head
        if cur == None:
            self.head = node
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        node = ListNode(val)
        cur = self.head
        i = 0

        if index == 0:
            self.addAtHead(val)
        else:
            while cur != None:
                if i == index - 1:
                    node.next = cur.next
                    cur.next = node
                    break
                cur = cur.next
                i += 1

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        i = 0

        if index == 0:
            if self.head != None:
                if self.head.next != None:
                    self.head = self.head.next
                else:
                    self.head = None

        while cur != None:
            if i == index - 1 and cur.next != None:
                cur.next = cur.next.next
                break
            cur = cur.next
            i += 1

    def print(self):
        cur = self.head
        if cur == None:
            print('---- My Linked List ----')
            print('Empty list!')
        else:
            while cur != None:
                print(cur.val, '-> ', end='')
                cur = cur.next
            print('None')


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1, 2)
# obj.get(1)
# obj.deleteAtIndex(1)
# obj.get(1)
# obj.get(3)
# obj.deleteAtIndex(1)
# obj.deleteAtIndex(0)
# obj.get(0)
# obj.deleteAtIndex(0)
# obj.get(0)
# obj.print()
