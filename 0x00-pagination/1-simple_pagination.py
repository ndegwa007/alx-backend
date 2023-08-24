#!/usr/bin/env python3
"""module implements a simple pagination class"""
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page of the dataset"""
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int

        start, stop = index_range(page, page_size)
        return self.dataset()[start:stop]
