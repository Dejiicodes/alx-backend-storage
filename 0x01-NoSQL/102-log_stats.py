 #!/usr/bin/env python3
"""
12-log_stats.py - Log statistics module with additional feature to display top 10 IPs
"""
from pymongo import MongoClient

def log_stats(mongo_collection):
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    # Total number of logs
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    # Number of each method type
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Number of logs with status check
    status_check = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    # Top 10 most present IPs
    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = mongo_collection.aggregate(pipeline)
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    log_stats(nginx_collection)
