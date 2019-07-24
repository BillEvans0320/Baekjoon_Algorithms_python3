# factorial
# key word : recursive function

def factorial(N = int):
    if N <= 1:
        return 1
    else:
        return N*factorial(N-1)

def main():
    N = int(input())
    print(factorial(N))
    return

if __name__ == "__main__":
    main()
