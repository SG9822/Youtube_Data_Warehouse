import streamlit as st
import pandas as pd
from Inserting_to_MySQL import engine
import plotly.express as px

st.set_page_config(
    page_title="Table Details",
    page_icon="📚",
)

st.sidebar.success("Select a page above")

st.image("TablesSQL.png", width=100)


st.title("Want to see Tables stored in our Database that you are working with?")
table = st.selectbox("Select the table you want to explore", ["Channels", "Videos", "Comments"], index=None)

query = ""
if table:
    try:
        if table == 'Channels':
            query = "select * from channel"
        elif table == 'Videos':
            query = "select * from video"
        elif table == 'Comments':
            query = "select * from comments"

        sql = pd.read_sql_query(query, engine)
        st.write(pd.DataFrame(sql))

    except:
        st.warning("No Tables in the Database")

st.header("Top 10 Stars")
st.subheader("Select both radio and select option for Top 10 stars")

top_radio = st.radio("Select the table you want to explore", ["Channel", "Video"], index=None)

list = []
if top_radio == "Channel":
    list = ["Subscription_Count", "Video_Count", "Channel_Views"]
else:
    list = ["View_Count", "Like_Count", "Comment_Count"]

top_select = st.selectbox("Select Sub query", list, index=None)

if top_radio and top_select:
    quotes = f"select {top_radio}_name, {top_select} from {top_radio} order by {top_select} desc limit 10"
    sql_table = pd.read_sql_query(quotes, engine)
    st.write(pd.DataFrame(sql_table))
    st.write(px.bar(sql_table, x=f"{top_radio}_name", y=top_select))
