import  streamlit as st
with st.sidebar:
    st.title('hi')
    st.write('你好')
    ages = st.number_input('你的年龄是:', value = 0, min_value = 0, max_value = 150, step = 1)
    if ages:
        st.write(f'原来已经{ages}岁了....')
    sure = st.button("点击here")
    if sure:
        st.write('你已确定')
st.write('欢迎来到洛阳🥻')
date = [{"lat": 34.605, "lon": 112.415}]
st.map(date, zoom = 12)
