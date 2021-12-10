import sys

def buildCards():
    d = {}
    i = 0
    player = []
    while line := sys.stdin.readline():
        temp = [int(i) for i in line.split()]
        if temp == []:
            if i != 0:
                d[i] = player
                player = []
            i += 1 
            continue
        player.append(temp)
    return d

def checkcards(cards,n):
    return False,-1

def findwinner(cards,numberlist):
    for drawnnum in numberlist:
        player = 1
        checkwinner,playerwin = checkcards(cards,drawnnum)
        if checkwinner and playerwin > 0:
            calculatewin(cards[playerwin])

def main():
    numberlist = [int(i) for i in sys.stdin.readline().strip().split(',')] #order in which numbers are picked
    cards = buildCards()
    print(cards)
    findwinner(cards,numberlist)

if __name__ == '__main__':
    main()
