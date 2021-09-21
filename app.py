# Import necessary libraries 
import streamlit as st
import numpy as np 
import json 

st.title("Address Matching and Normalization App")

# Add an expander for method and task description
my_expander = st.expander(label="Know more")
expander_text = '''
                This section talks about why normalization and how it works in this application. 
                Let me know if this is needed. 
                '''
my_expander.write(expander_text)

# Take two inputs 
add1 = st.text_input(label="Enter Address 1")
add2 = st.text_input(label="Enter Address 2")

# Convert both addresses to lower case 
add1 = add1.lower()
add2 = add2.lower()

'''Convert terms to a single format'''

# Read the json data 
with open('abbreviations.json') as f:
  data = json.load(f)

# Tokenize the address 
token_add1 = add1.split()
token_add2 = add2.split()
st.write(token_add1)


st.write("**Address 1:**", add1)
st.write("**Address 2:**", add2)

