import streamlit as st
import pandas as pd
import altair as alt 
import numpy as np

st.set_page_config(layout="wide")

#import the university data set
university_data = pd.read_excel("universityrankings.xlsx")

university = university_data["Institution"]
national = university_data["National Rank"]
employ = university_data["Employability Rank"]
faculty = university_data["Faculty Rank"]
research = university_data["Research Rank"]
world = university_data["Score"]

st.title("World Rankings by University")

st.sidebar.header("Interact with me!")

user_name = st.sidebar.text_input('What is your name?')
university_name = st.sidebar.selectbox("Choose a University to view!",list(university))

x_val = st.sidebar.selectbox("Pick a variable to compare!",university_data.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick another variable to compare!",university_data.select_dtypes(include=np.number).columns.tolist())


if user_name != "":
    st.write(f"Welcome {user_name}!")
else:
     st.write(f"Please enter your name!")

if university_name != "":
    st.write(f"Your favorite University is {university_name}!")
else:
    st.write(f"Please choose a unviersity!")



scatter = alt.Chart(university_data, title=f"{x_val} vs. {y_val}").mark_point(color= 'pink').encode(
    alt.X(x_val, title=f"{x_val}"),
    alt.Y(y_val, title=f"{y_val}"),
    tooltip = [x_val,y_val])
st.altair_chart(scatter, use_container_width=True)

st.subheader(f"The National Ranking for {university_name} is {employ}.")




st.write(university_data)
