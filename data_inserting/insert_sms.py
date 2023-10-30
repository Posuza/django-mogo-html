import pymongo

import random
connection = pymongo.MongoClient("localhost", 27017)
database = connection["ncc_dip2"]
collection = database["sms"]

if __name__ == '__main__':
    
    for i in range(1):
        # user_id = random.randint(10, 10000)
        sms_id = 3
        owner = "win1@gmail.com"
        message = "yet win1"

        sender: str = "win2@gmail.com"
        reciver: str = "win1@gmail.com"

        # sender: str = "win1@gmail.com"
        # reciver: str = "win2@gmail.com"
        # email: str = "win"+str(i)+"@gmail.com"
        # password: str = "12345"
        # phone: int = 94537
        # point: int = 100

        # info:str = "User data is Win"+str(i)+"id : "+str(user_id)

        data_form = {"_id": sms_id,
                    "woner": owner,
                    "message": message,
                    "sender": sender,
                    "reciver":reciver}

        ids = collection.insert_one(data_form)
        print("inserted id :", ids.inserted_id)