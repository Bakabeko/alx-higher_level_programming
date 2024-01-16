#!/usr/bin/python3
for i in range(ord('a') , ord('z') +1):
    if i != ord('q') and i != ord('c'):
        print("{:c}".format(i),end = " ")
