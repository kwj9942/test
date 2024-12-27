import streamlit as st
from datetime import time, date

st.title('인구이동 데이터 선택')

loc_options = ["서울", "대전", "대구", "부산", "세종", "울산"]
loc_selcet = st.selectbox("지역 선택", loc_options)

# y_options = st.number_input("년도 선택", min_value=2020, max_value=2024)
# m_options = st.number_input("월 선택", min_value=1, max_value=12)
# d_options = st.number_input("날짜 선택", min_value=1, max_value=31)
d = st.date_input("날짜 선택", date(2020, 1, 1))
# time_options = st.number_input("시간 선택", min_value=0, max_value=24)
start_time = st.slider(
    "시간 선택",
    value = time(00, 00),
    format="hh : mm",
)


if st.button('선택 완료!'):
    st.write(f"지역명 {loc_selcet}")
    # st.write(f"선택 날짜  {y_options} - {m_options} - {d_options}")
    st.write(f"선택 날짜  {d}")
    st.write(f"선택 시간  {start_time}시")