import streamlit as st
import requests

# print("hello, world")
# for number in range(1,6):
#   print(number)
#   streamlit.write(number)

st.title("날씨 챗봇")

st.subheader("오늘은 어떠신가요?")

# input("이름을 입력하세요")
col1, col2 = st.columns(2)

with col1:
  name = st.text_input("이름을 입력하세요")
  age = st.number_input("나이를 입력하세요")

  if name:
    st.write(f"{age}살, {name}님 반갑습니다")
    st.header(f"{name}님 반갑습니다")
    # st.write(type(age))

with col2:

  if st.button("날씨를 여쭈워봐도 될까요?"):

    option = st.selectbox("날씨를 선택하세요",["맑음","흐림","비","폭우","지구종말"])
    st.write(option)


SERVICE_KEY = "U%2F3cxgpV%2Bn4fLqOHggb3q0Wzbc2DliDoXqNP4FR5yMD7XMsUdxu6n%2FRS6ymOtyqIBJVC2ddPcwdOrHvX%2B%2FgBvQ%3D%3D"
BASE_URL = "https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0"

nx = st.text_input("지역의 X좌표를 입력하세요 (예:60")
ny = st.text_input("지역의 Y좌표를 입력하세요 (예:60")

if st.button("날씨 확인"):
  params = {
    'serviceKey' : SERVICE_KEY,
    'pageNo': '1',
    'numOfRows': '10',
    'dataType': 'JSON',
    'base_date': '2026813',
    'base_time': '0700',
    'nx': nx,
    'ny': ny,
  }

response = requests.get(BASE_URL, params=params)
data = response.json()
st.write(data)

try:
  items = data['response']['body']['item']
  st.write('##현재 날씨 정보')
  for item in items:
    category = item['category']
    value = item['fcsValue']
    st.write(f"- {category}: {value}")
except KeyError:
  st.error("데이터를 가져올수없습니다.")
