from datetime import datetime
from zoneinfo import ZoneInfo
import streamlit as st

kst = ZoneInfo("Asia/Seoul")

now_kst = datetime.now(kst)

tm_value = now_kst.strftime('%Y%m%d%H%M')

url = https://apihub.kma.go.kr/api/typ01/url/kma_sfctm2.php?tm=tm_value&stn=0&help=1&authKey=WHPm-aVWQvmz5vmlVgL54Q
response = requests.get(url)

st.write(now_kst)
st.write(tm_value)
st.write(response)
