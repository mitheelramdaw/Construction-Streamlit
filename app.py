import streamlit as st
import pandas as pd
import numpy as np



# Page Title
st.title("Streamlit App Template")

# Add text
st.write("Interactive Graphical App")

# Add a header
st.header(" Data Viz")

st.camera_input ("enter call :camera:")
# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.tan(x)

# Display the data using a line chart
st.line_chart(pd.DataFrame({"x": x, "y": y}))

# Add a slider with larger dot
st.header("Section 2: Interactivity")

slider_value = st.slider("Select a value", 0, 100, 50)
st.write("Value selcted:", slider_value)

# Create a sample dataframe
data = {
    "Name": ["Giga", "Ryan", "Mex"],
    "Age": [22, 20, 25]
}

df = pd.DataFrame(data)

st.header("Donuts: Data Display")

st.write("Execs of Kushinga:")
st.dataframe(df)

# Add a button
if st.button("Click me"):
    st.write("Button clicked!")

# Add an expander
with st.expander("Learn more"):
    st.write("Visit kushing.dev")

# Add footer text
st.text("© 2023 Kushinga")


import streamlit as st

# Fake user credentials (for demonstration purposes)
valid_username = "user"
valid_password = "password"

def main():
    st.title("👤 Login Page")


    # User input for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):
        if username == valid_username and password == valid_password:
            st.success("Logged in as {}".format(username))
            # Add your application logic here after successful login
        else:
            st.error("Invalid credentials. Please try again.")

if __name__ == "__main__":
    main()
