import streamlit as st 

st.title("名前記憶アプリ")
if'name'not in st.session_state:
    st.session_state.name = "value"
    
name = st.text_input("あなたの名前を入力してください")
if st.button("名前を記憶"):
    st.session_state.value = st.session_state.name