# Queue
class Queue:
    def __init__(self):
        self.list = []

    def push(self,x):
        self.list.append(x)

    def pop(self):
        if (self.empty()):
            return -1
        else:
            output =self.list[0]
            del self.list[0]
            return output

    def size(self):
        return len(self.list)

    def empty(self):
        if len(self.list) == 0:
            return 1
        else:
            return 0

    def front(self):
        if (self.empty()):
            return -1
        else:
            return self.list[0]

    def back(self):
        if (self.empty()):
            return -1
        else:
            return self.list[-1]



case_num = int(input())
Q = Queue() # 알파벳 Q를 Queue 클래스로

for i in range(case_num):
    cmd = list(input().split(' '))

    if cmd[0] == 'push':
        Q.push(cmd[1])              # 입력된 값은 push일 때만 들어간다.
    elif cmd[0] == 'pop':
        print(Q.pop())
    elif cmd[0] == 'size':
        print(Q.size())
    elif cmd[0] == 'empty':
        print(Q.empty())
    elif cmd[0] == 'front':
        print(Q.front())
    elif cmd[0] == 'back':
        print(Q.back())
