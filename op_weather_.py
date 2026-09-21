import streamlit as st
import requests

API_KEY = "8306a95ad41f685d2e59c0e448102948"

st.title("우리동네 날씨챗봇")
st.write("도시 이름을 입력하면 현재 날씨를 알려드려요")
#city = st.text_input("도시 이름을 영어로 입력하세요")
city_map = {"서울":"Seoul", "부산":"Busan", "인천":"Inchen", "대구":"Daegu", "광주":"Gwangju"}
weather_dict = {"Clouds":"흐림", "Clear":"맑음", "Rain":"비", "Snow":"눈", "Mist":"안개"}

if "message" not in session_state.messages :
  st.session_state.message = []

for message in st. session_state.messages :
  with st.chat_message(message["role"]):
    st.markdown(message["content"])



def get_weather(city_name):
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=kr"
  response = requests.get(url)
  #st.write(response.json())
  return response.json()


if prompt := st.text_input("도시 이름을 입력하세요"):
  st.session_state.message.append({"role":"user", "content":prompt})
  with st.chat_message("user"):
    st.markdown(prompt)
  with st.chat_message("assistant"):
  Eng_city = city_map[prompt,prompt]
  #st.write(city)
  weather_data = get_weather(Eng_city)
  st.write(weather_data)
  


# city = st.text_input("도시 이름을 영어로 입력하세요")

if weather_data.get("cod") == 200:
  Eng_city = city_map[prompt,prompt]
  #st.write(city)
  weather_data = get_weather(Eng_city)
  st.write(weather_data)

  st.write(f"{city}의 날씨를 알려준다")
  st.write(f"날씨는 : weather_dict[{weather_data['weather'][0]['main']}]")
  st.write(f"온도는 : {round(weather_data['main']['temp'])} C")
  st.write(f"최저온도는 : {round(weather_data['main']['temp_min'])} C")
  st.write(f"최고온도는 : {round(weather_data['main']['temp_max'])} C")
  st.markdown(reply)
  st.session_state.message.append({"role":"assistant", "content":prompt})
else:
  reply = "못찾음 ㅅㄱ."
  st.markdown(reply)
  st.session_state.message.append({"role":"assistant", "content":prompt})
