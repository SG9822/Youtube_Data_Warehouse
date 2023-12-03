from googleapiclient.errors import HttpError

from Data_Extraction import youtube_harvest, over_all
from Inserting_into_MongoDB import Mongodb, mongo
from Inserting_to_MySQL import data_collection
import streamlit as st

st.set_page_config(
    page_title="Youtube Details",
    page_icon="▶️",
)


st.sidebar.success("Select a page above")

st.image("youtube-logo-download.png", width=100)

st.title("Welcome to Page to Know YouTube Beyond Videos")
st.markdown("### Want to know about Channels")
user_input = st.text_input("Enter Channel Ids", placeholder='If more than one Id please separate with comma & no gap')

click_1 = st.button("Extract Details")

try:
    try:
        if click_1:

            if len(user_input) == 0 or user_input is None:
                print(None)
                st.warning("Please Enter at least 1 Id")
            else:
                user_input = user_input.split(",")
                youtube = youtube_harvest(user_input)
                for i in youtube:
                    st.success(f"{i['Channel_Name']['Channel_Id']} extracted")
    except HttpError as e:
        if e.resp.status == 403 and "quotaExceeded" in str(e):
            st.exception(HttpError("Quota exceeded. Implement retry or back-off logic."))
        else:
            # Handle other errors
            print(f"Error: {e}")
except:
    st.warning("Can You Please Try again")


click_2 = st.button("Insert into MongoDB")
if click_2:
    try:
        if len(over_all) == 0 or over_all is None:
            st.warning("Please Enter the Channel Id and Extract Data")
        else:
            for j in over_all:
                st.success(Mongodb(j))
            over_all.clear()
    except:
        st.warning("Please Try Again")
        print(len(over_all))


def files():
    with open('channels.txt', 'r') as f:
        f.seek(0)
        ch_arr = [i.strip() for i in f]
    return ch_arr


files = files()

st.divider()
st.markdown("### Migration to MySQL")
channel = st.selectbox("Select a channel to Migrate to SQL", files, index=None)
mig = st.button("Migrate")

if mig:

    try:
        st.success(data_collection(mongo, channel))
        st.balloons()
        files.remove(channel)
        with open('channels.txt', 'w') as f:
            for ch in files:
                f.write(f"{ch}\n")
    except:
        st.warning("Please Try again")


