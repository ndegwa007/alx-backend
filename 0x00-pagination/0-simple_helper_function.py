#!/usr/bin/env python3
"""simple pagination helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """return start and end index of a page"""
    p = 1
    x = 0
    ps = page_size
    t = tuple()
    if page == 1:
        t = (x, ps)
    while p < page:
        x = page_size
        page_size += ps
        listy = [x, page_size]
        t = tuple(listy)
        p += 1
    return t
