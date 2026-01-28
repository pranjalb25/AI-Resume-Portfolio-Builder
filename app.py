import streamlit as st
from resume_parser import extract_text
from jd_parser import clean_text
from similarity import match_score
from skill_extractor import extract_skills
from portfolio_generator import generate_portfolio_summary

st.set_page_config(page_title="AI Resume & Portfolio Builder")

st.title("AI Resume & Portfolio Builder")

resume_file = st.file_uploader("Upload Resume (PDF/DOCX)")
jd_text = st.text_area("Paste Job Description")

if resume_file and jd_text:
    resume_text = extract_text(resume_file)
    jd_clean = clean_text(jd_text)

    score = match_score(resume_text, jd_clean)
    st.subheader(f"📊 Resume–JD Match Score: {score}%")

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_clean)

    st.subheader("✅ Resume Skills")
    st.write(resume_skills)

    missing = list(set(jd_skills) - set(resume_skills))
    st.subheader("❌ Missing Skills")
    st.write(missing)


    st.subheader("🧠 AI-Generated Portfolio Summary")
    portfolio_text = generate_portfolio_summary(resume_skills)
    st.success(portfolio_text)
