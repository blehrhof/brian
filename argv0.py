import sys

if len(sys.argv) == 2:
    print("hello, {}".format(sys.argv[1]))
else:
    print("hello,world")

for i in range(len(sys.argv)):
    print(sys.argv[i])

for s in sys.argv:
    for c in s:
        print(c)
    print()

if len(sys.argv) != 2:
    print("missing command line argument")
    # exit code = "0" is success, otherwise error
    exit(1)