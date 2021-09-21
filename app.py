# Import necessary libraries 
import streamlit as st
import numpy as np 
import json 
from fuzzywuzzy import fuzz

# Custom modules 
from fuzzy_matching import levenshtein_ratio_and_distance

#### Start creating the app 


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

#### Convert terms to a single format

# Read the json data 
with open('abbreviations.json') as f:
  abb_data = json.load(f)

# Tokenize the address 
token_add1 = add1.split()
token_add2 = add2.split()

# Iterate through the list and replace any word that is in the abbreviation
for i in range(len(token_add1)): 
    if abb_data.get(token_add1[i], 0):
        token_add1[i] = abb_data[token_add1[i]]


for i in range(len(token_add2)): 
    if abb_data.get(token_add2[i], 0):
        token_add2[i] = abb_data[token_add2[i]]

# Join the sentences again 
add1 = " ".join(token_add1)
add2 = " ".join(token_add2)

#### Fuzzy matching using Levenstein Distance
st.subheader("Calculating the levenstein distance")
distance = levenshtein_ratio_and_distance(add1, add2)
ratio = levenshtein_ratio_and_distance(add1, add2, ratio_calc = True)

st.write("Levenstein distance", distance)
st.write("Levenstein match ratio:", ratio)

#### Fuzzy Wuzzy matching 
st.subheader("Fuzzy Match Percentage")
fuzz_ratio = fuzz.token_set_ratio(add1, add2)
st.write(f"Address match ratio: {fuzz_ratio}% match")


#### Show the sentences 
st.subheader("Fixed Address format")
st.write("**Address 1:**", add1)
st.write("**Address 2:**", add2)



st.subheader("Words that can be abbreviated at the moment")
st.write(abb_data)