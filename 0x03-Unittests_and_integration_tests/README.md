# 0x03. Unittests and Integration Tests

## Table of Contents
1. [Introduction](#introduction)
2. [Unit Tests](#unit-tests)
    - [What are Unit Tests?](#what-are-unit-tests)
    - [Example of Unit Tests](#example-of-unit-tests)
    - [Common Patterns](#common-patterns)
        - [Mocking](#mocking)
        - [Parameterization](#parameterization)
        - [Fixtures](#fixtures)
3. [Integration Tests](#integration-tests)
    - [What are Integration Tests?](#what-are-integration-tests)
    - [Example of Integration Tests](#example-of-integration-tests)
4. [Advanced Topics](#advanced-topics)
    - [Mocking Read-Only Properties](#mocking-read-only-properties)
    - [Memoization](#memoization)
5. [Conclusion](#conclusion)

## Introduction

This document covers the basics and advanced topics of unit testing and integration testing in Python, including common patterns such as mocking, parameterization, and fixtures.

## Unit Tests

### What are Unit Tests?

Unit tests are tests that focus on verifying the correctness of individual components or functions in isolation. They are fast to run and provide high granularity by testing small parts of the application.

### Example of Unit Tests

Here is a simple example of a unit test using Python's `unittest` module:

```python
import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
```

### Common Patterns

#### Mocking

Mocking is a technique used to replace real objects with mock objects to control the behavior of dependencies during testing.

```python
from unittest.mock import Mock

def fetch_data(api_client):
    return api_client.get('/data')

def test_fetch_data():
    mock_api_client = Mock()
    mock_api_client.get.return_value = {'key': 'value'}
    result = fetch_data(mock_api_client)
    assert result == {'key': 'value'}
```

#### Parameterization

Parameterization allows running the same test with different sets of data.

```python
from parameterized import parameterized
import unittest

class TestMath(unittest.TestCase):
    @parameterized.expand([
        ("addition", 1, 1, 2),
        ("subtraction", 2, 1, 1),
        ("multiplication", 2, 2, 4)
    ])
    def test_operations(self, name, input1, input2, expected):
        if name == "addition":
            result = input1 + input2
        elif name == "subtraction":
            result = input1 - input2
        elif name == "multiplication":
            result = input1 * input2
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
```

#### Fixtures

Fixtures are used to set up and tear down the test environment before and after a test.

```python
import unittest
import sqlite3

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)''')
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_insert_user(self):
        self.cursor.execute("INSERT INTO users (name) VALUES ('Bob')")
        self.conn.commit()
        self.cursor.execute("SELECT * FROM users WHERE name='Bob'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'Bob')

if __name__ == '__main__':
    unittest.main()
```

## Integration Tests

### What are Integration Tests?

Integration tests focus on verifying that different parts of the application work together correctly. They often require actual databases, network services, and other components, making them slower to run but essential for ensuring that integrated parts of the application function as expected.

### Example of Integration Tests

```python
import unittest
import sqlite3

class TestDatabaseIntegration(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)''')
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_database_insert(self):
        self.cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
        self.conn.commit()
        self.cursor.execute("SELECT * FROM users WHERE name='Alice'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'Alice')

if __name__ == '__main__':
    unittest.main()
```

## Advanced Topics

### Mocking Read-Only Properties

To mock a read-only property, you can use the `PropertyMock` class from `unittest.mock`.

```python
from unittest.mock import patch, PropertyMock
import unittest

class MyClass:
    @property
    def my_property(self):
        return 'original value'

class TestMyClass(unittest.TestCase):
    @patch('__main__.MyClass.my_property', new_callable=PropertyMock)
    def test_my_property(self, mock_property):
        mock_property.return_value = 'mocked value'
        instance = MyClass()
        self.assertEqual(instance.my_property, 'mocked value')

if __name__ == '__main__':
    unittest.main()
```

### Memoization

Memoization is a technique to cache the results of expensive function calls.

```python
import functools

@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Output: 55
print(fibonacci.cache_info())  # Cache information
```

## Conclusion

This document provides a comprehensive guide to writing unit tests and integration tests in Python. By understanding and applying these concepts, you can ensure the correctness and reliability of your code. If you have any questions or need further assistance, feel free to reach out.
```

This README provides an organized structure for the topics we've covered, with examples and explanations for each section. You can adjust the content as needed to fit your specific project requirements.