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
def run_operation(file_content,stack):

    header = create_header(stack)
    with tempfile.NamedTemporaryFile(mode='w',delete=True) as f:
        f.write(''.join((header,'\n',file_content,'>.>>.')))
        f.flush()
        result = subprocess.run(['bf',f.name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        return int.from_bytes(result.stdout,'big')

class TestAddition(unittest.TestCase):
    def setUp(self):
        with open('arithmetic/add.bf') as f:
            self.file_content = f.read()

    def test_simple_subtract(self):
        output = run_operation(self.file_content,[5,5])
        self.assertEqual(output,(5+5)%2**16)
    
    def test_wrong_answer(self):
        output = run_operation(self.file_content,[10,5])
        self.assertNotEqual(output,100)

    def test_overwrap(self):
        output = run_operation(self.file_content,[65531,10])
        self.assertEqual(output,5)

    def test_add_zero(self):
        output = run_operation(self.file_content,[5,0])
        self.assertEqual(output,5)

class TestSubtraction(unittest.TestCase):
    def setUp(self):
        with open('arithmetic/sub.bf') as f:
            self.file_content = f.read()

    def test_simple_subtract(self):
        output = run_operation(self.file_content,[10,5])
        self.assertEqual(output,5)


    def test_underwrap(self):
        output = run_operation(self.file_content,[5,10])
        self.assertEqual(output,65531)

    def test_subtract_zero(self):
        output = run_operation(self.file_content,[5,0])
        self.assertEqual(output,5)

class TestMultiplication(unittest.TestCase):
    def setUp(self):
        with open('arithmetic/mul.bf') as f:
            self.file_content = f.read()

    def test_simple_multiply(self):
        output1= run_operation(self.file_content,[3,4])
        output2= run_operation(self.file_content,[4,3])
        self.assertEqual(output1,12)
        self.assertEqual(output2,12)

    def test_multiply_zero(self):
        output1 = run_operation(self.file_content,[0,4])
        output2 = run_operation(self.file_content,[4,0])
        self.assertEqual(output1,0)
        self.assertEqual(output2,0)

    def test_identity(self):
        output1 = run_operation(self.file_content,[1,4])
        output2 = run_operation(self.file_content,[4,1])
        self.assertEqual(output1,4)
        self.assertEqual(output2,4)


if __name__ == '__main__':
    unittest.main()
