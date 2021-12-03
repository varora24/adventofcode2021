import sys

def main():
    hor = 0
    depth = 0
    aim = 0
    while line:=sys.stdin.readline().strip():
        info,val = line.split()
        if info == 'forward':
            hor += int(val)
            depth += ( aim * int(val) )
        elif info == 'down':
            aim += int(val)
        elif info == 'up':
            aim -= int(val)
    print(depth*hor)

if __name__ == '__main__':
    main()
