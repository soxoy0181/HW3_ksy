def factorial(num):
    if (num <= 1): return 1
    return num * factorial(num-1)

def __main__():
    for i in range(0,15,2):
        print("%d! = %d"%(i,factorial(i)))

__main__()
