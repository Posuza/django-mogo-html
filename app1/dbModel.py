import pymongo


class mongoDb:
    def __init__(self):
        pass
    
    def ___db_connection(self,collection_name):
        connection = pymongo.MongoClient("locahost",27017)
        database = connection["ncc_dip2"]
        collection = database[collection_name]
        return collection
    
    def users(self):
        data = self.___db_connection("user_info")
        return data

if __name__ == "__main__":
    user = mongoDb.users
    id = 0
    print(user)
    for i in user.find({},{"_id":0,"email":1,"password":1,"phone":1,"info":1}):
            print(i)