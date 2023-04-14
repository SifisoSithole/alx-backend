#!/usr/bin/env python3
"""
This module contains the `index_range` function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function calculates the start index and end index based on
    the page and page size

    args:
        page (int): Current page
        page_size (int): Length of the page

    return
        (tuple): a tuple of size two containing a start index and
        an end index corresponding to the range of indexes to return in a
        list for those particular pagination parameters
    """
    if type(page) is not int or page < 1:
        raise TypeError('The first argument must be an integer > 0')

    if type(page_size) is not int or page < 0:
        raise TypeError('The first argument must be an integer >= 0')

    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
