import streamlit as st 

st.title("ユーザー情報入力")

if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
    
if 'user_grade' not in st.session_state:
    st.session_state.user_grade = ""
    
if 'user_hobby' not in st.session_state:
    st.session_state.user_hobby = ""
    
name = st.text_input("あなたの名前を入力してください")
if st.button("名前を保存"):
    st.session_state.user_name = name
    st.success("名前を保存しました！")
    
st.write(f"現在保存されている名前：{st.session_state.user_name}")



name = st.text_input("名前")
grade = st.selectbox("学年",["","小学５年","小学６年","中学１年","中学２年","中学３年"])
hobbies = st.multiselect("趣味",["読書","スポーツ","ゲーム","音楽","絵画","その他"])

if st.button("情報を保存"):
    st.session_state.user_name = name
    st.session_state.user_grade = grade
    st.session_state.user_hobby = hobbies
    
    st.success("情報を保存しました！")