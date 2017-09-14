class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def listitems(self):
        return self.items[::-1]


stackobj = Stack()
print(stackobj.isEmpty())
stackobj.push(10)
stackobj.push(20)
print(stackobj.isEmpty())
stackobj.pop()
print(stackobj.peek())
stackobj.push(30)
stackobj.push(40)
print(stackobj.size())
print(stackobj.listitems())



