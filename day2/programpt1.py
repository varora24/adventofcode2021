import sys

def main():
    hor = 0
    depth = 0
    while line:=sys.stdin.readline().strip():
        info,val = line.split()
        if info == 'forward':
            hor += int(val)
        elif info == 'down':
            depth += int(val)
        elif info == 'up':
            depth -= int(val)
    print(depth*hor)

if __name__ == '__main__':
    main()
