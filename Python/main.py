import timeit
from functools import partial
import numpy as np

def differentialOne(x, y):
    return x + y

def eulerMethod(func, iterations: int, step: float, x0: float, y0: float):
    XValues = x0 + step * np.arange(iterations + 1)
    YValues = np.zeros(iterations + 1)
    YValues[0] = y0

    for i in range(iterations):
        YValues[i + 1] = YValues[i] + func(XValues[i], YValues[i]) * step

    return XValues, YValues


def eulerImprovedMethod(func, iterations, step, x0, y0):
    XValues = x0 + step * np.arange(iterations + 1)
    YValues = np.zeros(iterations + 1)
    YValues[0] = y0

    for i in range(iterations):
        YNextEstimate = YValues[i]+func(XValues[i],YValues[i])*step
        aMid = (func(XValues[i],YValues[i])+func(XValues[i+1],YNextEstimate))/2
        YValues[i+1]=YValues[i]+aMid*step
    
    return XValues, YValues


def RK4(func, iterations, step,x0,y0):
    XValues = x0 + step * np.arange(iterations + 1)
    YValues = np.zeros(iterations + 1)
    YValues[0] = y0

    for i in range(iterations):
        k1 = func(XValues[i],YValues[i])
        k2 = func(XValues[i] + 1/2 * step, YValues[i] + 1/2 * step * k1)
        k3 = func(XValues[i] + 1/2 * step, YValues[i] + 1/2 * step * k2)
        k4 = func(XValues[i] + step, YValues[i] + k3 * step)

        k = (k1+2*k2+2*k3+k4)/6

        YValues[i+1] = YValues[i] + k*step
    return XValues,YValues

def timing(iterations:int, func,functionIters:int,step:float,x0:float,y0:float)->tuple[float,float,float]:
    eulerTimer = timeit.Timer(partial(eulerMethod, func, functionIters, step,x0,y0))
    eulerImprovedTimer = timeit.Timer(partial(eulerImprovedMethod, func, functionIters, step,x0,y0))
    RK4Timer = timeit.Timer(partial(RK4,func, functionIters, step,x0,y0))
    eulerTime = eulerTimer.timeit(number=iterations)
    eulerImprovedTime = eulerImprovedTimer.timeit(number=iterations)
    RK4Time = RK4Timer.timeit(number=iterations)
    print(
        f"Euler metode tid: {eulerTime:.5f} \n"
        f"Euler forbedret metode tid: {eulerImprovedTime:.5f} \n"
        f"RK4 tid: {RK4Time:.5f}"
    )

    return (eulerTime,eulerImprovedTime,RK4Time)

def accuracy(func, iterations: int, step: float, x0: float, y0: float, solution):
    eulerResults = eulerMethod(func, iterations, step, x0, y0)
    eulerImprovedResults = eulerImprovedMethod(func, iterations, step, x0, y0)
    RK4Results = RK4(func, iterations, step, x0, y0)

    XActualResults = x0 + step * np.arange(iterations + 1)
    YActualResults = np.array([solution(x) for x in XActualResults])

    def compute_percentage_diff(approx_values):
        return np.abs((approx_values - YActualResults) / YActualResults) * 100

    eulerError = compute_percentage_diff(eulerResults[1])
    eulerImprovedError = compute_percentage_diff(eulerImprovedResults[1])
    RK4Error = compute_percentage_diff(RK4Results[1])

    return {
        "Euler Method": eulerError,
        "Euler Improved Method": eulerImprovedError,
        "RK4 Method": RK4Error
    }



def main():
    times = timing(100000, differentialOne,100,0.2,0,0)
    difference = accuracy(differentialOne, 100,0.2,0,0,lambda x: np.e**x - x - 1)
    print(difference)
    


if __name__ == "__main__":
    main()
