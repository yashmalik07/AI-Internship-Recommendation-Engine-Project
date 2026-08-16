import streamlit as st
import pandas as pd

from recommendation_engine import InternshipRecommender


# Page configuration
st.set_page_config(
    page_title="AI Internship Recommendation Engine",
    page_icon="🎯",
    layout="wide"
)


# Title
st.title("🎯 AI Internship Recommendation Engine")

st.write(
    "Find the most suitable internships based on "
    "your skills, domain and preferences."
)


# Load recommender
@st.cache_resource
def load_engine():

    return InternshipRecommender()


recommender = load_engine()


# Sidebar
st.sidebar.header("Student Profile")


students = recommender.students_df


student_options = dict(
    zip(
        students["name"],
        students["student_id"]
    )
)


selected_name = st.sidebar.selectbox(
    "Select Student",
    list(student_options.keys())
)


student_id = student_options[selected_name]


student = students[
    students["student_id"] == student_id
].iloc[0]


# Display student information
st.subheader("👨‍🎓 Student Profile")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Student ID",
        student["student_id"]
    )

with col2:

    st.metric(
        "Domain",
        student["domain"]
    )

with col3:

    st.metric(
        "Experience",
        student["experience_level"]
    )


st.write(
    "**Skills:** "
    + ", ".join(student["skills"])
)


st.divider()


# Recommendation button
if st.button(
    "🚀 Recommend Internships",
    use_container_width=True
):

    st.subheader(
        "✨ Recommended Internships"
    )

    recommendations = (
        recommender.hybrid_recommendation(
            student_id,
            top_n=5
        )
    )

    if not recommendations:

        st.warning(
            "No recommendations available."
        )

    else:

        for i, rec in enumerate(
            recommendations,
            start=1
        ):

            with st.container():

                st.markdown(
                    f"### {i}. {rec['title']}"
                )

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.write(
                        f"**ID:** {rec['internship_id']}"
                    )

                with col2:
                    st.write(
                        f"**Domain:** {rec['domain']}"
                    )

                with col3:
                    st.write(
                        f"**Duration:** {rec['duration']}"
                    )

                with col4:
                    st.write(
                        f"**Match Score:** "
                        f"{rec['hybrid_score']}"
                    )

                st.divider()


# All internships
st.subheader("📚 Available Internships")

display_df = recommender.internships_df.copy()

display_df["required_skills"] = (
    display_df["required_skills"]
    .apply(lambda x: ", ".join(x))
)

st.dataframe(
    display_df,
    use_container_width=True
)


# Footer
st.info(
    "This recommendation engine combines "
    "Collaborative Filtering and Content-Based "
    "Filtering using a Hybrid Recommendation approach."
)
