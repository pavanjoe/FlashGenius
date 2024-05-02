import streamlit as st
from streamlit_option_menu import option_menu

# Importing specific functions from pages module which are assumed to be different pages of the app

# Configuring the Streamlit app's page settings such as title, icon, layout, and sidebar state
st.set_page_config(
    page_title="FlashCards",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items=None,
)

# Custom CSS to hide the Streamlit's hamburger menu on the sidebar
st.markdown(
    """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Setting a header for the app
st.header("FlashCards")

# Setting background image and font style for the app using custom CSS
page_bg_img = f"""
    <style>
    .st-emotion-cache-13k62yr {{
    font-size: 20px;
    background-size: cover;
    background-color: rgb(57 87 66);
    }}
    </style>
    """

# Applying the background image style to the app
st.markdown(page_bg_img, unsafe_allow_html=True)

# Adding a text block that describes the functionality of the app
st.text(
    """

Welcome to FlashGenius!

Empower your learning journey with FlashGenius - the ultimate tool to transform your study notes into dynamic flashcards. Designed with students in mind, FlashGenius simplifies the process of converting your notes into interactive flashcards, enabling you to master your subjects with ease.

Gone are the days of tedious manual creation of flashcards. With FlashGenius, you simply input your study notes, and our intelligent algorithm does the rest. Whether you're preparing for exams, reinforcing key concepts, or enhancing long-term retention, FlashGenius adapts to your learning needs.

Our platform offers:

Effortless Conversion: Say goodbye to time-consuming manual flashcard creation. Just upload your study notes, and let FlashGenius instantly generate custom flashcards tailored to your content.

Personalized Learning: Experience personalized learning like never before. FlashGenius analyzes your notes and creates flashcards that target your weak areas, ensuring focused and effective study sessions.

Interactive Practice: Engage in active learning through interactive flashcard practice. Test your knowledge, review concepts, and track your progress effortlessly, all within the FlashGenius platform.

Anywhere, Anytime Access: Study on your own terms. Whether you're at home, in the library, or on the go, FlashGenius provides seamless access to your flashcards across devices, ensuring uninterrupted learning.

Optimized Performance: Maximize your study efficiency with FlashGenius's optimized performance. Experience lightning-fast loading times, intuitive interface, and reliable functionality every time you use our platform.

Join thousands of students worldwide who are revolutionizing their learning experience with FlashGenius. Start converting your study notes into powerful flashcards today and unleash your inner genius!

Sign up now and embark on a journey towards academic excellence with FlashGenius!
"""
)

# Creating a custom button using HTML and CSS that links to the main page of the app
st.markdown(
    f'<a href="/main" target="_self"><button class="button-6" type="button" style="padding: 10px 20px;font-family:sans-serif;border-radius: 14px;background-color:#FFFFFF;color:black;font-size: 16px;">Get Started</button></a>',
    unsafe_allow_html=True,
)

