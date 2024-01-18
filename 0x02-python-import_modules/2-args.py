#!/usr/bin/python3
# 2-args.py
# abubkr moaz

if __name__ == "__main__":

    """Print the number of and list of arguments."""

    import sys
    count = len(sys.argv)
    if count == 0:
        print("{} arguments.", sys.len(argv))
    else:
        print("{} arguments: ".format(count - 1))
        for i in range(1, count):
            print("{}: {}".format(i, sys.argv[i]))
