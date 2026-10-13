from datetime import datetime
from zoneinfo import ZoneInfo
import streamlit as st

kst = ZoneInfo("Asia/Seoul")

now_kst = datetime.now(kst)

tm_value = now_kst.striftime('%Y%m%d%H%M')

st.write(now_kst)
st.write(tm_value)
