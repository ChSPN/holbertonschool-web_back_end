#!/usr/bin/env python3
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    :param mongo_collection: pymongo collection object
    :return: list of documents or an empty list if no documnt in the collection
    """
    return list(mongo_collection.find())


# Exemple d'utilisation
if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
