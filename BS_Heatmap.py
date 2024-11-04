import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Split Layout Example", layout="wide")

# Style the main area
st.markdown(
    """
    <style>
    .main-background {
        background-color: #000000; /* Black background for the main area */
        color: white; /* White text for contrast */
        padding: 20px; /* Padding for the content */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create a sidebar for inputs
st.sidebar.title("Input Section")
input_text = st.sidebar.text_input("Enter something:")
input_number = st.sidebar.number_input("Enter a number:", min_value=0)

# Main area
st.markdown('<div class="main-background">', unsafe_allow_html=True)
st.title("Display Section")
st.write("You entered: ", input_text)
st.write("Number entered: ", input_number)
st.markdown('</div>', unsafe_allow_html=True)
