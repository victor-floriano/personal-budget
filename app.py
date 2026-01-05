from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Personal Budget", layout="wide")

html = Path("personal-budget.html").read_text(encoding="utf-8")
st.components.v1.html(html, height=1200, scrolling=True)
