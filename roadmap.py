def generate_roadmap(repo_data, score):
    roadmap = []

    # Documentation
    if not repo_data.get("description"):
        roadmap.append("Add a clear README with project overview, setup steps, and usage instructions.")

    # Commit practices
    if repo_data.get("commits", 0) < 10:
        roadmap.append("Increase commit frequency with meaningful commit messages.")

    # Testing (simple assumption)
    roadmap.append("Add unit tests to improve code reliability and maintainability.")

    # Project maturity
    if score < 75:
        roadmap.append("Refactor code for better readability and modular structure.")

    # Advanced suggestions
    if score >= 75:
        roadmap.append("Add CI/CD using GitHub Actions for automated testing.")
        roadmap.append("Improve project documentation with examples and screenshots.")
        roadmap.append("Consider open-sourcing the project and managing issues properly.")

    return roadmap
