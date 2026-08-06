import streamlit as st

# print("hello, world")
# for number in range(1,6):
#   print(number)
#   streamlit.write(number)

# input("이름을 입력하세요")
name = st.text_input("이름을 입력하세요")
age = st.text_input("나이를 입력하세요")

if name:
  st.write(f"{age}살, {name}님 반갑습니다")
  st.write(type(age))
