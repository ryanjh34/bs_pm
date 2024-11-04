import streamlit as st

# Set the page configuration for a better layout
st.set_page_config(page_title="Split Screen Example", layout="wide")

# Create two columns for layout
col1, col2 = st.columns([1, 2])

# Styling the first column (1/3 of the screen) to be grey
with col1:
    st.markdown(
        """
        <style>
        .grey-background {
            background-color: #D3D3D3;
            height: 100vh; /* Full height of the viewport */
            padding: 20px; /* Padding for the content */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="grey-background">', unsafe_allow_html=True)
    
    # Add your input elements here
    st.header("Input Section")
    input_text = st.text_input("Enter something:")
    input_number = st.number_input("Enter a number:", min_value=0)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Styling the second column (2/3 of the screen) to be black
with col2:
    st.markdown(
        """
        <style>
        .black-background {
            background-color: #000000;
            color: white; /* Set text color to white for contrast */
            height: 100vh; /* Full height of the viewport */
            padding: 20px; /* Padding for the content */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="black-background">', unsafe_allow_html=True)
    
    st.header("Display Section")
    # You can display some outputs or additional information here
    st.write("This section can be used to display results or other information.")
    
    st.markdown('</div>', unsafe_allow_html=True)

