from modsim.modsim import *
import matplotlib.pyplot as plt
from modsim.modsim import flip as flip2
from numpy import *
import pint
import random
from sympy import *

def differential_solver(alpha, beta, type0):
    
    dfdt = diff(f(t), t)
    
    eq1 = Eq(dfdt, type0)
    solution1 = dsolve(eq1)
    
    # Let's sub C1 for p_0 (p_0 is the initial population/value of the function P)
    C1, p_0 = symbols("C1 p_0")
    particular_solution = solution1.subs(C1, p_0)
    general_solution = solution1.rhs # isolationg right side of equation
    
    A = (K - p_0) / p_0
    logistic = K / (1 + A * exp(-r*t))
    
    at_0 = general_solution.subs(t,0)
    solutions = solve(Eq(at_0, p_0), C1)
    
    ans_C1 = solutions[0]
    
    particular_solution = general_solution.subs(C1, ans_C1)
    simplified = simplify(particular_solution)
    
    tacos = simplified.subs(t,0)
    if str(tacos) == "p_0":
        print("Your answer is:", str(simplified))
        print("Without initial condition p_0, your answer is:", str(simplified.subs(p_0, 0)))
        result = simplified.subs(p_0, 1)
       
        print("Your  answer at t = 0 is: ", str(tacos), "If this isn't p_0 there's a problem somewhere.") # should come out to p_0 
        # print(simplify(simplified - logistic)) # used to check logistic equation
    else:
        print("Invalid input, check your variables")
    print(result)
    
    return result

    
alpha = symbols('alpha')
beta  = symbols("beta")
t = symbols("t")
f = Function("f")
r, K = symbols("r K")
sigma = symbols("sigma")
M = sigma / K
h  = UNITS.hour 
gamma = 2 
type1 = alpha*f(t) + beta * f(t)**2 # quadratic growth equation
type2 = alpha*f(t) # proportional growth equation
type3 = r*f(t) * (1-f(t)/K) # logistic growth equation --> dP/dt = r*P(1 - P/K)
type4 = K * f(t) * (f(t) - M) # Death equation? hard to check if true since answer is so messy
type5 = gamma
# predator prey differentail equation


def plotter(result, title, xlabel, ylabel):
    
    """ This isn't working at the moment, can't convert result into a satisfactory data type """
    t = np.arange(0,10,1)

    
    plt.plot(t, result, "--", color = "blue")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(["2 * x"])
    plt.title(title)
    plt.show()
    
result = differential_solver(alpha, beta, type4)
print(result)
print(type(result))
