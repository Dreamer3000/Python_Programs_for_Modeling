from sympy import symbols, diff, exp, Derivative

def generalized_derivative(subx, suby, subz):
    x,y,z = symbols('x y z')
    expression1 = 2 * x ** 2 + 6 * x + 4
    
    answer = diff(expression1)
    print("The general derivative of expression1 is " + str(answer))
    
    specific = answer.subs(x,subx)
    print()
    print("""The specific answer of this expression when replacing the variable
with """ + str(subx) + """ is """ + str(specific))
    
    
apples = input("What varialbe/s do you want to use? x, y or z: ")
tacos = apples.split()
if 'x' in tacos:
    bagels = input("What number do you want to replace x with? :")
    subx = int(bagels)
elif 'x' not in tacos:
    subx = 0

if 'y' in tacos:
    bagels = input("What number do you want to replace x with? :")
    suby = int(bagels)
elif 'y' not in tacos:
    suby = 0

if 'z' in tacos:
    bagels = input("What number do you want to replace x with? :")
    subz = int(bagels)
elif 'z' not in tacos:
    subz = 0

generalized_derivative(subx, suby, subz)

# let's do some partial derivatives now
# first off, we'll get the partial derivates of e ^ (x * y * z)
def partial_derivative():
    x,y,z = symbols('x y z')
    xderiv = int(input("How many derivates do you want to find for x? : "))
    yderiv = int(input("How many derivates do you want to find for y? : "))
    zderiv = int(input("How many derivates do you want to find for z? : "))
    
    expression = exp(x * y * z)
    answer = diff(expression, x, xderiv, y, yderiv, z, zderiv)
    print()
    print(answer)
    print()
    # To create an unevaluated derivative, do the following:
    derivative = Derivative(expression, x, xderiv, y, yderiv, z, zderiv)
    # To evaluate this unevaluated derivative:
    result = derivative.doit()
    print(result)

partial_derivative()
    
    

