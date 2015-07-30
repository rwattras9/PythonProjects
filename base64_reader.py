# Python code to read Mirth base64 error messages
# Author: rwattras

#!/usr/bin/python

import base64, sys

if (len(sys.argv) != 1): 
	print "usage: python base64_reader.py"
else: 
	print("Paste gibberish Mirth error code here (enter CTL-C when done): ")
	
	code = []
	while True:
		try:
			codeLine = raw_input()
			code.append(codeLine)
		except KeyboardInterrupt:
			break

	codeString = ''.join(code)
	decode = base64.b64decode(codeString)
	print("\n\nDecoded error text:\n\n\t" + decode + "\n")
