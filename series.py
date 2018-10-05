def fibonacci(n):
    first = 0
    second = 1
    if n==0:
        return (first)
    elif n==1:
        return (second)
    else:
        for i in range(n-1):
            nextnum = first + second
            first = second
            second = nextnum
        return (nextnum)
def lucas(n):
    first = 2
    second = 1
    if n==0:
        return (first)
    elif n==1:
        return (second)
    else:
        for i in range(n-1):
            nextnum = first + second
            first = second
            second = nextnum
        return (nextnum)
def sum_series(n, x=0, y=1):
    first = x
    second = y
    if n==0:
        return(first)
    elif n==1:
        return (second)
    else:
        for i in range(n-1):
            nextnum = first + second
            first = second
            second = nextnum
        return(nextnum)


assert fibonacci(7)==13, "Error in Fibonacci Function"
assert lucas(7)==29, "Error in Lucas Function"
assert sum_series(7)==13, "Error in generalized function (no optional Parameters)"
assert sum_series(7,2,1)==29, "Error in generalized function (optional Parameters)"