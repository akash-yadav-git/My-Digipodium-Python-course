#to run open terminal and cd to your folder and type
#streamlit run filename.py

import streamlit as st


st.header("Simple Math")

choices=['Area of square','Area of Circle',"Area of triangle"]

choice=st.radio('select an option', choices)
if choice==choices[0]:
    side=st.number_input("length of a side", min_value=1,max_value=100)
    area=side**2
    st.success(f'The total area is={area:.2f}')





   