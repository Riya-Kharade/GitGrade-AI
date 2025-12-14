import streamlit as st
from repo_fetcher import fetch_repo_data
from evaluator import calculate_score, get_level
from summary_generator import generate_summary
from roadmap import generate_roadmap

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(page_title="GitGrade AI", layout="wide")

# -------------------------------------------------
# CUSTOM THEME (DARK BLUE – CLEAN)
# -------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
.title {
    font-size: 40px;
    font-weight: 700;
    color: #38bdf8;
}
.subtitle {
    color: #9ca3af;
    font-size: 18px;
}
.section {
    background-color: #020617;
    padding: 25px;
    border-radius: 16px;
    margin-top: 25px;
    box-shadow: 0px 0px 20px rgba(56,189,248,0.15);
}
.card {
    background-color: #020617;
    padding: 20px;
    border-radius: 14px;
    text-align: center;
    box-shadow: 0px 0px 15px rgba(56,189,248,0.2);
}
.card-title {
    color: #9ca3af;
    font-size: 14px;
}
.card-value {
    color: #38bdf8;
    font-size: 28px;
    font-weight: bold;
}
.sidebar-title {
    font-size: 22px;
    font-weight: 600;
    color: #38bdf8;
}

            
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.markdown("<div class='sidebar-title'>🚀 GitGrade AI</div>", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🔍 Analyzer",
        "📄 Report",
        "👔 Recruiter View",
        "⚙️ How It Works"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Evaluate GitHub projects like a recruiter")

# -------------------------------------------------
# HOME PAGE
# -------------------------------------------------
if page == "🏠 Home":
    st.markdown("<div class='title'>GitGrade AI</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Turn your GitHub repository into a recruiter-ready evaluation</div>", unsafe_allow_html=True)

    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("""
### 🔍 What is GitGrade AI?

GitGrade AI is a **repository evaluation system** that analyzes a GitHub project and converts it into:

- ✅ A **quality score (0–100)**
- ✅ A **clear written summary**
- ✅ A **personalized improvement roadmap**

This helps students understand **how their GitHub looks to recruiters**.

### 🎯 Why GitGrade AI exists
Most students:
- Push code without understanding quality
- Don’t know if their commits show effort
- Don’t know what recruiters notice first

GitGrade AI acts as a **virtual coding mentor**.
""")
    st.markdown("</div>", unsafe_allow_html=True)


    

# -------------------------------------------------
# ANALYZER PAGE (MAIN FEATURE)
# -------------------------------------------------
elif page == "🔍 Analyzer":
    st.markdown("<div class='title'>Repository Analyzer</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Paste a public GitHub repository link</div>", unsafe_allow_html=True)

    repo_url = st.text_input("🔗 GitHub Repository URL")

    if st.button("Analyze Repository 🚀"):
        with st.spinner("🔍 GitGrade AI is analyzing the repository..."):
            repo_data = fetch_repo_data(repo_url)

        if not repo_data:
            st.error("Invalid repository or GitHub API error.")
        else:
            score = calculate_score(repo_data)
            level = get_level(score)
            summary, strengths, weaknesses = generate_summary(repo_data, score)
            roadmap = generate_roadmap(repo_data, score)

            # Snapshot Cards
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.markdown(f"<div class='card'><div class='card-title'>Score</div><div class='card-value'>{score}/100</div></div>", unsafe_allow_html=True)
            with c2:
                st.markdown(f"<div class='card'><div class='card-title'>Level</div><div class='card-value'>{level}</div></div>", unsafe_allow_html=True)
            with c3:
                st.markdown(f"<div class='card'><div class='card-title'>Commits</div><div class='card-value'>{repo_data['commits']}</div></div>", unsafe_allow_html=True)
            with c4:
                st.markdown(f"<div class='card'><div class='card-title'>Language</div><div class='card-value'>{repo_data['language']}</div></div>", unsafe_allow_html=True)

            # Summary
            st.markdown("<div class='section'>", unsafe_allow_html=True)
            st.markdown("### 🧠 AI Summary")
            st.write(summary)
            st.markdown("</div>", unsafe_allow_html=True)

            # Roadmap
            st.markdown("<div class='section'>", unsafe_allow_html=True)
            st.markdown("### 🛣️ Improvement Roadmap")
            for i, step in enumerate(roadmap, 1):
                st.write(f"{i}. {step}")
            st.markdown("</div>", unsafe_allow_html=True)

            # Save state
            st.session_state["report_data"] = {
                "repo": repo_data,
                "score": score,
                "level": level,
                "summary": summary,
                "roadmap": roadmap
            }

# -------------------------------------------------
# REPORT PAGE
# -------------------------------------------------
elif page == "📄 Report":
    st.markdown("<div class='title'>Project Report</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Download your GitGrade evaluation</div>", unsafe_allow_html=True)

    if "report_data" not in st.session_state:
        st.warning("Analyze a repository first.")
    else:
        data = st.session_state["report_data"]

        report_text = f"""
GitGrade AI – Repository Evaluation Report

Project: {data['repo']['name']}
Language: {data['repo']['language']}
Commits: {data['repo']['commits']}

Score: {data['score']} / 100
Level: {data['level']}

Summary:
{data['summary']}

Roadmap:
""" + "\n".join([f"- {r}" for r in data["roadmap"]])

        st.download_button(
            "📥 Download Report",
            report_text,
            file_name="GitGrade_Report.txt"
        )

# -------------------------------------------------
# RECRUITER VIEW (UNIQUE FEATURE)
# -------------------------------------------------
elif page == "👔 Recruiter View":
    st.markdown("<div class='title'>Recruiter Perspective</div>", unsafe_allow_html=True)

    if "report_data" not in st.session_state:
        st.warning("Analyze a repository first.")
    else:
        level = st.session_state["report_data"]["level"]

        st.markdown("<div class='section'>", unsafe_allow_html=True)
        if level == "Advanced":
            st.success("Recruiter sees this as a strong, consistent project.")
        elif level == "Intermediate":
            st.info("Recruiter sees potential but expects better practices.")
        else:
            st.warning("Recruiter may question consistency and maturity.")
        st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# HOW IT WORKS (JUDGES LOVE THIS)
# -------------------------------------------------
elif page == "⚙️ How It Works":
    st.markdown("<div class='title'>How GitGrade AI Works</div>", unsafe_allow_html=True)

    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("""
1. Accepts a public GitHub repository URL  
2. Fetches metadata using GitHub API  
3. Analyzes commits, activity & structure  
4. Converts signals into score & level  
5. Generates summary & roadmap  

**No random scoring. Only transparent logic.**
""")
    st.markdown("</div>", unsafe_allow_html=True)
