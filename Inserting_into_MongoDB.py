import pymongo

def mongoDbCreation():
    connection = pymongo.MongoClient('mongodb://localhost:27017/')
    my_db = connection['Youtube_data_warehouse_1']
    collection_1 = my_db.channel_data
    return collection_1


mongo = mongoDbCreation()

def channel_file(channel):
    with open('channels.txt', 'a+') as f:
        f.seek(0)
        channel_list = [i.strip() for i in f.readlines()]
        print(channel_list)
        if channel not in channel_list:
            f.seek(0, 2)
            f.write(f'{channel}\n')


def Mongodb(details):
    channel_name = details['Channel_Name']['Channel_Name']
    channel_file(channel_name)

    id = details['Channel_Name']['Channel_Id']

    if mongo.find_one({'Channel_Name.Channel_Id': id}, {'Channel_Name': 1}):
        mongo.delete_one({'Channel_Name.Channel_Id': id})
        mongo.insert_one(details)
        var = f"{id} is already in database so it is replaced, but please again migrate to MySQL"
        return var

    else:
        mongo.insert_one(details)
        var = f"{id} is inserted into MongoDB"
    return var
