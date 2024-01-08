#!/usr/bin/env python3
"""Unittests and integration tests"""

from typing import Any, Dict, Tuple
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Dict[str, Any],
        path: Tuple[str, ...],
        expected_result: Any
    ) -> None:
        """
        Test the access_nested_map function.

        Args:
        - nested_map (dict): The nested map to access.
        - path (tuple): The path to the value in the nested map.
        - expected_result (any): The expected result
        of accessing the nested map.

        Returns:
        - None

        Raises:
        - AssertionError: If the actual result
        does not match the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
