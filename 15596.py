# key word : if __name__ == '__main__':

def solve(a):
    return sum(a)

def main():
    a = list(map(int,input().split()))
    print(solve(a))

if __name__ == "__main__":
    main()
