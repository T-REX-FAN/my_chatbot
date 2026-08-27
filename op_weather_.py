import streamlit as st
import request

API_KEY = "8306a95ad41f685d2e59c0e448102948"

st.title("우리동네 날씨챗봇")
st.write("도시 이름을 입력하면 현재 날씨를 알려드려요")

def get_weather(city_name):
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=kr"
  response = request.get(url)
  return response.json

city = st.text_input("도시 이름을 영어로 입력하세요")

if city:
  get_weather(city)
