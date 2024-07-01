#!/usr/bin/env python3
'''
Test cases for the utils module
'''
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


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


class TestGetJson(unittest.TestCase):
    '''
    Familiarize yourself with the utils.get_json function.

    Define the TestGetJson(unittest.TestCase) class and implement the
    TestGetJson.test_get_json method to test that utils.get_json returns the
    expected result.

    We don’t want to make any actual external HTTP calls. Use
    unittest.mock.patch to patch requests.get. Make sure it returns a Mock
    object with a json method that returns test_payload which you parametrize
    alongside the test_url that you will pass to get_json with the following
    inputs:

    test_url="http://example.com", test_payload={"payload": True}
    test_url="http://holberton.io", test_payload={"payload": False}
    Test that the mocked get method was called exactly once (per input) with
    test_url as argument.

    Test that the output of get_json is equal to test_payload.
    '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        '''
        A test function for the function using parameterized and
        expected results mocked
        '''
        with patch('utils.requests.get') as mock_get:
            # Create a Mock response object with the desired json method
            mock_response = Mock()
            mock_response.json.return_value = test_payload

            # Set the mock object to return the mock response
            mock_get.return_value = mock_response

            # Call the function with the test URL
            result = get_json(test_url)

            # Check that requests.get was called once with the correct URL
            mock_get.assert_called_once_with(test_url)

            # Check that the function returned the expected payload
            self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
