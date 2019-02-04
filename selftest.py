#!/usr/bin/env python3
import unittest

def hello():
    return True

class MyTest(unittest.TestCase):
    def test_hello(self):
        self.assertTrue(hello())

if __name__ == "__main__":
    unittest.main()