import streamlit as st
import pandas as pd
import numpy as np
# import random
import matplotlib.pyplot as plt

# print("===")
# print(np.random.rand(1000))
# print()
# print(np.random.rand(1000)) 127.2, 37.4
# lat_loc = (np.random.randn(1000)/50) + 37.76
# lon_loc = (np.random.randn(1000)/50) + -122.4
lat_loc = (np.random.randn(1000)/50) + -20
lon_loc = (np.random.randn(1000)/50) + 40
# lat_loc = (np.random.randn(1000)/50) + 127.2
# lon_loc = (np.random.randn(1000)/50) + 37.4

# id = [range(1,10)]

data = ({
    "lat" : lat_loc,
    "lon" : lon_loc
})
st.dataframe(data)
st.write("위치")
st.map(data)


data = pd.DataFrame({
    "캐릭터": ["전사","마법사","힐러","탱커","랜덤"],
    "선택횟수": [120, 95, 150, 80, 111],
    "승률 (%)": [52, 48, 56, 60, 49],
    "인지도 (%)": [25, 20, 30, 15, 22],
    "공격방식": ["근거리","원거리","원거리","근거리","랜덤"]
})

st.bar_chart(data, x = "공격방식", y="선택횟수",color='캐릭터', stack=False)

plt.rc("font", family="Malgun Gothic")
fig = data.plot.pie(
    y = "인지도 (%)",
    labels = data["캐릭터"],
    autopct = "%1.1f%%",
    figsize = (6,6),
    legend = False,
    title = "캐릭터 별 인지도"
).get_figure()
st.pyplot(fig)

st.scatter_chart(data["캐릭터","선택획수","공격방식"])

