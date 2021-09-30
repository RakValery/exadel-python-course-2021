#Task 06: Decorators
import time
def measure_elapsed_time(fn):
    def execution_time(*arg, **kwarg):
        start = time.time()
        res = fn(*arg, **kwarg)
        end = time.time()
        print(f"Function {fn} with arg {arg, kwarg} execution time:{end-start} seconds.")
        return res
    return execution_time
def fib(n: int):
    if type(n) is not int:
        try:
            n = int(n)
        except ValueError:
            print(f"ValueError: Value {n} ({type(n)}) must be a integer")
            return 0
    if  n < 0:
        return fib(n + 2) - fib(n + 1)
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
@measure_elapsed_time
def wait_xsecs(x):
    time.sleep(x)
    return f"I waited for {x} sec"
@measure_elapsed_time
def fib_ex(n):
    return(fib(n))
print(fib_ex(10))
print(wait_xsecs(8))