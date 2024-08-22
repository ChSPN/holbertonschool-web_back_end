#!/usr/bin/env python3
""" 9-main """

def insert_school(mongo_collection, **kwargs):
    """ insert a document in a collection based on kwargs """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
