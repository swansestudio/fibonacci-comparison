import os
import time
import timeit
os.system("cls")


number = 40
result = 0
fib_cache = {}


# ------------------------------------ Recursion ------------------------------------
def fibinacci_recursion(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibinacci_recursion(n - 1) + fibinacci_recursion(n - 2)


# ------------------------------ Recursion with a cache -------------------------------

def fib_cached(n):
    if n in fib_cache:
        return fib_cache[n]
    if n == 0 or n == 1:
        return n
    else:
        fib_cache[n] = fib_cached(n - 1) + fib_cached(n - 2)
        return fib_cache[n]


# ------------------------------ Non-recursive (Loop) Alg ---------------------------------

def fibonacci_loop(n):
    a = 0
    b = 1
    for i in range(n):
        temp = a
        a = b
        b = temp + b
    return a

# --------------------------- Driver and time measurement code ---------------------------
t0 = timeit.default_timer()
result = fibinacci_recursion(number)
t1 = timeit.default_timer()

print('Fibonacci of', number, '=', result)
print('Time RECURSION: %.6f s' % (t1 - t0))
print()


t0 = timeit.default_timer()
result = fib_cached(number)
t1 = timeit.default_timer()

print('Fibonacci of', number, '=', result)
print('Time CACHED: %.6f s' % (t1 - t0))
print()


t0 = timeit.default_timer()
result = fibonacci_loop(number)
t1 = timeit.default_timer()

print('Fibonacci of', number, '=', result)
print('Time LOOP: %.6f s' % (t1 - t0))
print()
