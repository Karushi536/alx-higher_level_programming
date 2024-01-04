#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    result = 0

    for i in range(1, argc + 1):
        result += int(argv[i])

    print(result)
