#!/usr/bin/env python3
import functools 
import numpy
import tempfile
import subprocess
import sys

with open('arithmetic/add.bf') as f:
    add_file = f.read()

x = numpy.arange(65000,2**16)
y = numpy.arange(65000,2**16)

for i in y:
    for j in x:
        header = ''.join(['+>' , ''.join(['+']*(i//2**8)),
               '>+>' , ''.join(['+']*(i%2**8)) ,
               '>+>',''.join(['+']*(j//2**8)) ,
               '>+>',''.join(['+']*(j%2**8)),'<<<'])

        with tempfile.NamedTemporaryFile(mode='w',delete=True) as f:
            f.write(''.join((header,'\n',add_file,'>.>>.')))
            f.flush()
            result = subprocess.run(['bf',f.name],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)
        output = int.from_bytes(result.stdout,'big')
        expect = ((i//2**8)*2**8 + (i%2**8) + (j//2**8)*2**8 + (j%2**8))%2**16
        if(expect != output):
            print(' i : {} j : {} '.format(i,j))
            print(' expect : {} '.format(expect))
            print(' output : {} '.format(output))
            sys.exit(1)
    print(i)

        


