
# 🚀 GitGrade AI

**GitGrade AI** is an AI-powered GitHub repository evaluation system that analyzes public GitHub projects from a **recruiter’s perspective** and converts them into a meaningful **Score, Summary, and Improvement Roadmap**.

This project helps students and developers understand how their GitHub repositories appear to recruiters and how they can improve code quality, documentation, and development practices.

---

## 🔍 What GitGrade AI Does

Given a **public GitHub repository URL**, GitGrade AI:

- 📊 Generates a **GitGrade Score (0–100)**
- 🏷️ Classifies the project as **Beginner / Intermediate / Advanced**
- 🧠 Produces a **human-readable summary**
- 🛣️ Creates a **personalized improvement roadmap**
- 👔 Shows a **Recruiter’s Perspective**
- 📄 Allows downloading a **clean evaluation report**

---

## 🎯 Why GitGrade AI?

Most students push code to GitHub but:
- Don’t know if their project looks professional
- Don’t understand commit consistency
- Don’t know what recruiters notice first

GitGrade AI acts as a **virtual coding mentor** that clearly tells:
> What’s good, what’s missing, and what to do next.

---

## 🧠 How It Works

1. Accepts a public GitHub repository URL  
2. Fetches repository metadata using GitHub API  
3. Analyzes commits, activity, language usage, and documentation  
4. Applies rule-based + AI-inspired evaluation logic  
5. Generates score, summary, and roadmap  

**No random scoring. Only transparent logic.**

---

## 🖥️ Application Pages

- 🏠 **Home** – Introduction and purpose of GitGrade AI  
- 🔍 **Analyzer** – Paste GitHub repo link and analyze  
- 📄 **Report** – Download evaluation report  
- 👔 **Recruiter View** – See how recruiters perceive the project  
- ⚙️ **How It Works** – Clear explanation of system logic  

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (Frontend & UI)
- **GitHub REST API**
- **Rule-based evaluation logic**
- **Custom CSS dashboard theme**

---

## 📦 Project Structure

```
gitgrade-ai/
│
├── app.py
├── repo_fetcher.py
├── evaluator.py
├── summary_generator.py
├── roadmap.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📄 Sample Output

**Input:**
```
https://github.com/username/repository-name
```

**Output:**
```
Score: 78 / 100
Level: Intermediate

Summary:
Strong code consistency and folder structure; needs more tests and documentation.

Roadmap:
- Add unit tests
- Improve README with project instructions
- Introduce CI/CD using GitHub Actions
```

---

## 🌱 Future Enhancements

- LLM-powered deep code review
- Repository comparison (two repos)
- PDF report generation
- CI/CD quality checks
- Code complexity analysis

---

## 👩‍💻 Author

Built with ❤️ for students and developers to grow better GitHub profiles.

---

⭐ If you like this project, consider giving it a star!
