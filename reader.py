#!/usr/bin/python

import sys

print("WARNING: This code reads rugos beke lyrics. To continue, use the y modifier to do so.")

if(sys.argv[1] == "y"){
 print("There is need for help")
  with open(sys.argv[2], 'r') as f:
    print(f.read())
}
