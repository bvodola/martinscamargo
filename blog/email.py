#!/usr/bin/python

import sys

# output = open('/home/bvodola/example-script.out', 'a')
# output.write(sys.stdin.read())
# output.write(" TEST")
# output.close()

email = sys.stdin.read()
output = open('/home/bvodola/script.txt', 'w')
output.write(email)
output.close()