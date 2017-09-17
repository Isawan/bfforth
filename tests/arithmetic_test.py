#!/usr/bin/env python3
import functools 
import numpy
import tempfile
import subprocess
import sys
import unittest
import time

"""
This function generates a header to initilise the stack
"""
def create_header(stack):
    prehead = map(lambda x: ''.join([
        ''.join(['+']*(x//2**8)),
        '>+>',
        ''.join(['+']*(x%2**8))]), 
        stack)
    head = ''.join(['+>',
            '>+>'.join(prehead),
            '<<<'])
    return head


"""
This is a function to test arithmetic brainfuck operations
"""
def run_arithmetic_operation(file_content,stack):

    header = create_header(stack)
    with tempfile.NamedTemporaryFile(mode='w',delete=True) as f:
        f.write(''.join((header,'\n',file_content,'>.>>.')))
        f.flush()
        result = subprocess.run(['bf',f.name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        return int.from_bytes(result.stdout,'big')

class TestAdditionCorrectness(unittest.TestCase):
    def setUp(self):
        with open('arithmetic/add.bf') as f:
            self.file_content = f.read()

    def test_simple_subtract(self):
        output = run_arithmetic_operation(self.file_content,[5,5])
        self.assertEqual(output,(5+5)%2**16)
    
    def test_overwrap(self):
        output = run_arithmetic_operation(self.file_content,[65531,10])
        self.assertEqual(output,5)

    def test_add_zero(self):
        output = run_arithmetic_operation(self.file_content,[5,0])
        self.assertEqual(output,5)

class TestSubtractionCorrectness(unittest.TestCase):
    def setUp(self):
        with open('arithmetic/sub.bf') as f:
            self.file_content = f.read()

    def test_simple_subtract(self):
        output = run_arithmetic_operation(self.file_content,[10,5])
        self.assertEqual(output,5)

    def test_underwrap(self):
        output = run_arithmetic_operation(self.file_content,[5,10])
        self.assertEqual(output,65531)

    def test_subtract_zero(self):
        output = run_arithmetic_operation(self.file_content,[5,0])
        self.assertEqual(output,5)

if __name__ == '__main__':
    unittest.main()
