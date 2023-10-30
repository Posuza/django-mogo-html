import pymongo

import random
connection = pymongo.MongoClient("localhost", 27017)
database = connection["ncc_dip2"]
collection = database["comments"]

if __name__ == '__main__':

    for i in range(1):
        id = random.randint(10, 10000)
        post_id =2061
        comment = "nice win1 from win2,thank all"
        com_email: str = "win1@gmail.com"
        

        # info:str = "User data is Win"+str(i)+"id : "+str(user_id)

        data_form = {"_id": id,
                    "post_id": post_id,
                    "comment": comment,
                    "com_email": com_email}

        ids = collection.insert_one(data_form)
        print("inserted id :", ids.inserted_id)