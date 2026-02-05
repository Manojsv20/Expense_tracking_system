import streamlit as st
from datetime import datetime
import requests

from add import add_update_tab
from analytics import analytics_tab

API_URL="http://localhost:8000"

st.title("EXPENSE TRACKING SYSTEM")
tab1,tab2=st.tabs(["add/update","Analysis"])

with tab1:
   add_update_tab()
with tab2:
    analytics_tab()