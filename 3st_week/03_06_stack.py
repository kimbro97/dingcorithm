class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        # 어떻게 하면 될까요?
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # pop 기능 구현
    def pop(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "Stack is empty!"
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "Stack is empty!"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.head is None


stack = Stack()
stack.push(4)
print(stack.peek())

stack.push(3)
print(stack.head.data)

print(stack.pop())
print(stack.pop())
print(stack.pop())