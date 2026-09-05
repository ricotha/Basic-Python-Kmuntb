# LAB 6-2 - Advanced File Handling "15 points"
# + Generate random score [40-100] for ENG, MATH, CP, SPORT and SCI
#   to 1000 students and store this data to "scores.txt"
# + Transform score to grade and find grade avg:
#   80-100 = A, store grade and grade avg to "grade.txt"

import random
from ast import literal_eval

subjects = ['ENG', 'MATH', 'CP', 'SPORT', 'SCI']
students = 1000

# Part 1: generate random scores [40-100] for 1000 students -> "scores.txt"
with open('scores.txt', 'w') as f:
    for i in range(1, students + 1):
        scores = {subject: random.randint(40, 100) for subject in subjects}
        f.write(f"Student {i}: {scores}\n")

# Part 2: transform score to grade
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

# Read "scores.txt", transform each score to a grade,
# find the average score, convert to average grade, and store everything in "grade.txt" in column format
with open('scores.txt', 'r') as f_in, open('grade.txt', 'w') as f_out:
    # Write header
    f_out.write(f"{'Student':<10}{'ENG':<8}{'MATH':<8}{'CP':<8}{'SPORT':<8}{'SCI':<8}{'AVG':<8}\n")
    f_out.write('-' * 58 + '\n')
    
    for line in f_in:
        student_id, scores_str = line.strip().split(': ', 1)
        scores = literal_eval(scores_str)
        grades = {subject: score_to_grade(score) for subject, score in scores.items()}
        avg_score = sum(scores.values()) / len(scores)
        avg_grade = score_to_grade(avg_score)
        
        # Extract student number for cleaner display
        student_num = student_id.split()[1]
        f_out.write(f"{student_num:<10}{grades['ENG']:<8}{grades['MATH']:<8}{grades['CP']:<8}{grades['SPORT']:<8}{grades['SCI']:<8}{avg_grade:<8}\n")

# Print the contents of "grade.txt"
print("\nGrades stored in grade.txt:")
with open('grade.txt', 'r') as f:
    print(f.read())