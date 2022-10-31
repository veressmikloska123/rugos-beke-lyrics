#!/usr/bin/python

import sys

if len(sys.argv) > 1:
 if(sys.argv[1] == "y"):
  print("There is need for help")
  if len(sys.argv) > 2:
   i = 0
   print("Verse 0:")
   with open(sys.argv[2], 'r') as f:
    fuckinglines = f.readlines()
    for fr in fuckinglines:
     if(fr == "\n"):
      i += 1
      print("\nVerse "+str(i)+":")
     else:
      print(fr)
  else:
   print("WARNING: You do not know how it works. Refrain from doing that again.")
 else:
  print("WARNING: You do not know if this is for you. Please refrain from using this code block anytime after.")
else:
 print("WARNING: This code reads rugos beke lyrics. To continue, use the y modifier to do so.")

 print("Lesser instruments: for a better life. no limits in underlife")
