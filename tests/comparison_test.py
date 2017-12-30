#!/usr/bin/env python3
import unittest
from brainwrap.util import run_arithmetic

class TestEquals(unittest.TestCase):
    def setUp(self):
        with open('opcode/comparison/equals.bf') as f:
            self.file_content = f.read()

    def test_five_equals_five(self):
        output = run_arithmetic(self.file_content,[5,5])
        self.assertEqual(output,1)

    def test_five_not_equal_six(self):
        output = run_arithmetic(self.file_content,[5,6])
        self.assertEqual(output,0)
    
    def test_six_not_equal_five(self):
        output = run_arithmetic(self.file_content,[6,5])
        self.assertEqual(output,0)

    def test_zero_equals_zero(self):
        output = run_arithmetic(self.file_content,[0,0])
        self.assertEqual(output,1)

    def test_zero_not_equals_five(self):
        output = run_arithmetic(self.file_content,[0,5])
        self.assertEqual(output,0)

    def test_512_equals_512(self):
        output = run_arithmetic(self.file_content,[512,512])
        self.assertEqual(output,1)

    def test_512_not_equal_2048(self):
        output = run_arithmetic(self.file_content,[512,2048])
        self.assertEqual(output,0)

    def test_3453_equals_3453(self):
        output = run_arithmetic(self.file_content,[3453,3453])
        self.assertEqual(output,1)
    
    def test_3453_not_equals_5321(self):
        output = run_arithmetic(self.file_content,[3453,5321])
        self.assertEqual(output,0)



if __name__ == '__main__':
    unittest.main()
