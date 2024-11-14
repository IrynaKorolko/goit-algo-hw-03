def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        if n <=0:
            return 0
        if n ==1:
            return 1
        if n in cache:
            return cache[n]
        if n not in cache:
            n_fib = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = n_fib
        return cache[n]
    return fibonacci
f = caching_fibonacci()
print(f(5))

