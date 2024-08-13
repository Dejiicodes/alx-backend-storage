#!/usr/bin/env python3
""" Module for using PyMongo """


def list_all(mongo_collection):
    """ Lists all documents in a collection """

    doc_list = []

    docs = mongo_collection.find()
    for doc in docs:
        doc_list.append(doc)

    return doc_list

    # shorter alternatives:
    # return [item for item in mongo_collection.find()]
    # return list(mongo_collection.find())
