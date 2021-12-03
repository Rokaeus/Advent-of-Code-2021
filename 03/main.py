import numpy as np

def convert_input_to_list(path):
    with open(path,'r') as input:
        list = [str(entry.rstrip().replace(" ","")) for entry in input]
        return list

def solve_common_bit_gamma(input):
    binaryresults = []
    for i in range(0,(len(input[0]))):
        zeros = 0
        ones = 0
        for row in input:
            if row[i] == "0":
                zeros += 1
            elif row[i] == "1":
                ones += 1
        
        if zeros > ones:
            binaryresults.append(0)
        elif ones > zeros:
            binaryresults.append(1)

    return binaryresults

def solve_common_bit_epsilon(input):
    binaryresults = []
    for i in range(0,(len(input[0]))):
        zeros = 0
        ones = 0
        for row in input:
            if row[i] == "0":
                zeros += 1
            elif row[i] == "1":
                ones += 1
        
        if zeros > ones:
            binaryresults.append(1)
        elif ones > zeros:
            binaryresults.append(0)

    return binaryresults

def binaryToDecimal(n):
    return int(n,2)

def solve_gamma(list):
    gamma_string = ""
    for x in list:
        gamma_string += str(x)
    return (binaryToDecimal(gamma_string))

def solve_epsilon(list):
    epsilon_string = ""
    for x in list:
        epsilon_string += str(x)
    return (binaryToDecimal(epsilon_string))

gamma = solve_gamma(solve_common_bit_gamma(convert_input_to_list("input.txt")))
epsilon = solve_epsilon(solve_common_bit_epsilon(convert_input_to_list("input.txt")))
consumtion = gamma * epsilon
print(consumtion)