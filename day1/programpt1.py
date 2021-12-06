import sys

def count(vals):
    total = 0
    for i in range(len(vals)-1):
        
        if vals[i] < vals[i+1]:
            print(f'{vals[i]} is less than {vals[i+1]}')
            total += 1
    return total
def main():
    vals = []
    for line in sys.stdin:
        vals.append(int(line))
    print(count(vals))


if __name__ == '__main__':
    main()
