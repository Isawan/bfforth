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
        self.assertEquals(output,0)


if __name__ == '__main__':
    unittest.main()
