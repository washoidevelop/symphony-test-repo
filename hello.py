def hello():
    print("Hello, World!")

def count_down(n):
    for i in range(n, 0, -1):
        print(i)

if __name__ == "__main__":
    count_down(5)
