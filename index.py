from ctypes import sizeof
from turtle import width
import streamlit as st 
import time 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

#st.title("Car Accident Detection")

# st.header("Data")
# st.text("Hi Khalid")
# st.subheader("Dodo")

# st.markdown(""" ### h1 tag 
# # h2 tag
# # h3 tag
# :moon:<br>
# :sunglasses:
# """,True)

# st.latex(r'''a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#      \sum_{k=0}^{n-1} ar^k =
#      a \left(\frac{1-r^{n}}{1-r}\right)''')
# s='khalid'
# st.write(s)

# dic = {
#      "Name":["khalid","amal"],
#      "Age": [22 , 25],
#      "City": ["California","amsterdam"]
#      }
# st.table(dic)
# st.write(dic)
# st.json(dic)

# @st.cache
# def real_time():
#      time.sleep(5)
#      return time.time()

# if st.checkbox("1"):
#      st.write(real_time())

# if st.checkbox("Hi choose me",value = False):
#      st.write("fuck you")

# data = pd.DataFrame(
#      np.random.randn(100,3),
#      columns=('a','b','c')
# )
# st.line_chart(data)
# st.area_chart(data)
# st.bar_chart(data)

# plt.scatter(data['a'],data['b'])
# plt.title("scatter")
# st.pyplot()

# chart = alt.Chart(data).mark_circle().encode(
#     x = 'a',y='b',tooltip =['a','b'])
# st.altair_chart(chart)

# chart_2 = alt.Chart(data).mark_circle().encode(
#     x = 'a',y='b')

# st.altair_chart(chart_2,use_container_width = True)

# st.graphviz_chart("""
# digraph{
# watch -> like
# like -> share
# share -> subscripe
# share -> watch     
# }
# """)

# city = pd.DataFrame({
#     'awesome cities' : ['Chicago', 'Minneapolis', 'Louisville', 'Topeka'],
#     'lat' : [41.868171, 44.979840,  38.257972, 39.030575],
#     'lon' : [-87.667458, -93.272474, -85.765187,  -95.702548]
# })
# st.map(city)

#st.image("Data//WhatsApp Image 2022-12-19 at 4.40.01 PM.jpeg",caption='Habiba', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
# st.video("https://www.youtube.com/watch?v=jq0lKFb-P8k&list=PLuU3eVwK0I9PT48ZBYAHdKPFazhXg76h5&index=4")

# while st.button("click here"):
#      st.write("عاوز اي يا عرص ")
#      break

# if st.button('Say hello'):
#     st.write('Why hello there')
# else:
#     st.write('Goodbye')

# name = st.text_input("Enter you name")
# st.write(name)

#______________________________

# File = st.file_uploader("Uplode your video to detect")
# st.image(File)

#_________________________________

# Set page title and layout
st.set_page_config(page_title="My web page", layout="wide")
st.title("Car Accident Detection")

rad =st.sidebar.radio("Navigation",["Home","About Us"])

if rad == "Home":
     # Define columns for the layout
     col1, col2 = st.columns(2)

     # Add content to the first column
     with col1:
          st.image("WhatsApp Image 2023-06-26 at 17.07.55.jpg")
          st.subheader("Welcome to my web page!")
          st.write("This is some text that describes what my web page is about.")

     # Add content to the second column
     with col2:
          st.subheader("Sign up for our news letter")
          st.write("Enter your email address below to receive updates about our website.")
          email = st.text_input("Email address")
          if st.button("Sign up"):
               st.write(f"Thank you for signing up with {email}!")
               File = st.file_uploader("Uplode your video to detect")
               st.image(File)

if rad == "About Us":
     st.write("The Problem is to build a reliable and accurate traffic accident detection system using state-of-the-art object detection models. The system should be able to analyze live video feeds from CCTV cameras and determine whether an accident has occurred or not, based on the presence of specific visual cues such as collision, and vehicle damage. The system's performance will be evaluated based on accuracy, precision, recall, and computational efficiency")

