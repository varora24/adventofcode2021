import sys
import math

def finddecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def findvals(data):
    gamma = ""
    epsilon = ""
    for i in range(len(data[0])):
        ones = 0
        zeros = 0
        for vals in data:
            if vals[i]=='1':
                ones+=1
            else:
                zeros+=1
        if ones > zeros:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
        else:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
    g = finddecimal(int(gamma))
    e = finddecimal(int(epsilon))
    return g*e

def main():
    data = []
    while line:=sys.stdin.readline().strip():
        data.append(line)
    print(findvals(data))
    
if __name__ == '__main__':
    main()
