#!/usr/bin/env python3
import unittest
from brainwrap.util import run_dataspace


class TestBridge(unittest.TestCase):
    def setUp(self):
        with open('opcode/dataspace/bridge.bf') as f:
            self.file_content = f.read()

    def test_simple_bridge(self):
        output = run_dataspace(self.file_content,
                [2,13,0,3,0,0,0,3,0,42,0,34,0,32],
                init_cursor=2,
                footer=''.join(['<<']+['.>']*7*2))
        self.assertEqual(list(output),
                [2,13,0,0,0,0,1,3,1,42,1,34,0,32])

    def test_long_bridge(self):
        tape = [ 1, 2, 1, 2, 0, 0]
        exp  = [ 1, 2, 0, 0, 0, 0] + [1,0]*(256+2) +[0,0]
        foot = ''.join(['<<']+['.>']*2*(3+256+2+1))
        output = run_dataspace(self.file_content, tape, 2, foot)
        self.assertEqual(list(output),exp)

    def test_even_longer_bridge(self):
        tape = [1, 2, 250, 30, 0, 0]
        exp  = [1, 2, 0,  0, 0, 0] + [1,0]*(256*250 + 30) + [0,0]
        foot = ''.join(['<<']+['.>']*2*(3+256*250+30+1))
        output = run_dataspace(self.file_content, tape, 2, foot)
        self.assertEqual(list(output),exp)

class TestStore(unittest.TestCase):
    def setUp(self):
        with open('opcode/dataspace/store.bf') as f:
            self.file_content = f.read()

    def test_store_first(self):
        tape = [10, 0, 0, 5, 0, 0]
        exp  = [  0, 0, 0,  0, 0, 0] + [1,0]*5 + [0, 10, 0, 0]
        foot = ''.join(['<<']+['.>']*2*(3+ 5 + 2))
        output = run_dataspace(self.file_content, tape, 2, foot)
        self.assertEqual(list(output),exp)

    def test_store_second(self):
        tape = [  0, 10, 0, 5, 0, 0]
        exp  = [  0, 0, 0,  0, 0, 0] + [1,0]*5 + [0, 0, 0, 10]
        foot = ''.join(['<<']+['.>']*2*(3+ 5 + 2))
        output = run_dataspace(self.file_content, tape, 2, foot)
        self.assertEqual(list(output),exp)

    def test_store_all(self):
        tape = [10, 10, 0, 5, 0, 0]
        exp  = [  0, 0, 0,  0, 0, 0] + [1,0]*5 + [0, 10, 0, 10]
        foot = ''.join(['<<']+['.>']*2*(3+ 5 + 2))
        output = run_dataspace(self.file_content, tape, 2, foot)
        self.assertEqual(list(output),exp)

if __name__ == '__main__':
    unittest.main()
