#!/usr/bin/env python3
""" NoSQL """

def insert_school(mongo_collection, **kwargs):
    """ insert a document in a collection based on kwargs """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
