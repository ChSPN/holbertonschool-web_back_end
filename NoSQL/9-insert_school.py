#!/usr/bin/env python3
"""
This module provides a function to insert a new document into a MongoDB collection.
"""

from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs) -> str:
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        **kwargs: Arbitrary keyword arguments representing the document fields.

    Returns:
        str: The ID of the newly created document.
    """
    new_document = mongo_collection.insert_one(kwargs)
    return str(new_document.inserted_id)


if __name__ == "__main__":
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school

    # Insertion d'une nouvelle école pour tester
    new_school_id = insert_school(school_collection, name="UCSF", address="505 P
