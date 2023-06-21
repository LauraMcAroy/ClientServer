from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.       
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'password'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32384
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert =self.database.animals.insert_one(data)  # data should be dictionary  
            return insert
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, search):
        if search is not None:
            if search:
                searchResult = self.database.animals.find(search)
                return searchResult
        else:
            raise Exception("Search Parameter Empty.")
            
# Method to implement U in CRUD

    def update(self, searchData, updateData):
        if searchData is not None:
            result = self.database.animals.update_many(searchData, {"$set" : updateData})
        else:
            return "{}"
        
        return result
                
#Method to implement D in CRUD
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            return "{}"
        return result
                