import os

try:
    from groq import Groq
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    GROQ_AVAILABLE = True
except:
    GROQ_AVAILABLE = False


def explain_repo_with_llm(repo_data, score, level):
    """
    Uses LLM to explain repo quality like a mentor / recruiter
    Falls back to rule-based explanation if API not available
    """

    if not GROQ_AVAILABLE:
        return (
            f"This project is evaluated as {level} with a score of {score}. "
            "The commit activity, language usage, and documentation were analyzed "
            "to understand project maturity. Improving tests and automation "
            "would further strengthen this repository."
        )

    prompt = f"""
    You are a senior software engineer and recruiter.

    Analyze this GitHub repository summary and explain it in simple terms:

    Project Name: {repo_data['name']}
    Description: {repo_data['description']}
    Language: {repo_data['language']}
    Commits: {repo_data['commits']}
    Score: {score}
    Level: {level}

    Explain:
    1. What this score means
    2. How a recruiter would see this project
    3. What the student should improve next
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content
