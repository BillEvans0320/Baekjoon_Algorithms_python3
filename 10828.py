# Stack
class Stack:
    def __init__(self):
        self.list = []

    def push(self,x):
        self.list.append(x)

    def pop(self):
        if (self.empty()):
            return -1
        else:
            output =self.list[-1]
            del self.list[-1]
            return output

    def size(self):
        return len(self.list)

    def empty(self):
        if len(self.list) == 0:
            return 1
        else:
            return 0

    def top(self):
        if (self.empty()):
            return -1
        else:
            return self.list[-1]


case_num = int(input())
S = Stack()

for i in range(case_num):
    cmd = list(input().split(' '))

    if cmd[0] == 'push':
        S.push(cmd[1])              # 입력된 값은 push일 때만 들어간다.
    elif cmd[0] == 'pop':
        print(S.pop())
    elif cmd[0] == 'size':
        print(S.size())
    elif cmd[0] == 'empty':
        print(S.empty())
    elif cmd[0] == 'top':
        print(S.top())
