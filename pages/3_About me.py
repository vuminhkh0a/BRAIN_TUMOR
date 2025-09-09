import streamlit as st

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
# col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
# with col1:
#     st.image("assets/profile_image.png", width=230)

# with col2:
#     st.title("Vu Minh Khoa", anchor=False)
#     st.write("Sophomore at Hanoi University of Science and Technology, interested in Computer Vision for medical and healthcare research")
#     st.link_button(label='Github', url='https://github.com/vuminhkh0a')
#     st.link_button(label='Linkedin', url='https://www.linkedin.com/in/vmkhoa28/')
#     if st.button("✉️ Contact Me"):
#         show_contact_form()

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
        st.link_button(label="Github", url="https://github.com/vuminhkh0a")

    with btn_col2:
        st.link_button(label="Linkedin", url="https://www.linkedin.com/in/vmkhoa28/")

    with btn_col3:
        if st.button("✉️ Contact Me"):
            show_contact_form()



# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience", anchor=False)
st.write(
    """
    - 7 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas), SQL, VBA
    - Data Visualization: PowerBi, MS Excel, Plotly
    - Modeling: Logistic regression, linear regression, decision trees
    - Databases: Postgres, MongoDB, MySQL
    """
)
