import streamlit as st

def footer_home():
    #logo_url = "src\imgs\4cfca67d-c43b-4604-97ff-aa42211d5967.png"
    st.markdown(
        f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
            <p style="font-weight:bold; color:black;"> Created with ❤️ by Aniket Patel</p>
        <div>
        """
        ,
        unsafe_allow_html=True
    )