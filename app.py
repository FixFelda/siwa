"""Streamlit wrapper untuk Kalkulator & Simulasi 3D Spektrofotometer UV-Vis
(Penetapan kadar fosfat metode asam askorbat).

Seluruh aplikasi ada di index.html (HTML + JS + three.js). File ini hanya
menampilkannya di Streamlit, sehingga tampilan dan perhitungan tetap identik.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Kadar Fosfat - Spektrofotometer Digital",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hilangkan padding & header bawaan Streamlit agar aplikasi tampil penuh
st.markdown(
    """
    <style>
      header[data-testid="stHeader"], footer {display:none;}
      .block-container {padding:0 !important; max-width:100% !important;}
      iframe {border:0;}
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "index.html"
html = html_path.read_text(encoding="utf-8")

components.html(html, height=950, scrolling=True)
