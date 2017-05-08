'''
2017 Spring CS300 HW 7: Coin change Implementation

Author: 20130416 SEUNGHEE YOON, 20130289 PARK HAEOREUM
Due: 2017-05-01 10 AM

 - Written in single file (problem2_c.py) as guidance had demanded.

'''

def InputHandler(filename):
    f = open(filename, 'r')
    coins = f.readline().rstrip("\n").rstrip().split(" ")
    coins = [ int(e) for e in coins ]
    goal = int(f.readline().rstrip("\n").rstrip())
    return coins, goal

def DPSolution():
    coins, goal = InputHandler('input.txt')
    coins = ['coins:'] + coins
    print(coins)
    k = len(coins) - 1
    n = goal
    w = [ [ 0 for m in range(n+1)] for i in range(k+1) ]
    w = Init(w, k, n)
    #memoization_print(w, k, n)
    for i in range(1, k+1):
        for m in range(1, n+1):
            if m >= coins[i]:
                w[i][m] = w[i][m-coins[i]] + w[i-1][m]
            if m < coins[i]:
                w[i][m] = w[i-1][m]
    memoization_print(w, k, n)
    print("w[k][[n]:", w[k][n])
    OutputHandler(w[k][n])


def Init(w, k, n):
    for m in range(0, n+1):
        w[0][m] = 0
    for i in range(0, k+1):
        w[i][0] = 1
    return w

def memoization_print(w, k, n):
    print("Memoization Table follows: ")
    for i in range(k+1):
        for m in range(n+1):
            print(w[i][m], end= '  ')
        print()

def OutputHandler(number):
    f = open('output.txt', 'w')
    f.write(str(number))
    f.close()
DPSolution()