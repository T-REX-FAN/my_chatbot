 import streamlit

# print("hello, world")
# for number in range(1,6):
#   print(number)
#   streamlit.write(number)

input("이름을 입력하세요")
name = st.text_input("이름을 입력하세요")
st.write(f"{name}님 반갑습니다")
