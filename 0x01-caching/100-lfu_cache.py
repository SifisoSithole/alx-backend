#!/usr/bin/env python3
"""
LFUCache module
"""
from base_caching import BaseCaching
from typing import Any
from doubly_linked_list import DoubleLinkedList


class LFUCache(BaseCaching):
    """
    A caching system that uses the Least Frequently Used (LFU)
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

    def __init__(self):
        """
        Initialize class
        """
        self.__linked_list = DoubleLinkedList()
        super().__init__()

    def put(self, key: Any, value: Any):
        """
        Adds a key-value pair to the cache. If the cache is at capacity,
        removes the most recently used key-value pair.

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
            self.__linked_list.update_node(key)
        else:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                k = self.__linked_list.delete_tail_node()
                del self.cache_data[k]
                print('DISCARD:', k)
            self.__linked_list.add_node(key)
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
        value = self.cache_data.get(key)
        if value is not None:
            self.__linked_list.update_node(key)
        return value
