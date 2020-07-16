import matplotlib.pyplot as plt
import numpy as np
import random

# P(m) = (A ^ n) / ((K ^ n) + A ^ n)

# A is the experimentally measured transcript abundance
# K is the abundance for which the probability of being mobile is 50%,
# and n gives the steepness of the curve.

# K is the number of mRNA that decide to move 50 % of the time
# Under the sassumption that K is completely random:
# The more mRNA you have, higher chance of it being mobile?

K = 0
K_list = []
A_list = []
A = int(input("How many transcripts do we have initially? : "))
n = int(input("Put in a steepness for the curve? : "))

# mobile over nonmobile = y-axis
for i in range(0, A):
    
    bagels = random.randint(1,10)
    if bagels <= 5:
        K += 1

def saturation(A, K, A_list, n):
    
    counter = 0
    probability = []
    
    for i in range(len(A_list)):
        probability.append((A_list[counter] ** n) / (K ** n + A_list[counter] ** n))
    
        counter += 1
  
 
    
    # A_list = np.linspace(1, A, len(K_list))
    
    plt.plot(np.log(A_list), probability, 'b--')
    plt.title("Probability of mRNA being mobile")
    plt.xlabel("ln(Total Number of mRNA)")
    plt.ylabel("Probability of mRNA being mobile")
    plt.show()
    
    return probability




for i in range(1, A):
    A_list.append(i)

saturation(A, K, A_list, n)

