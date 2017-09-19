#!/usr/bin/env python3
import unittest
from tests.util import create_header,run_operation

class TestCells(unittest.TestCase):
    def setUp(self):
        with open('opcode/dataspace/cells.bf') as f:
            self.file_content = f.read()

    def test_correct_value(self):
        output = run_operation(self.file_content,[2,2,4,4,2,3,4,5,12434,4,54])
        self.assertEqual(output,2)

if __name__ == '__main__':
    unittest.main()
