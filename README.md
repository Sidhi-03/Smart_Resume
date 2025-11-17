# 🚀 Smart AI Resume Generator
### Build Instant ATS-Friendly Resumes Using Google Gemini + Streamlit

This project is a smart resume generator powered by Google Gemini AI.  
Users can instantly generate clean, ATS-friendly, keyword-optimized resumes based on:

- Name  
- Target Job Title  
- Experience Level  
- Job Description (for keyword extraction)

The UI automatically adapts to both light and dark modes.

---

## 🌟 Features

### 🔹 AI-Powered Resume Generation
- Generates ATS-friendly resume using Google Gemini
- Extracts keywords from job description
- Auto-adds optimized skills, summary, and bullet points
- Clean Markdown formatting

### 🔹 Smart UI (Light + Dark Mode Support)
- Text auto-visible in both themes
- Styled resume output area
- Simple & responsive design

### 🔹 User Inputs
- Full Name  
- Target Role  
- Experience Level (Fresher → Senior)  
- Job Description (Optional)

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python | Backend logic |
| Streamlit | Web UI |
| Google Gemini API | AI content generation |
| HTML/CSS | Dynamic styling |

---

---

## 🔑 Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/sidhi-03/Smart-AI-Resume-Generator.git
cd Smart-AI-Resume-Generator
###2️⃣ Install dependencies
```bash
pip install -r requirements.txt
###3️⃣ Add Google Gemini API Key
```bash

Create a folder:

mkdir .streamlit


Create file:

.streamlit/secrets.toml


Paste inside:

GOOGLE_API_KEY = "your_api_key_here"


###⚠️ Never commit your API key to GitHub!

###▶️ Run the App
```bash
streamlit run app.py


Open in browser:

http://localhost:8501

###🚧 Roadmap
```bash

 Export resume to PDF

 Multiple resume templates

 Cover letter generator

 Resume–JD match score

 Skill gap analysis

🤝 Contributing
```bash

Contributions, issues, and feature requests are welcome!


