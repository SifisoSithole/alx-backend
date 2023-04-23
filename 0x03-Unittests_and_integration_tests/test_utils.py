#!/usr/bin/env python3


from unittest import TestCase
from typing import Mapping, Sequence, Union
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(TestCase):
    """
    Test cases for the access_nested_map function.
    """
    @parameterized.expand([
        # Test case 1: Access a value at the root level of the map
        ({"a": 1}, ("a",), 1),

        # Test case 2: Access a nested map at the root level of the map
        ({"a": {"b": 2}}, ("a",), {'b': 2}),

        # Test case 3: Access a value in a nested map
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping,
        path: Sequence,
        expected_output: Union[Mapping, int]
    ):
        """
        Test that the access_nested_map function returns the expected
        output for a given input.

        Parameters
        ----------
        nested_map : Mapping
            A nested map to be accessed.
        path : Sequence
            A sequence of keys representing a path to the value to be accessed.
        expected_output : Union[Mapping, int]
            The expected output from accessing the nested
            map with the given path.
        """
        output = access_nested_map(nested_map, path)
        self.assertEqual(output, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence, wrong_output: str
    ):
        """
        Test that accessing a non-existent key in
        a nested map raises a KeyError.

        Parameters
        ----------
        nested_map : Mapping
            A nested map.
        path : Sequence
            A sequence of keys representing a path to the non-existent value.
        wrong_output : str
            A string representation of the wrong output that
            should be raised by the function.

        Raises
        ------
        AssertionError
            If the function does not raise a KeyError
            with the expected wrong output.
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
            self.assertEqual(wrong_output, e.exception)
