#!/usr/bin/env python3
import unittest
from tests.util import create_header,run_operation

class TestDrop(unittest.TestCase):
    def setUp(self):
        with open('stack/drop.bf') as f:
            self.file_content = f.read()

    def test_drop(self):
        output = run_operation(self.file_content,[10,2000])
        self.assertEqual(output,10)

class TestPick(unittest.TestCase):
    def setUp(self):
        with open('stack/pick.bf') as f:
            self.file_content = f.read()

    def test_simple_pick(self):
        output = run_operation(self.file_content,[10,20,30,40,50,2])
        self.assertEqual(output,30)

    def test_top_pick(self):
        output = run_operation(self.file_content,[10,20,30,40,50,0])
        self.assertEqual(output,50)

    def test_deep_pick(self):
        stack = list(range(5000+1))
        stack.append(4000)
        output = run_operation(self.file_content,stack)
        self.assertEqual(output,1000)


if __name__ == '__main__':
    unittest.main()
