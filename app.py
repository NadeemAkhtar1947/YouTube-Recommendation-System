import streamlit as st
import pickle
import pandas as pd


# Add a Markdown component to display the greeting
st.markdown("### Hi, My name is Nadeem and this app is developed by me")

links_row = "<a href='https://www.linkedin.com/in/nadeem-akhtar-/' target='_blank'>" \
            "<img src='https://img.icons8.com/color/48/000000/linkedin.png' width='30'></a>" \
            " | " \
            "<a href='https://github.com/NadeemAkhtar1947' target='_blank'>" \
            "<img src='https://img.icons8.com/color/48/000000/github.png' width='30'></a>" \
            " | " \
            "<a href='https://www.kaggle.com/mdnadeemakhtar/code' target='_blank'>" \
            "<img src='https://www.kaggle.com/static/images/site-logo.png' width='30'></a>" \
            " | " \
            "<a href='https://tyrex.netlify.app/' target='_blank'>" \
            "<img src='https://img.icons8.com/color/48/000000/globe--v1.png' width='30'></a>"

# Display the links row using Markdown
st.markdown(links_row, unsafe_allow_html=True)



# Function to increment view count
def increment_views():
    # Read current view count from file
    try:
        with open("view_count.txt", "r") as file:
            views = int(file.read())
    except FileNotFoundError:
        # If file doesn't exist, initialize view count to 0
        views = 0

    # Increment view count
    views += 1

    # Write updated view count to file
    with open("view_count.txt", "w") as file:
        file.write(str(views))

    return views

# Increment view count only once per user visit
if not st.session_state.get("view_counted", False):
    total_views = increment_views()
    st.session_state.view_counted = True
else:
    total_views = int(open("view_count.txt", "r").read())

# Display total views
st.write("Total Views:", total_views)

# Your Streamlit app code goes here...



def recommend_youtube(youtube_name):
    yt_index = youtube[youtube['Youtuber'] == youtube_name].index[0]
    distances = similarity[yt_index]
    yt_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:10]

    recommended_yt = []
    for i in yt_list:
        Youtuber = youtube.iloc[i[0]].Youtuber
        recommended_yt.append(youtube.iloc[i[0]].Youtuber)
    return recommended_yt

yts_dict = pickle.load(open('yt_dict.pkl','rb'))
youtube = pd.DataFrame(yts_dict)

similarity = pickle.load(open('similarity_matrix.pkl','rb'))

st.title("YouTube Recommendation System")

selected_yt_name = st.selectbox(
'Enter a YouTube channel',
youtube['Youtuber'].values)


if st.button('Get Recommend'):
    names = recommend_youtube(selected_yt_name)
    col1 , col2 , col3 = st.columns(3)
    with col1:
        st.success(names[0])
    with col2:
        st.success(names[1])
    with col3:
        st.success(names[2])
    with col1:
        st.success(names[3])
    with col2:
        st.success(names[4])
    with col3:
        st.success(names[5])
    with col1:
        st.success(names[6])
    with col2:
        st.success(names[7])
    with col3:
        st.success(names[8])

# Add custom text at the bottom using Markdown
st.markdown("---")
st.markdown("Copyright © Nadeem Akhtar. All Rights Reserved")



