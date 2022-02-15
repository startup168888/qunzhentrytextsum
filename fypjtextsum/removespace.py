f = open("test2.txt")
for line in f:
        line = line.rstrip()
        if line:
                print(line, end = '')
