#!/usr/bin/env python3
"""
LRUCache module
"""
from base_caching import BaseCaching
from typing import Any


class LRUCache(BaseCaching):
    """
    A caching system that uses the Least Recently Used (LRU)
    algorithm to add and remove values.

    Inherits from BaseCaching.

    Methods:
    -------
    put(key: Any, value: Any) -> None:
        Adds a key-value pair to the cache. If the cache is at capacity,
        removes the Least recently used key-value pair.

    get(key: Any) -> Any:
        Returns the value associated with the given key.
        If the key doesn't exist, returns None.
    """

    def put(self, key: Any, value: Any):
        """
        Adds a key-value pair to the cache. If the cache is at capacity,
        removes the least recently used key-value pair.

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
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            key = next(iter(self.cache_data))
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
        try:
            value = self.cache_data.pop(key)
        except KeyError:
            return None
        self.cache_data[key] = value
        return self.cache_data.get(key)
