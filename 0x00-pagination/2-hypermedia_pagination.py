#!/usr/bin/env python3
"""module implements a simple pagination class"""
import csv
import math
from typing import List


class Server:
    """
    server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.res = {}

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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns dictionary with query info"""
        attr = ['page_size',
                'page',
                'data',
                'next_page',
                'prev_page',
                'total_pages']
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page, prev_page = None, None
        if self.get_page(page, page_size) == []:
            page_size = 0
        if page > 1:
            prev_page = page - 1
        if page < total_pages:
            next_page = page + 1
        values = [
                page_size,
                page,
                self.get_page(page, page_size),
                next_page,
                prev_page,
                total_pages]
        for i, j in zip(attr, values):
            self.res[i] = j
        return self.res
