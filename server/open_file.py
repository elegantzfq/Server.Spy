

file = open('/proc/cpuinfo')
for line in file.readlines():
    print(line)
