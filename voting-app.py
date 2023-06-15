
import streamlit as st

PAGE_CONFIG = {"page_title":"Reddit-like Site","page_icon":":smiley:","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

# Define a boolean session state variable for user authentication.
if "is_authenticated" not in st.session_state:
    st.session_state.is_authenticated = False

# Define a dictionary to store user-related information.
user_info = {}

# Define a dictionary to store posts.
posts = {}

# Define functions for the sign in, sign up, and profile pages.
def sign_in():
    st.title("Sign In")
    user_name = st.text_input("Enter your user name")
    if st.button("Sign In"):
        if user_name in user_info and user_info[user_name]["authenticated"]:
            st.success("You are now signed in.")
            st.session_state.is_authenticated = True
        else:
            st.warning("Invalid user name or password.")

def sign_up():
    st.title("Sign Up")
    user_name = st.text_input("Enter a unique user name")
    password = st.text_input("Enter your password", type="password")
    
    if st.button("Submit"):
        if user_name in user_info:
            st.warning("That user name already exists. Please choose a different one.")
        else:
            user_info[user_name] = {"password": password, "authenticated": True}
            st.success("User successfully created. You can now sign in.")
            st.button("Sign In", key="sign_in")

def profile():
    st.title("Profile")
    st.write("This is your profile page.")
    st.button("Sign Out", key="sign_out")

# Define functions for the front page and post pages
def front_page():
    st.title("Front Page")
    st.write("Welcome to our Reddit-like site!")
    if st.session_state.is_authenticated:
        st.button("Create Post", key="create_post")
    for post_id in posts.keys():
        post = posts[post_id]
        st.header(post["title"])
        st.write(f"Posted by {post['user_name']}")
        st.write(f"URL: {post['url']}")
        comment = st.text_input("Add a comment", key=f"{post_id}-comment")
        if st.button("Add Comment", key=f"{post_id}-add_comment") and comment:
            post.setdefault("comments", []).append(comment)
        if "comments" in post:
            for comment in post["comments"]:
                st.write(comment)

def create_post():
    st.title("Create Post")
    title = st.text_input("Enter a title for your post")
    url = st.text_input("Enter the URL for your post")
    content = st.text_area("Enter the content for your post")
    
    if st.button("Submit") and title and url:
        post_id = len(posts) + 1
        posts[post_id] = {"title": title, "url": url, "user_name": next(iter(user_info))}
        if content:
            posts[post_id]["content"] = content

# Define the main function for our website
def main():
    st.sidebar.title("Navigation")
    if st.session_state.is_authenticated:
        st.sidebar.button("My Profile", key="profile")
    else:
        st.sidebar.button("Sign In", key="sign_in")
        st.sidebar.button("Sign Up", key="sign_up")
        
    if st.session_state.get("sign_in"):
        sign_in()
    elif st.session_state.get("sign_up"):
        sign_up()
    elif st.session_state.get("profile"):
        profile()
    elif st.session_state.is_authenticated:
        page = st.sidebar.radio("Go to", ("Front Page", "Create Post"))
        if page == "Front Page":
            front_page()
        elif page == "Create Post":
            create_post()
    else:
        st.write("Please sign in or sign up.")
    
if __name__ == '__main__':
    main()

