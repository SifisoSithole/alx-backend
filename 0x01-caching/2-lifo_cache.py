#!/usr/bin/env python3
"""
LIFOCache module
"""
from base_caching import BaseCaching
from typing import Any


class LIFOCache(BaseCaching):
    """
    A caching system that uses the Last-In-First-Out (LIFO)
    algorithm to add and remove values.

    Inherits from BaseCaching.

    Methods:
    -------
    put(key: Any, value: Any) -> None:
        Adds a key-value pair to the cache. If the cache is at capacity,
        removes the newest key-value pair.

    get(key: Any) -> Any:
        Returns the value associated with the given key.
        If the key doesn't exist, returns None.
    """

    def put(self, key: Any, value: Any):
        """
        Adds a key-value pair to the cache. If the cache is at capacity,
        removes the newest key-value pair.

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
        if key in self.cache_data.keys():
            self.cache_data.pop(key)
        self.cache_data[key] = value
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            iterator = iter(self.cache_data.items().__reversed__())
            next(iterator)
            key, _ = next(iterator)
            self.cache_data.pop(key)
            print('DISCARD:', key)

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
