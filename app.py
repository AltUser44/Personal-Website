from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import os


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r. status_code != 200:
        return None
    return r.json()

# use local css file
def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("OneDrive/style/style.css")



# loading assets
lottie_coding = "https://lottie.host/63e9a5f0-f3fc-4ce3-bf56-607c9b5bf15e/9U9fB8vOyy.json"

# Define path to the images
one_drive_images_path = os.path.join('C:\\', 'Users', 'kpnke', 'OneDrive', 'images')
img_earth_path = os.path.join(one_drive_images_path, 'earth.png')  # Define the full path to the earth image
img_allie_path = os.path.join(one_drive_images_path, 'allie.png')  # Define the full path to the allie image

# Load the images
img_earth = Image.open(img_earth_path)
img_allie = Image.open(img_allie_path)


# header section
with st.container():
    st.subheader("Hi, I am Kester :wave:")  # Corrected method name to 'subheader' and added a space before the emoji code
    st.title("A Data Analyst from the United States")
    st.write("I am passionate about finding intuitive ways to use coding to create and design tools that help enhance user experience.")
    st.markdown("[Learn More](https://pythonandvba.com)")  # Corrected markdown for hyperlink

# What I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")  # Capitalized the title for consistency
        st.write("##")
        st.write(
            """ 
            I am a third-year college student on my path to becoming a data scientist:
            - Using Python, Html, Javascript and Java to automate repetitive tasks, demonstrating how these 
              languages can streamline workflows and increase efficiency in any work environment.
            - Utilizing my knowledge in data analysis and data science to build meaningful and impactful projects, 
              showcasing my ability to extract insights and make data-driven decisions.
            - Overcoming challenges by using different innovative tools to develop projects, 
              demonstrating my problem-solving skills and ability to adapt to various tools for optimal solutions."
              
            Check out my other projects below 👇 
            """  # Added a period at the end for proper punctuation
        )
    st.markdown("[Other Projects](https://github.com/AltUser44?tab=repositories)")  # Corrected markdown for hyperlink and the URL scheme
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")


# projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
     st.image(img_earth)
    with text_column:
        st.subheader("3D web visualization of a spinnin sphere encircled by 5 individually rotating rings")
        st.write(
            """
            - Using Three.Js this programs visually displays a 3D sphere.
            - Users can click and drag to control the camera's view, exploring the sphere and rings.
            
            In this link below, you can explore the project furthermore.
            """
        )
        st.markdown("Project (https://github.com/AltUser44/3dSphere)")
with st.container():
    image_column, text_column, = st.columns((1, 2))
    with image_column:
        st.image(img_allie)
    with text_column:
        st.subheader("A.L.I.E. (Artificial Listening Interactive Entity)")
        st.write(
            """
            - Uses graphical user interface (GUI) to facilitate user interaction.
            - Users can easily access information on various topics.
            
            In this link below, you can explore the project furthermore.
            """
        )
        st.markdown("Project (https://github.com/AltUser44/A.L.I.E)")



# Add contact info
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

# Documentation: email address
contact_form = """
<form action="https://formsubmit.co/codingisfun.kpnkese@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>

"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()