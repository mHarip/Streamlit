import streamlit as st

# --- AUTHENTICATION ---
if not st.user.is_logged_in:
    st.button("Log in with Google", on_click=st.login)
    st.stop()

# Optional: Limit to a specific email
allowed_email = "mprasadasce@gmail.com"
if st.user.email != allowed_email:
    st.error("Access denied: You are not authorized to view this app.")
    st.stop()

# --- APP CONTENT ---
st.button("Log out", on_click=st.logout)

st.title("Hello Streamlit-er 👋")
st.markdown(
    """ 
    This is a playground for you to try Streamlit and have fun. 

    **There's :rainbow[so much] you can build!**
    
    We prepared a few examples for you to get started. Just 
    click on the buttons above and discover what you can do 
    with Streamlit. 
    """
)

if st.button("Send balloons!"):
    st.balloons()
