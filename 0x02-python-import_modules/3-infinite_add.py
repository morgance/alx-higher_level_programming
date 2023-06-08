#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result_of_add = 0

    for arg in sys.argv:
        if arg != sys.argv[0]:
            result_of_add += int(arg)
    print(result_of_add)
