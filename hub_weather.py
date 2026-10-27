from datetime import datetime
from zoneinfo import ZoneInfo
import streamlit as st
import requests

kst = ZoneInfo("Asia/Seoul")

now_kst = datetime.now(kst)

tm_value = now_kst.strftime('%Y%m%d%H%M')

url = f"https://apihub.kma.go.kr/api/typ01/url/kma_sfctm2.php?tm=tm_value&stn=0&help=1&authKey=WHPm-aVWQvmz5vmlVgL54Q"
response = requests.get(url)

all_lines = response.text.split('\n')

clone_lines = []
sample_data = [0.3, 10.0, 1.6, 56.0, 6.9, -9.0, -9.0, -9.0, -9.0]
for x in sample_data:
  if x = 1.6 :
    st.write("x")

st.write("현재 시간: "now_kst)
st.write("변환된 현재 시간: "tm_value)
st.write(response.text)


for 
st.write("현재 온도: ")
