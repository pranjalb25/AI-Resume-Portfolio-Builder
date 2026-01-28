def generate_portfolio_summary(skills, role="AI & ML Engineer"):
    if not skills:
        return "Aspiring professional with a strong interest in AI and data-driven technologies."

    skill_text = ", ".join(skills)

    summary = f"""
Aspiring {role} with hands-on experience in {skill_text}.
Skilled in developing intelligent solutions using data-driven and machine learning techniques.
Passionate about continuous learning and applying AI technologies to solve real-world problems.
    """
    return summary.strip()