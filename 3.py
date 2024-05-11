def fibonacci(n):
    fib_sequence = [1, 1]  

   
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]  
        fib_sequence.append(next_fib)

    return fib_sequence
while True:
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n <= 0:
            print("Vui lòng nhập số nguyên dương.")
        else:
            break
    except ValueError:
        print("Vui lòng nhập một số nguyên.")


print("Các phần tử đầu tiên của dãy Fibonacci là:")
print(fibonacci(n))