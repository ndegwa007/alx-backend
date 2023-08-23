#!/usr/bin/env python3
"""module implements cache using FIFO"""
from collections import deque
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class inherits from the base class"""
    def __init__(self):
        """initialize this class"""
        super().__init__()
        self.q = deque()

    def put(self, key, item):
        """put the dict values in FIFO algo"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and
        key not in self.cache_data.keys():
            oldest_key = self.q.popleft()
            self.cache_data.pop(oldest_key)
            print("DISCARD: ", oldest_key)
        self.cache_data[key] = item
        self.q.append(key)

    def get(self, key):
        """get cache key values"""
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
