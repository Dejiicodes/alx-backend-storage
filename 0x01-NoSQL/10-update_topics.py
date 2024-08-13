#!/usr/bin/env python3
""" Module for using PyMongo """


def update_topics(mongo_collection, name, topics):
    """ Changes field in document based on name field """
    name_field = {"name": name}
    value_field = {"$set": {"topics": topics}}
    mongo_collection.update_many(name_field, value_field)
