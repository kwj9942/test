import streamlit as st
import pandas as pd

print("수정사항")
data = open('C:\\KIMUJUNG\\python basic\\my_page\\DM_FPOPL_D_SM_20200205_sample.csv','r')

st.title('인구이동량')
st.header('지역별 인구이동량')

location = st.text_input('지역명 (서울, 대전, 대구, 부산, 세종, 울산)')

if location:
    st.write(location + "지역 인구이동 데이터")
    st.dataframe(data)

if location:
    st.write(location + "지역 인구이동 차트")
    # st.bar_chart(data)

if location:
    st.write(location + "지역 인구이동 시각화")
    # st.map(data[])