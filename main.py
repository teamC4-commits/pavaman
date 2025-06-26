
import streamlit as st
from DiseaseClassification import app as prediction_app
from docs import app as docs_app
from data import app as data_app
from cropScope import app as cropScope_app


query_params = st.query_params
page = query_params.get("page", "cropScope")


st.markdown("""
    <style>
        .navbar {
            display: flex;
            justify-content: start;
            gap: 20px;
            padding: 10px 0;
            border-bottom: 1px solid #ddd;
        }
        .navbar a {
            text-decoration: none;
            font-weight: 600;
            color: #4a4a4a;
            padding: 8px 16px;
            border-radius: 8px;
        }
        .navbar a:hover {
            background-color: 0e1117;
            border: 2px solid white;
            color:white;
        }
    </style>
    <div class="navbar">
        <a href='?page=cropScope' target="_self">Multispectral Analysis</a>
        <a href='?page=DiseaseClassification' target="_self">Disease Prediction</a>
        <a href='?page=Docs' target="_self">Docs</a>
        <a href='?page=Data' target="_self">Data</a>
    </div>
""", unsafe_allow_html=True)


if page=="cropScope":
    cropScope_app()
elif page == "DiseaseClassification":
    prediction_app()
elif page == "Docs":
    docs_app()
elif page == "Data":
    data_app()
else:
    st.error("Page not found.")
