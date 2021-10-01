#!/usr/bin/python
import base64
import random

random.seed(0)
X_int   = [ random.getrandbits(n*8) for _ in range(m)  ]
X_bits  = [ [ 1 if num & (1 << pow2) else 0 for pow2 in range(n*8)  ] for num in X_int  ]
X_bytes = [ num.to_bytes(n, 'little') for num in X_int  ]
X_byte_array =  [ [ byte for byte in bytestr  ] for bytestr in X_bytes  ]

Y       = [ base64.b64encode(s) for s in X_bytes  ]
Y_int   = [ int.from_bytes(s, 'little')   for s in Y_bytes  ]
Y       = [ [1 if num & 1 << pow2 else 0 for pow2 in range(8*8) ] for num in Y_int  ]
Y_byte_array = [ [byte for byte in bytestr ] for bytestr in Y_bytes  ]



assert
with open()
