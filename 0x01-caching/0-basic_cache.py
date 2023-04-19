#!/usr/bin/env python3
"""
BasicCache module
"""
from base_caching import BaseCaching
from typing import Any


class BasicCache(BaseCaching):
    """
     A simple caching system that stores key-value pairs in memory.

    Inherits from BaseCaching.

    Methods:
    -------
    put(key: Any, value: Any) -> None:
        Adds a key-value pair to the cache. If the key already exists,
        its value is updated.

    get(key: Any) -> Any:
        Returns the value associated with the given key.
        If the key doesn't exist, returns None.

    """

    def put(self, key: Any, value: Any):
        """
        Adds a key-value pair to the cache. If the key already exists,
        its value is updated.

        Parameters:
        ----------
        key : Any
            The key of the key-value pair to add to the cache.
        value : Any
            The value of the key-value pair to add to the cache.

        Returns:
        -------
        None
        """
        if key is None or value is None:
            return
        self.cache_data[key] = value

    def get(self, key: Any) -> Any:
        """
        Returns the value associated with the given key.
        If the key doesn't exist, returns None.

        Parameters:
        ----------
        key : Any
            The key of the key-value pair to retrieve from the cache.

        Returns:
        -------
        Any
            The value associated with the given key, or None if
            the key doesn't exist in the cache.
        """
        if key is None:
            return

        return self.cache_data.get(key)
