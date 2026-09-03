import streamlit as st
import requests

API_KEY = "8306a95ad41f685d2e59c0e448102948"

st.title("우리동네 날씨챗봇")
st.write("도시 이름을 입력하면 현재 날씨를 알려드려요")

def get_weather(city_name):
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=kr"
  response = requests.get(url)
  st.write(response.json())
  #return response.json

city = st.text_input("도시 이름을 영어로 입력하세요")

if city:
  st.write(city)
  get_weather(city)

  st.write(f"{city}의 날씨를 알려준다")
  st.write(f"날씨는 : {weather_data['weather'][0]['description']}")
  st.wrtie(f"온도는 : {weather_data['main']['temp']} C")
