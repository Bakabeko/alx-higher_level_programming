#!/usr/bin/python3
# 3-infinite_add.py
# abubkr
if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys
    count = 0
    for i in range(len(sys.argv) - 1):
        count += int(sys.argv[i + 1])
    print("{}".format(count))
