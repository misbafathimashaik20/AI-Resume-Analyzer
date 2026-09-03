import streamlit as st
from resume_parser import extract_resume_text


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="centered"
)


st.title("🤖 AI Resume Analyzer")

st.write(
    "Upload your resume and let the system analyze it."
)


uploaded_file = st.file_uploader(
    "📄 Upload your Resume",
    type=["pdf", "docx"]
)


if uploaded_file is not None:

    st.success("Resume uploaded successfully! ✅")

    if st.button("🔍 Analyze Resume"):

        resume_text = extract_resume_text(uploaded_file)

        st.subheader("📄 Extracted Resume Text")

        st.text_area(
            "Resume Content",
            resume_text,
            height=400
        )

        st.success("Resume text extracted successfully! 🎉")
