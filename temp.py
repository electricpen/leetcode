def better_fibonacci(n):
    if n < 2:
        return n
    else:
        temp = 0
        last = 1
        curr = 1
        count = 2
        while count < n:
            temp = last
            last = curr
            curr = temp + last
            count += 1
        return curr


print(better_fibonacci(2))
print(better_fibonacci(3))
print(better_fibonacci(4))
print(better_fibonacci(5))
print(better_fibonacci(6))
print(better_fibonacci(7))
