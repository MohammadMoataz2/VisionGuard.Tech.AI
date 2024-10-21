import streamlit as st

# Inject CSS for custom styling
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 70px;
        font-weight: 800;
        color: #C0C0C0; /* Vibrant reddish-orange */
        font-family: 'Arial', sans-serif;
        text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.25); /* Soft shadow for depth */
        margin-top: 60px;
        margin-bottom: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render the title with emoji and CSS class
st.markdown("<h1 class='title'>🛡️ Vision Guard</h1>", unsafe_allow_html=True)




