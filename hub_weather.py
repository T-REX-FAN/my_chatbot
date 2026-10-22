from datetime import datetime
from zoneinfo import ZoneInfo
import streamlit as st
import requests

kst = ZoneInfo("Asia/Seoul")

now_kst = datetime.now(kst)

tm_value = now_kst.strftime('%Y%m%d%H%M')

url = f"https://apihub.kma.go.kr/api/typ01/url/kma_sfctm2.php?tm=tm_value&stn=0&help=1&authKey=WHPm-aVWQvmz5vmlVgL54Q"
response = requests.get(url)

st.write("현재 시간: "now_kst)
st.write("변환된 현재 시간: "tm_value)
st.write(response.text)

st.write("현재 온도: ")
