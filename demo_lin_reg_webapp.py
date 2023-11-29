import streamlit as st
import pickle

# Load the pickled model
with open('modelpos.pkl', 'rb') as file:
    model = pickle.load(file)

# Create the Streamlit web app
st.header("Streamlit demo")

st.sidebar.header("This is a web app")

projects_complited = st.sidebar.slider("Select projects_complited to get position", 0, 10, 5)

st.write("projects_complited is:", projects_complited)

yhat_test = model.predict([[projects_complited]])


st.write("position is", yhat_test)
