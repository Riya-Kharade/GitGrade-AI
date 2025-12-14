from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def generate_pdf_report(
    filename,
    repo_data,
    score,
    level,
    summary,
    strengths,
    weaknesses,
    roadmap
):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    y = height - 50

    def draw_line(text):
        nonlocal y
        c.drawString(50, y, text)
        y -= 18
        if y < 50:
            c.showPage()
            y = height - 50

    # Title
    c.setFont("Helvetica-Bold", 20)
    draw_line("GitGrade AI – Repository Evaluation Report")
    y -= 20

    c.setFont("Helvetica", 12)

    draw_line(f"Project Name: {repo_data['name']}")
    draw_line(f"Primary Language: {repo_data['language']}")
    draw_line(f"Commits: {repo_data['commits']}")
    draw_line(f"Stars: {repo_data['stars']} | Forks: {repo_data['forks']}")
    y -= 10

    draw_line(f"GitGrade Score: {score} / 100")
    draw_line(f"Level: {level}")
    y -= 20

    draw_line("Summary:")
    draw_line(summary)
    y -= 15

    draw_line("Strengths:")
    for s in strengths:
        draw_line(f"- {s}")
    y -= 10

    draw_line("Areas for Improvement:")
    if weaknesses:
        for w in weaknesses:
            draw_line(f"- {w}")
    else:
        draw_line("- No major weaknesses detected.")
    y -= 10

    draw_line("Personalized Improvement Roadmap:")
    for i, step in enumerate(roadmap, 1):
        draw_line(f"{i}. {step}")

    c.save()
