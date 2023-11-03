#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arguments = len(sys.argv) -1
    if num_arguments == 0:
        print("No arguments.")
    else:
        if num_arguments == 1:
            print("1 argument.")
        else:
            print("{} arguments:".format(num_arguemnts))
            for i, arg in enumerate(sys.argv[1:], start=1):
                print("{}: {}".format(i, arg))

