import numpy as np

def convert_input_to_list(path):
    with open(path,'r') as input:
        list = [str(entry.rstrip().replace(" ","")) for entry in input]
        return list

def solve_gamma_rate(input):
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

print(solve_gamma_rate(convert_input_to_list("inputtest.txt")))