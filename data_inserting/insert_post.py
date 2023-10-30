import pymongo

import random
connection = pymongo.MongoClient("localhost", 27017)
database = connection["ncc_dip2"]
collection = database["posts"]

if __name__ == '__main__':
    sms_id = 0
    for i in range(3):
        # user_id = random.randint(10, 10000)
        post_id = random.randint(10, 10000)
        post = "wind1 post "
        owner: str = "win1@gmail.com"
        

        # info:str = "User data is Win"+str(i)+"id : "+str(user_id)

        data_form = {"_id": post_id,
                    "post": post,
                    "owner": owner}

        ids = collection.insert_one(data_form)
        print("inserted id :", ids.inserted_id)