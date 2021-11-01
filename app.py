# Basic & Fundamentals

# Core Pkgs
from pandas.io.pytables import Selection
import streamlit as st

# Load EDA Pkgs
import pandas as pd

# # Display Data
df = pd.read_csv("iris.csv")

# # Methos 1
st.dataframe(df)

# # Adding A color style from pandas
st.dataframe(df.style.highlight_max(axis=0))

# # Method 2
st.table(df)

# # Method 3: Using superfxn st.write
st.write(df.head())

# Display Json
st.json({'data':'name'})

# Display Code
# mycode = """
# def sayhello():
#     print("Hello Streamlit)
# end
# """
# st.code(mycode, language='ruby')

# Working with Widgets
# Buttons/Radio/Checkbos/Select

# # Working with Buttons
# name = "Binita"


# if st.button("Submit"):
#     st.write("Name: {}".format(name.upper()))

# if st.button("Submit", key='new02'):
#     st.write("First Name: {}".format(name.lower()))

# # Working with RadioButtons
# status = st.radio("What is your status", ("Active", "Inactive"))
# if status == 'Active':
#     st.success("You are active")
# elif status == "Inactive":
#     st.warning("Inactive")

# # Working with Checkbox
# if st.checkbox("Show/Hide"):
#     st.text("Showing something")

# # Working with Beta Expander
# # if st.beta_expander("Python"):
# #     st.success("Hello Python")

# with st.beta_expander("Binita"):
#     st.text("Hello Binita")


# Select/Multiple select
# my_lang = ['Python', 'Excel', 'Java']

# choice = st.selectbox("Language", my_lang)
# st.write("You selected {}".format(choice))

# # Multiple Selection

# spoken_lang = ("English", "Nepali", "Hindi")
# my_spoken_lang = st.multiselect("spoken lang", spoken_lang, default="English")

# # Slider
# # For Numbers (Int/Float/Date)
# age = st.slider("Age", 1, 100, 5)

# # Select Slider
# # Any datatype
# color = st.select_slider('Choose Color', options=[
#                          'yellow', 'red', 'blue', 'black', 'white'], value=('yellow', 'red'))

# Work with Media File(videos/images/audio)
# Display Images
# from PIL import Image
# img = Image.open('data/image_03.jpg')
# st.image(img, use_column_width=True)

# From URL
# st.image("https://cdn.searchenginejournal.com/wp-content/uploads/2019/12/when-to-use-data-science-in-seo-5def8e5b1c22c-1520x800.webp")

# # Display Videos
# video_file = open("data/afafafa.mp4", 'rb').read()
# st.video(video_file, start_time=3)

# Display Audio files
# audio_file = open('.mp3', 'rb')
# st.audio(audio_file.read())

