import sys
import math

def filter_data_bitwise(data, filter_by_most_common,bits):
    filtered = [x for x in data]
    for bit in reversed(bits):
        ratio = sum(1 for num in filtered if num & bit) / len(filtered)
        wanted_bit_value = bit * int((ratio >= 0.5) == filter_by_most_common)
        filtered = [x for x in filtered if x & bit == wanted_bit_value]
        if len(filtered) == 1:
            break
    return filtered

def main():
    data = []
    while line:=sys.stdin.readline().strip():
        data.append(line)
    n = len(data[0])
    bits = [2 ** x for x in range(n)]
    d = [int(line,base=2) for line in data]
    filtered_by_most_common = filter_data_bitwise(d,True,bits)
    filtered_by_least_common = filter_data_bitwise(d,False,bits)    
    print(filtered_by_most_common[0] * filtered_by_least_common[0])
    
if __name__ == '__main__':
    main()
