class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


s = Stack()
print(s.is_empty())  # True

s.push(1)
s.push(2)
s.push(3)
print('s is stack: ', s)
print(s.is_empty())  # False

print(s.pop())  # 3
print(s.pop())  # 2
print(s.pop())  # 1
print(s.is_empty())  # True