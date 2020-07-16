from sympy import symbols, diff, exp, Derivative, integrate, cos, sin, simplify

# we can integrate with sympy with the integrate() function
x,y,z = symbols("x y z")
bagels = integrate(cos(x), x)
print(bagels)
print()

# the simplify() function  takes in your competed integral and 'pretties it up' for lack of a better word
def integrater(function, x):
    
    answer = integrate(function, x)
    print(simplify(answer))

mangos = input("Enter some functions that we'll integrate, followed by commas. If you don't want to add anything, type n: ")
things = mangos.split(",")
f = open("functions.txt", "a+")

for function in things:
    if function in "functions.txt":
        pass
    elif function.lower() == 'n':
        break
    else:
        f.write(function + ",")
f.close()

f = open("functions.txt", "r")
f.seek(0)
    
text = f.readline()
text_list = text.split(",")
print(text_list)
# print(text_list)

for function in text_list:
    if function == "cos(x)":
        integrater(cos(x), x)
    elif function == 'sin(x)':
        integrater(sin(x), x)
    elif function == 'cos(x) ** 2':
        integrater(cos(x) ** 2, x)
    elif function == 'sin(x) ** 2':
        integrater(sin(x) ** 2, x)
        
# integrater(sin(x), x)
    