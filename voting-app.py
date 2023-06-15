
import streamlit as st

PAGE_CONFIG = {"page_title":"Reddit-like Site","page_icon":":smiley:","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

# Create dictionary to store user info
user_info = {}

# Define functions for the sign up and submit pages
def sign_up():
    st.title("Sign Up")
    user_name = st.text_input("Enter a unique user name")
    email = st.text_input("Enter your email address")
    
    if st.button("Submit"):
        if user_name in user_info:
            st.warning("That user name already exists. Please choose a different one.")
        else:
            user_info[user_name] = email
            st.success("User successfully created. You can now post to the front page.")
            st.button("Post to Front Page", key="post")

def post():
    st.title("Post to Front Page")
    title = st.text_input("Enter a title for your post")
    url = st.text_input("Enter the URL for your post")
    
    if st.button("Submit"):
        st.header(title)
        st.write(f"More information about the post...")
        st.button("Read More")

# Define the main function for the website
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Sign Up", "Front Page"))
    
    if page == "Sign Up":
        sign_up()
    elif page == "Front Page":
        st.title("Front Page")
        for user_name in user_info.keys():
            st.header(user_name)
            st.button("Post", key=f"{user_name}-post")
    
    if st.session_state.get("post"):
        post()

if __name__ == '__main__':
    main()

