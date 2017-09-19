#!/usr/bin/env python3
import unittest
from tests.util import create_header,run_operation

class TestBL(unittest.TestCase):
    def setUp(self):
        with open('opcode/io/bl.bf') as f:
            self.file_content = f.read()

    def test_space_pushed(self):
        output = run_operation(self.file_content,[1,23,3,2,3,4])
        self.assertEqual(output,32)

class TestEmit(unittest.TestCase):
    def setUp(self):
        with open('opcode/io/emit.bf') as f:
            self.file_content = f.read()

    def test_simple_emit(self):
        output = run_operation(self.file_content,[1,3,3,2,4,4],footer='')
        self.assertEqual(output,4)

    def test_overflow_emit(self):
        output = run_operation(self.file_content,[1,3,3,2,4,256],footer='')
        self.assertEqual(output,0)

if __name__ == '__main__':
    unittest.main()
