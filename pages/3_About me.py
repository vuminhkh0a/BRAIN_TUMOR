import streamlit as st
from forms.contact import contact_form
import setup
from setup import overall

overall()

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("assets/profile_image.png", width=230)

with col2:
    st.title("Vu Minh Khoa", anchor=False)
    st.write(
        "Sophomore at Hanoi University of Science and Technology, "
        "interested in Computer Vision for medical and healthcare research"
    )

    btn_col1, btn_col2, btn_col3 = st.columns([1,1,1], gap="small")

    with btn_col1:
        st.markdown(
            """
            <a href="https://github.com/vuminhkh0a" target="_blank">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" 
                     width="24" style="vertical-align:middle;margin-right:6px;">
                Github
            </a>
            """,
            unsafe_allow_html=True
        )

    with btn_col2:
        st.markdown(
            """
            <a href="https://www.linkedin.com/in/vmkhoa28/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" 
                     width="24" style="vertical-align:middle;margin-right:6px;">
                Linkedin
            </a>
            """,
            unsafe_allow_html=True
        )

    with btn_col3:
        if st.button("✉️ Contact Me"):
            show_contact_form()    


st.write("\n")
st.subheader("Projects", anchor=False)
st.write(
    """
    - Brain tumor MRI diagnosis app
    - Skin lesion segmentation
    - Custom ResNet50 for object classification with AdamW on CIFAR-10
    - Churn prediction using Machine Learning
    """
)

st.write("\n")
st.subheader("Experiences", anchor=False)
st.write(
    """
    - Research Member, AIMA Warm-up Research Program (Aug 2025 – Present)
    - Research Intern, Institute for AI Innovation and Societal Impact - AI4LIFE, Hanoi University of Science and Technology (Jan 2025 - May 2025)
    """
)

st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
    - Programming: Python (PyTorch, Scikit-learn, Pandas, Numpy, Seaborn, Matplotlib), C++, SQL
    - Knowledge: Fundamental knowledge of Machine Learning and Deep Learning
    - Languages: English (IELTS 7.0)
    """
)
