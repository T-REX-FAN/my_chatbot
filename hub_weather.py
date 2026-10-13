from datetime import datetime
from zoneinfo import ZoneInfo
import streamlit as st

kst = Zoneinfo("Asia/seoul")

now_kst = datetime.now(kst)

st.write(now)
