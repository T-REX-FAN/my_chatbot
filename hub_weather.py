from datetime import datetime
from zoneinfo import ZoneInfo
import streamlit as st

kst = ZoneInfo("Asia/seoul")

now_kst = datetime.now(kst)

st.write(now)
