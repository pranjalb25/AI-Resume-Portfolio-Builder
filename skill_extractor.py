SKILLS = ["python", "machine learning", "nlp", "sql", "deep learning", "data analysis"]

def extract_skills(text):
    return [skill for skill in SKILLS if skill in text.lower()]