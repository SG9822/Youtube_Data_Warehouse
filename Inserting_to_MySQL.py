import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote
import pymysql
import mysql.connector

# to mysql

user = 'root'
password = quote('MySQL@123')
host = '127.0.0.1'
port = 3306
database = 'Youtube_Data'

engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')


def df_mysql(channels, comments, videos):
    try:
        myconnection = pymysql.connect(host='127.0.0.1', user='root', passwd='MySQL@123')
        cur = myconnection.cursor()
        cur.execute('create database Youtube_Data')

        myconnection = pymysql.connect(host='127.0.0.1', user='root', passwd='MySQL@123', database='Youtube_Data')
        cursor = myconnection.cursor()
        cursor.execute('use Youtube_Data')
    except:
        channel = pd.DataFrame(channels).astype(
            {'Channel_Name': 'object', 'Channel_Id': 'object', 'Subscription_Count': 'int64', 'Video_Count': 'int64',
             'Channel_Views': 'int64', 'Channel_Description': 'object', 'Playlist_Id': 'object'})
        comment = pd.DataFrame(comments)
        video = pd.DataFrame(videos).astype(
            {'Published_Date': 'datetime64[ns]', 'View_Count': 'int64', 'Like_Count': 'int64', 'Favourite_Count': 'int64',
             'Comment_Count': 'int64'})
        # Save DataFrame to MySQL
        checking = pd.read_sql_query("select channel_id from channel", engine)
        # print(channels[0])
        id_c = channels[0]['Channel_Id']
        if id_c in checking["channel_id"].tolist():
            mydb = mysql.connector.connect(user = 'root',
            password = 'MySQL@123',
            host = '127.0.0.1',
            port = 3306,
            database = 'Youtube_Data')

            mycursor = mydb.cursor()

            mycursor.execute("SET SQL_SAFE_UPDATES = 0")
            mydb.commit()
            mycursor.execute(f"delete from channel where Channel_Id = '{id_c}'")
            mydb.commit()
            mycursor.execute(f"DELETE FROM comments WHERE channel_id = '{id_c}'")
            mydb.commit()
            mycursor.execute(f"DELETE FROM video WHERE channel_id = '{id_c}'")
            mydb.commit()
            mycursor.execute("SET SQL_SAFE_UPDATES = 1")
            mydb.commit()


        channel.to_sql('channel', con=engine, if_exists='append', index=False)
        comment.to_sql('comments', con=engine, if_exists='append', index=False)
        video.to_sql('video', con=engine, if_exists='append', index=False)


def data_collection(collection, channel):
    channels = []
    channels.append(collection.find_one({'Channel_Name.Channel_Name': channel}, {'Channel_Name': 1, '_id': 0})['Channel_Name'])
    comments = []
    c = collection.find_one({'Channel_Name.Channel_Name': channel}, {'comments': 1, '_id': 0})
    for i in c:
        for j in c[i]:
            comments.append(c[i][j])
    videos = []
    v = collection.find_one({'Channel_Name.Channel_Name': channel}, {'video': 1, '_id': 0})
    for i in v:
        for j in v[i]:
            videos.append(v[i][j])

    df_mysql(channels, comments, videos)
    return f"{channel} Migrated to MySQL"
