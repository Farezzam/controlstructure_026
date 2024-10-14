def evaluate_performance(percentage):
    if percentage >= 90:
        print("Excellent performance")
    elif percentage >= 80:
        print("Very Good performance")
    elif percentage >= 70:
        print("Good performance")
    elif percentage >= 60:
        print("Average performance")
    else:
        print("Needs improvement")

def find_largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

def print_odd_numbers(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i, end=" ")

def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()

