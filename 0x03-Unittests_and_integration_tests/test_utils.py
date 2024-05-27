#!/usr/bin/env python3
"""test utils module"""

import unittest
from unittest.mock import patch
from typing import Dict, Tuple, Union
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map
    args:
        unittest.TestCase
    """

    @parameterized.expand(
        [
            ({"a": 1}, ["a"], 1),
            ({"a": {"b": 2}}, ["a"], {"b": 2}),
            ({"a": {"b": 2}}, ["a", "b"], 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Dict, path: Tuple[str], expected: Union[Dict, int]
    ) -> None:
        """test access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ["a"], KeyError),
            ({"a": 1}, ["a", "b"], KeyError),
        ]
    )
    def test_access_nested_map_exception(
        self, nested_map: Dict, path: Tuple[str], expected: Union[Dict, int]
    ) -> None:
        """test access_nested_map method"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json
    args:
        unittest.TestCase
    """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(self, test_url: str, test_payload: Dict[str, bool]) -> None:
        """test that it returns a valid json
        args:
            test_url: str
            test_payload: Dict[str, bool]
        """
        response_dict = {"return_value.json.return_value": test_payload}
        with patch("requests.get", autospec=True, **response_dict) as mock_get:
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    test memoize
    """

    def test_memoize(self) -> None:
        """
        Test for memoize function
        """

        class TestClass:
            """
            Test class
            """

            def a_method(self):
                """a method function"""
                return 42

            @memoize
            def a_property(self):
                """a property function"""
                return self.a_method()

        with patch.object(TestClass, "a_method") as mocked:
            test = TestClass()
            self.assertEqual(test.a_property, mocked.return_value)
            self.assertEqual(test.a_property, mocked.return_value)
            mocked.assert_called_once()
