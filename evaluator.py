from datetime import datetime

def calculate_score(repo_data):
    score = 0

    # 1️⃣ Commit Score (30)
    commits = repo_data.get("commits", 0)
    if commits >= 20:
        score += 30
    elif commits >= 10:
        score += 20
    elif commits >= 5:
        score += 10

    # 2️⃣ Documentation Score (20)
    if repo_data.get("description"):
        score += 20

    # 3️⃣ Language Score (20)
    if repo_data.get("language"):
        score += 20

    # 4️⃣ Activity Score (30)
    updated_at = repo_data.get("updated_at")
    if updated_at:
        last_update = datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%SZ")
        days_diff = (datetime.utcnow() - last_update).days

        if days_diff <= 30:
            score += 30
        elif days_diff <= 90:
            score += 20
        else:
            score += 10

    return score


def get_level(score):
    if score >= 75:
        return "Advanced"
    elif score >= 45:
        return "Intermediate"
    else:
        return "Beginner"
