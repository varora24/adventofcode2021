import sys

def count(vals):
    total = 0
    merge = []
    for i in range(len(vals)-2): 
        temp = vals[i]+vals[i+1]+vals[i+2]
        merge.append(temp)
    for i in range(len(merge)-1):
        if merge[i] < merge[i+1]:
            print(f'{merge[i]} is less than {merge[i+1]}')
            total += 1
    return total
def main():
    vals = []
    for line in sys.stdin:
        vals.append(int(line))
    print(count(vals))


if __name__ == '__main__':
    main()
