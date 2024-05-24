class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        # thêm 1 phần tử vào ngăn xếp bằng cách thêm 1 phần tử vào cuối danh sách
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return None
        # lấy một phần tử ra từ đỉnh ngăn xếp bằng cách loại bỏ phần tử cuối cùng của danh sách
    def isEmpty(self):
        return len(self.stack) == 0
        # isEmpty kiểm tra xem ngăn xếp đã trống chưa bằng cách kiểm tra độ dài của danh sách
    def isFull(self):
        return False

    def count(self):
        return len(self.stack)

    def printStack(self):
        print(self.stack)
        
# tạo stack
stack1 = Stack()
stack1.push(9)
stack1.push(10)
stack1.push(8)
stack1.push(11)
stack1.pop()
stack1.printStack()

print(stack1.isEmpty())
print(stack1.isFull())
print(stack1.count())