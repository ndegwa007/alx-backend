#!/usr/bin/env python3
"""module implements a cache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class adds a caching system"""

    def __init__(self):
        """inherits the __init__ method"""
        super().__init__()

    def put(self, key, item):
        """adds item to the cache_data dict"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get key values"""
        if key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
