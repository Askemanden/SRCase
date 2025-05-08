import timeit
from functools import partial

def differentialOne(x, y):
    return x + y

def eulerMethod(func, iterations, step):
    for i in range(200):
        x = 1 + 1

def eulerImprovedMethod(func, iterations, step):
    for i in range(200):
        x = 1 + 1

def RK4(func, iterations, step):
    for i in range(200):
        x = 1 + 1

def timing(iterations):
    eulerTimer = timeit.Timer(partial(eulerMethod, 1, 1, 1))
    eulerImprovedTimer = timeit.Timer(partial(eulerImprovedMethod, 1, 1, 1))
    RK4Timer = timeit.Timer(partial(RK4, 1, 1, 1))
    eulerTime = eulerTimer.timeit(number=iterations)
    eulerImprovedTime = eulerImprovedTimer.timeit(number=iterations)
    RK4Time = RK4Timer.timeit(number=iterations)
    print(
        f"Euler metode tid: {eulerTime:.5f} \n"
        f"Euler forbedret metode tid: {eulerImprovedTime:.5f} \n"
        f"RK4 tid: {RK4Time:.5f}"
    )

def main():
    timing(100000)



if __name__ == "__main__":
    main()
