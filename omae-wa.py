#!/usr/bin/env python

def main():
    n = 0
    while True:
        f = open(f'omaewa{n}.txt', 'a')
        for i in range(n+15):
            f.write('omae wa mou shinderu\n')
        f.close()
    
        f = open(f'nani{n}.txt', 'a')
        for j in range(n+3):
            print('nani?!')
            f.write('nani?!\n')
        f.close()

        n += 1


if __name__=='__main__':
    main()