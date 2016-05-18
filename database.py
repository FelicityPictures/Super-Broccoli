from pymongo import MongoClient

connection = MongoClient()
db = connection["broccoli"]

"""
COLLECTIONS
courses: code, name, year, description 
dependencies: code, master (req), slave
"""



if __name__ == "__main__":
    
