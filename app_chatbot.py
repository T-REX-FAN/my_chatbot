import streamlit as st

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
    st.button("나이를 여쭈어봐도 될까요?")
    # st.write(type(age))

with col2:

  if name and st.button("나이를 여쭈어봐도 될까요?") :

    option = st.selectbox("날씨를 선택하세요",["맑음","흐림","비","폭우","지구종말"])
    st.write(option)
