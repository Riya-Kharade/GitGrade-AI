# 🚀 GitGrade AI

**GitGrade AI** is an intelligent GitHub repository evaluation system that analyzes a public GitHub project and converts it into a **recruiter-style assessment** with a score, summary, and personalized improvement roadmap.

It helps students and developers understand **how their GitHub projects look from a recruiter’s perspective** and what they should improve next.

---

## 🔍 Problem Statement

Most students push code to GitHub without knowing:
- How clean or mature their project looks
- Whether their commit history shows real effort
- What recruiters actually notice first

GitGrade AI solves this by acting as a **virtual coding mentor**.

---

## 🎯 What GitGrade AI Provides

For any public GitHub repository, GitGrade AI generates:

- ✅ **GitGrade Score (0–100)**  
- ✅ **Project Level** (Beginner / Intermediate / Advanced)  
- ✅ **Human-Readable Summary**  
- ✅ **Strengths & Weaknesses**  
- ✅ **Personalized Improvement Roadmap**  
- ✅ **Recruiter Perspective View**  
- ✅ **Downloadable Project Report**

---

## 🧠 How It Works

1. User enters a **public GitHub repository URL**
2. System fetches repository metadata using the **GitHub API**
3. Repository is analyzed based on:
   - Commit consistency
   - Project activity
   - Language usage
   - Documentation signals
4. Rule-based logic converts these signals into:
   - Score
   - Level
   - Summary
   - Roadmap

> ⚠️ No random scoring. Only transparent, explainable logic.

---

## 🖥️ Application Pages

### 🏠 Home
- Introduction to GitGrade AI
- Purpose and value for students

### 🔍 Analyzer
- Input GitHub repository URL
- Displays score, level, summary, and roadmap

### 📄 Report
- Generate and download a clean evaluation report

### 👔 Recruiter View
- Shows how a recruiter would perceive the project

### ⚙️ How It Works
- Explains the evaluation pipeline step by step

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Data Source**: GitHub Public API
- **Logic**: Rule-based evaluation system
- **Styling**: Custom CSS (Dark Dashboard Theme)

---

## 📦 Project Structure

gitgrade-ai/
│
├── app.py
├── repo_fetcher.py
├── evaluator.py
├── summary_generator.py
├── roadmap.py
├── requirements.txt
└── README.md



---

## ▶️ How to Run Locally

```bash
# Clone the repository
git clone <your-repo-link>

# Navigate to project folder
cd gitgrade-ai

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py


🌟 Why GitGrade AI is Unique

Recruiter-centric evaluation

Transparent scoring logic

Actionable roadmap instead of vague feedback

Clean dashboard UI

Beginner-friendly and hackathon-ready

🚀 Future Enhancements

LLM-based deep code analysis

Compare multiple repositories

PDF report generation

GitHub login & profile analysis

CI/CD & test detection

AI-generated code improvement suggestions

👩‍💻 Author

Riya Sunil Kharade
Engineering Student | Web & AI Enthusiast

📌 License

This project is for educational and hackathon purposes.


---

If you want, I can also:
- Rename the repo perfectly for GitHub
- Shorten README for hackathon submission
- Add **screenshots section**
- Prepare **submission description**

Just tell me 😊
