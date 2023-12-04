import pandas as pd
from Inserting_to_MySQL import engine
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Query Details",
    page_icon="📊",
)

st.sidebar.success("Select a page above")

query_dict = {
    'What are the names of all the videos and their corresponding channels?': [
        'select video_name, Channel_Name from channel c left join video v on c.Channel_Id = v.Channel_Id'],
    'Which channels have the most number of videos, and how many videos do they have?': [
        'select Channel_Name, Video_Count from channel order by Video_Count desc limit 1', 'Channel_Name',
        'Video_Count'],
    'What are the top 10 most viewed videos and their respective channels?': [
        'select Video_Name, Channel_Name, View_Count from channel c left join video v  on c.Channel_Id = v.Channel_Id order by View_Count desc limit 10',
        'Video_Name', 'View_Count'],
    'How many comments were made on each video, and what are their corresponding video names?': [
        'select Video_Name, Comment_Count from video', 'Video_Name', 'Comment_Count'],
    'Which videos have the highest number of likes, and what are their corresponding channel names?': [
        'select Channel_Name, Video_Name, Like_Count from channel c join video v on c.Channel_Id = v.Channel_Id order by Like_Count desc',
        'Video_Name', 'Like_Count'],
    'What is the total number of likes for each video, and what are their corresponding video names?': [
        'select Video_Name, Like_Count from video order by Like_Count desc', 'Video_Name', 'Like_Count'],
    'What is the total number of views for each channel, and what are their corresponding channel names?': [
        'select Channel_Name, Channel_Views from channel', 'Channel_Name', 'Channel_Views'],
    'What is the average duration of all videos in each channel, and what are their corresponding channel names?': [
        'select Channel_Name, round(avg(Duration), 3) Average_Duration  from channel c left join video v on c.Channel_Id = v.Channel_Id group by Channel_Name',
        'Channel_Name', 'Average_Duration'],
    'What are the names of all the channels that have published videos in the year 2022?': [
        'select Distinct Channel_Name, year(Published_Date) year_published from channel c join video v on c.Channel_Id = v.Channel_Id where year(Published_Date) = 2022'],
    'Which videos have the highest number of comments, and what are their corresponding channel names ?': [
        'select Channel_Name, Video_Name, Comment_Count from channel c join video v on c.Channel_Id = v.Channel_Id order by Comment_Count desc limit 5',
        'Video_Name', 'Comment_Count']
}


def query(query_dict, s):
    if len(query_dict[s]) > 1:
        table = pd.read_sql_query(query_dict[s][0], engine)
        table = pd.DataFrame(table)
        st.dataframe(table)
        st.header("Chart")
        st.write(px.bar(table, x=query_dict[s][1], y=query_dict[s][2]))

    else:
        table = pd.read_sql_query(query_dict[s][0], engine)
        table = pd.DataFrame(table)
        if s == 'What are the names of all the channels that have published videos in the year 2022?':
            table["year_published"] = pd.to_datetime(table["year_published"], format="%Y").dt.strftime("%Y")
        st.write(table)
        st.caption("Sorry Chart can't be formed")



st.image("The image you like", width=150)
st.title("Query Details")
st.header("Want to know some Stats and Ranks?")

select = st.selectbox("Select query", list(query_dict.keys()), index=None)
q = st.button("Query")
if q:
    # print(query(query_dict, select))
    try:
        print(query(query_dict, select))

    except:
        st.warning("Please Provide the Query")
