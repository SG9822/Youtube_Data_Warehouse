import googleapiclient.discovery
from googleapiclient.errors import HttpError

api_key = 'Use Your Api'

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "api_key.json"

developerKey = api_key
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=api_key)


def channel_details(user_input):
    details = {}
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=user_input
    )
    response_1 = request.execute()
    desc_c = response_1['items'][0]['snippet']['description']
    if desc_c == "" or desc_c is None:
        d = 'No Description'
    else:
        d = desc_c
    title = response_1['items'][0]['snippet']['title']
    details.update(
        dict(Channel_Name=title.strip(),
             Channel_Id=response_1['items'][0]['id'],
             Subscription_Count=response_1['items'][0]['statistics']['subscriberCount'],
             Video_Count=response_1['items'][0]['statistics']['videoCount'],
             Channel_Views=response_1['items'][0]['statistics']['viewCount'],
             Channel_Description=d,
             Playlist_Id=response_1['items'][0]['contentDetails']['relatedPlaylists']['uploads'])
    )

    return details


def video_id(channel_id):
    next_Page_Token = None
    video_ids = []
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=channel_id
    )
    response_1 = request.execute()

    while True:
        request_v = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=response_1['items'][0]['contentDetails']['relatedPlaylists']['uploads'],  # playlist_id
            maxResults=50,
            pageToken=next_Page_Token

        )
        response_2 = request_v.execute()
        for item in response_2.get('items', ''):
            video_ids.append(item['contentDetails']['videoId'])
        next_Page_Token = response_2.get('nextPageToken')
        if not next_Page_Token:
            break
    return video_ids


def video_dictionary(video_ids):
    v = 0
    video = {}
    for ids in video_ids:

        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=ids
        )
        response_3 = request.execute()
        v += 1
        try:
            tag = ', '.join(response_3['items'][0]['snippet']['tags'][0:2])
        except:
            tag = 'No Tag'
        try:
            count = response_3['items'][0]['statistics']['commentCount']
        except:
            count = 0
        try:
            like = response_3['items'][0]['statistics']['likeCount']
        except:
            like = 0
        try:
            fav = response_3['items'][0]['statistics']['favoriteCount']
        except:
            fav = 0
        if response_3['items'][0]['snippet']['description'] == '':
            desc = 'No Description'
        else:
            desc = response_3['items'][0]['snippet']['description']

        video[f"Video_Id_{v}"] = {
            'Video_Id': response_3['items'][0]['id'],
            'Channel_Id': response_3['items'][0]['snippet']['channelId'],
            'Video_Name': response_3['items'][0]['snippet']['title'],
            'Video_Description': desc,
            'Published_Date': response_3['items'][0]['snippet']['publishedAt'].replace('T', ' ').replace('Z', ''),
            'Tags': tag,
            'View_Count': response_3['items'][0]['statistics']['viewCount'],
            'Like_Count': like,
            'Favourite_Count': fav,
            'Comment_Count': count,
            'Duration': response_3['items'][0]['contentDetails']['duration'].replace("PT", "").replace("H",
                                                                                                       ":").replace
            ("M", ":").replace("S", ""),
            'Thumbnail': response_3['items'][0]['snippet']['thumbnails']['default']['url'],
            'Caption_Status': response_3['items'][0]['contentDetails']['caption'].replace('true',
                                                                                          'Available').replace(
                'false', 'Not Available')
        }
    return video


def comments(video_ids):
    comments = {}
    c = 0
    for id in video_ids:
        try:
            request = youtube.commentThreads().list(
                part="snippet,replies",
                videoId=id,
                maxResults=20,
            )
            response_4 = request.execute()
            for item in response_4.get('items', ''):
                c += 1
                comments[f'Comment_Id_{c}'] = {
                    'Channel_Id': item['snippet']['channelId'],
                    'Video_Id': item['snippet']['videoId'],
                    'Comment_Id': item['id'],
                    'Comment_Text': item['snippet']['topLevelComment']['snippet']['textOriginal'],
                    'Comment_Author': item['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                    'Comment_PublishedAt': item['snippet']['topLevelComment']['snippet']['publishedAt'].replace
                    ('T', ' ').replace('Z', '')
                }
        except HttpError:
            continue
    return comments


over_all = []


def youtube_harvest(user_input):
    for id in user_input:
        single = {}
        single.update(Channel_Name=channel_details(id))
        vi = video_id(id)
        single.update(video=video_dictionary(vi))
        single.update(comments=comments(vi))
        over_all.append(single)
        print(f'Data from {id} extracted')
        # print(over_all)
    return over_all
