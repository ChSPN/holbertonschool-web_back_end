#!/usr/bin/env python3
"""NoSQL"""
from typing import List


def list_all(mongo_collection) -> List:
    """
    Lists all documents in a collection.

    :param mongo_collection: pymongo collection object
    :return: list of documents or an empty list if no documnt in the collection
    """
    return list(mongo_collection.find())
