def generate_summary(repo_data, score):
    strengths = []
    weaknesses = []

    # Strengths
    if repo_data["commits"] >= 15:
        strengths.append("Consistent and regular commit history")

    if repo_data.get("description"):
        strengths.append("Project has a clear description")

    if repo_data.get("language"):
        strengths.append(f"Uses {repo_data['language']} as the primary language")

    # Weaknesses
    if repo_data["commits"] < 5:
        weaknesses.append("Very low development activity")

    if not repo_data.get("description"):
        weaknesses.append("Missing or weak project documentation")

    # Summary text
    if score >= 75:
        summary = (
            "This repository demonstrates strong development practices with good consistency "
            "and a clear project purpose."
        )
    elif score >= 45:
        summary = (
            "This repository shows moderate development effort but has room for improvement "
            "in structure and consistency."
        )
    else:
        summary = (
            "This repository is at an early stage and requires significant improvements "
            "in development practices and documentation."
        )

    return summary, strengths, weaknesses
