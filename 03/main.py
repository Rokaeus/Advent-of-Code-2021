import numpy as np

def convert_input_to_list(path):
    with open(path,'r') as input:
        list = [str(entry.rstrip().replace(" ","")) for entry in input]

def convert_binary_to_int(binary):
    strings = [str(integer) for integer in binary]
    result = [int(entry, 2) for entry in strings]
    string = [bin(x,2) for x in result]
    return string

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
    
    results = convert_binary_to_int(binaryresults)
    return results

def convert_list_to_string(list):
    string = ""
    for element in list:
        string += element
    return string

print(solve_gamma_rate(convert_input_to_list('inputtest.txt')))