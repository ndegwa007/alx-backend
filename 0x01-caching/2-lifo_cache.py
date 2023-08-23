#!/usr/bin/env python3
"""module implements cache LIFO system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class holds a LIFO caching system"""
    def __init__(self):
        """inherits from a base class"""
        self.stack = []
        super().__init__()

    def put(self, key, item):
        """adds items to cache within the limit"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                key not in self.cache_data.keys():
            last_key = self.stack.pop()
            self.cache_data.pop(last_key)
            print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """query the key value"""
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
