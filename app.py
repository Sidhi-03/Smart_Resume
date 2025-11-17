import streamlit as st
import google.generativeai as genai
import base64

# -----------------------------------------------------------
# CONFIGURE API KEY
# -----------------------------------------------------------
genai.configure(api_key="Your API key")


MODEL_NAME = "models/gemini-2.0-flash-lite-preview-02-05"

# ----------------------------
# GENERATE RESUME
# ----------------------------
def generate_resume(name, job_title, experience_level, job_description):
    try:
        prompt = f"""
        Create a professional, ATS-friendly resume for:

        Name: {name}
        Job Title: {job_title}
        Experience Level: {experience_level}

        Job Description:
        {job_description}

        Tasks:
        - Extract relevant ATS keywords.
        - Add a skills section using those keywords.
        - Add an optimized summary.
        - Write strong bullet points.
        - Keep formatting clean, plain text, and professional.

        Resume:
        """

        response = genai.GenerativeModel(MODEL_NAME).generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Error generating resume: {str(e)}"


# ----------------------------
# STREAMLIT SETTINGS
# ----------------------------
st.set_page_config(page_title="AI Resume Generator", layout="wide")

# ----------------------------
# AUTO THEME CSS (LIGHT + DARK)
# ----------------------------
adaptive_css = """
<style>
.resume-box {
    background-color: var(--background-color); 
    padding: 20px;
    border-radius: 12px;
    border: 1px solid var(--secondary-background-color);
}

/* Text auto adapts to theme */
.resume-box, .resume-box * {
    color: var(--text-color) !important;
    font-size: 18px;
}

/* Input labels visible in all modes */
label, .stTextInput label, .stSelectbox label, .stTextArea label {
    color: var(--text-color) !important;
    font-weight: 600;
}
</style>
"""
st.markdown(adaptive_css, unsafe_allow_html=True)

# ----------------------------
# UI
# ----------------------------
st.title("⚡ AI Resume Generator (Smart + ATS Optimized)")

name = st.text_input("Your Name")
job_title = st.text_input("Your Target Job Title")

experience_level = st.selectbox(
    "Your Experience Level",
    ["Fresher", "1–2 Years", "3–5 Years", "5+ Years"]
)

job_description = st.text_area(
    "Paste Job Description (Optional but Recommended)",
    height=180
)

# ----------------------------
# GENERATE BUTTON
# ----------------------------
if st.button("🚀 Generate Resume"):
    if not name or not job_title:
        st.warning("⚠ Please enter both Name and Job Title.")
    else:
        with st.spinner("Generating your resume…"):
            resume_text = generate_resume(name, job_title, experience_level, job_description)

        st.markdown("<div class='resume-box'>", unsafe_allow_html=True)
        st.markdown(resume_text.replace("\n", "<br>"), unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
