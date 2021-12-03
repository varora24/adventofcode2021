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

    for i in range(len(data[0])):
        for vals 

def main():
    data = []
    while line:=sys.stdin.readline().strip():
        data.append(line)
    print(findvals(data))
    
if __name__ == '__main__':
    main()
