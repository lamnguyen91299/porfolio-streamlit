import streamlit as st 
import streamlit.components.v1 as components
from PIL import Image
from streamlit_timeline import timeline
import pandas as pd
import webbrowser
from bokeh.models.widgets import Div



st.set_page_config(page_title='Lam Nguyen Porfolio', page_icon='🧊', layout="wide",initial_sidebar_state="expanded")

with st.sidebar:
    image = Image.open("static/forweb.jpg")
    # st.image(image, width = 200)
    st.title("Nguyen Hoang Lam ")
    # components.html('<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="harshitwadhwani" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/harshitwadhwani?trk=profile-badge"></a></div>', height = 310 )
    if st.button("Github"):
      js = "window.open('https://github.com/lamnguyen91299')"  # New tab or window
      html = '<img src onerror="{}">'.format(js)
      div = Div(text=html)
      st.bokeh_chart(div)  
    with open("static/CV_DA_lamnguyen.pdf", "rb") as file:
        btn = st.download_button(
                label="Download Resume",
                data=file,
                file_name="CV_DA_lamnguyen.pdf"
            )
        
st.title ("Introduction")
st.write("Data Analyst with expertise in Python, and analytical techniques, passionate about extracting insights from data to drive informed decision-making.")

st.title ("Skills")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Technical skill**")
    st.button('Python | PySpark, Streamlit')
    st.button('SQL| Bigquery, MySQL, Postges, MSSQL')
    st.button('Technical writing (SRS, BRD docs)')
    st.button('Statistical analysis and modeling')

    
with col2:
    st.write("**Soft Skill**")
    st.button("Scrum, Agile")
    st.button('Backlog management')
    st.button('Project management')
    st.button('Data management')
with col3:
    st.write('')

st.title('Projects')
st.subheader('Youtube channel auto report')
st.write('Utilize Python and MML to develop an app for automatically analyzing data from a YouTube channel.')
if st.button('Open Project', key = 54):
  js = "window.open('https://youtube-auto-report.streamlit.app')"  # New tab or window
  html = '<img src onerror="{}">'.format(js)
  div = Div(text=html)
  st.bokeh_chart(div)  
  
  
st.subheader('Application using gemini Api')
st.write('An application utilizes MML Gemini Pro to generate a marketing campaign based on selected inputs, creating descriptions based on the input images.')
if st.button('Show Project', key =55):
  js = "window.open('https://gen-ai-app.streamlit.app')"  # New tab or window
  html = '<img src onerror="{}">'.format(js)
  div = Div(text=html)
  st.bokeh_chart(div)  
  

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 