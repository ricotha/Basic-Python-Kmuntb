# LAB 6-2 - Advanced File Handling "15 points"
# ITA PAI
# + Generate random score [40-100] for
# HANAPORS
# DONYAPO
# ENG, MATH, CP, SPORT and SCI to 1000 students and store this data to "scores.txt"
# WAAN + Transform score to grade and find grade avg :
# NED MITH
# 80-100 = A, store grade and grade avg to
# "grade.txt"

# LAB 6-2 - Advanced File Handling "15 points"
# ITA PAI
# + Generate random score [40-100] for
# HANAPORS
# DONYAPO
# ENG, MATH, CP, SPORT and SCI to 1000 students and store this data to "scores.txt"
# WAAN + Transform score to grade and find grade avg :
# NED MITH
# 80-100 = A, store grade and grade avg to
# "grade.txt"

import random

# Generate random scores [40-100] for ENG, MATH, CP, SPORT, and SCI to 1000 students
subjects = ['ENG', 'MATH', 'CP', 'SPORT', 'SCI']
students = 1000

# Store scores to "score.txt"
with open('score.txt', 'w') as f:
    for i in range(students):
        scores = [random.randint(40, 100) for _ in subjects]
        f.write(f"Student {i+1}: {dict(zip(subjects, scores))}\n")

# Transform score to grade and find grade average
def score_to_grade(score):
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

# Store grade and grade average to "grade.txt"
with open('score.txt', 'r') as f_in, open('grade.txt', 'w') as f_out:
    for line in f_in:
        parts = line.strip().split(': ', 1)  # limit to first ': ' only, so the dict's own ': ' isn't split too
        if len(parts) == 2:
            student_id = parts[0]
            scores_dict = eval(parts[1])
            grades = {subject: score_to_grade(score) for subject, score in scores_dict.items()}
            avg_score = sum(scores_dict.values()) / len(scores_dict)
            f_out.write(f"{student_id}: Grades={grades}, Average Score={avg_score:.2f}\n")