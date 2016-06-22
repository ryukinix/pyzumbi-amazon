x = int(input("Insira o número do termo Fibonacci: "))
[a, b, n] = [0, 1, 1]
while x > n:
    b = a + b
    a = b - a
    n = n + 1
print("Fib(%d) = %d" %(x, b))
