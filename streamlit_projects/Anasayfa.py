from dotenv import load_dotenv
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from streamlit.source_util import (
    page_icon_and_name,
    calc_md5,
    get_pages,
    _on_pages_changed,
)

# def hide_sidebar():
#     st.markdown("""
# <style>
#         section[data-testid="stSidebar"][aria-expanded="true"]{
#             display: none;
#         }
# </style>
#     """, unsafe_allow_html=True)
 
# hide_sidebar()

load_dotenv()
st.write("# Welcome to Mystic Bot🔮! 👋")


# def delete_page(main_script_path_str, page_name):

#     current_pages = get_pages(main_script_path_str)
#     # st.write(current_pages)

#     for key, value in current_pages.items():
#         if value["page_name"] == page_name:
#             del current_pages[key]
#             break
#         else:
#             pass
#     _on_pages_changed.send()


# delete_page("1_📈_Veri_Çek", "Veri_Çek")

# st.markdown(
#     """
#     Streamlit is an open-source app framework built specifically for 
#     Machine Learning and Data Science projects.
#     **👈 Select a demo from the sidebar** to see some examples
#     of what Streamlit can do!
#     ### Want to learn more?
#     - Check out [streamlit.io](https://streamlit.io)
#     - Jump into our [documentation](https://docs.streamlit.io)
#     - Ask a question in our [community
#         forums](https://discuss.streamlit.io)
#     ### See more complex demos
#     - Use a neural net to [analyze the Udacity Self-driving Car Image
#         Dataset](https://github.com/streamlit/demo-self-driving)
#     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
# """
# )
