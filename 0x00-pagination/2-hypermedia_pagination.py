#!/usr/bin/env python3
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page according to the page number and page size

        args:
            page (int): Current page
            page_size (int): Length of the page

        return:
            names_list (list): Returns the appropriate page of the dataset
        """
        list_range = index_range(page, page_size)
        names_list = self.dataset()
        return names_list[list_range[0]:list_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
         args:
            page (int): Current page
            page_size (int): Length of the page

        return:
            info_dict (dict):  returns a dictionary containing key-value pairs
        """
        info_dict = {}
        names_list = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        info_dict['page_size'] = len(names_list)
        info_dict['page'] = page
        info_dict['data'] = names_list
        if page + 1 > total_pages:
            info_dict['next_page'] = None
        else:
            info_dict['next_page'] = page + 1
        if page == 1:
            info_dict['prev_page'] = None
        else:
            info_dict['prev_page'] = page - 1
        info_dict['total_pages'] = total_pages
        return info_dict
