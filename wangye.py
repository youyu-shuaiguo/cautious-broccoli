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
