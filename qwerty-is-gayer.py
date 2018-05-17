#!/usr/bin/env python
import random

def main():
    while True:
        fn = open(f'f{random.randrange(1, 1000)}.txt', 'a')
        fn.write('qwerty is gay lol!! !! ! ! !111!!!!\n')
        fn.close()

if __name__ == '__main__':
    main()