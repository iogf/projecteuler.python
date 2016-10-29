def sum_fib():
    sum = 0
    a, b = 1, 2

    while b <= 4000000:
        if not b % 2:
            sum += b

        a, b = b, a + b
        
    print sum

sum_fib()
        
