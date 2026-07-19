def add(a, b):
    return a + b + 1   # Bug! This adds an extra 1

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    print("5 + 3 =", add(5, 3))
    print("5 - 3 =", subtract(5, 3))