#!/usr/bin/env python3
'''
Test cases for the utils module
'''
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''
    Familiarize yourself with the utils.access_nested_map function and
    understand its purpose. Play with it in the Python console to make sure
    you understand.

    In this task you will write the first unit test for
    utils.access_nested_map.

    Create a TestAccessNestedMap class that inherits from unittest.TestCase.

    Implement the TestAccessNestedMap.test_access_nested_map method to test
    that the method returns what it is supposed to.

    Decorate the method with @parameterized.expand to test the function for
    following inputs:

    nested_map={"a": 1}, path=("a",)
    nested_map={"a": {"b": 2}}, path=("a",)
    nested_map={"a": {"b": 2}}, path=("a", "b")
    For each of these inputs, test with assertEqual that the function returns
    the expected result.

    Implement TestAccessNestedMap.test_access_nested_map_exception. Use the
    assertRaises context manager to test that a KeyError is raised for the
    following inputs (use @parameterized.expand):

    nested_map={}, path=("a",)
    nested_map={"a": 1}, path=("a", "b")
    Also make sure that the exception message is as expected.

    The body of the test method should not be longer than 2 lines.
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        ''' test case for the function using the parameterized '''
        self.assertEqual(access_nested_map(
            nested_map=nested_map, path=path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        ''' test case for the function for exceptions '''
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map=nested_map, path=path)

        self.assertEqual(cm.exception.args[0], path[-1])


if __name__ == "__main__":
    unittest.main()
