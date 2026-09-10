# LAB 6-2 - Advanced File Handling "15 points"
# + Generate random score [40-100] for ENG, MATH, CP, SPORT and SCI
#   to 1000 students and store this data to "scores.txt"
# + Transform score to grade and find grade avg:
#   80-100 = A, store grade and grade avg to "grade.txt"

import random
import sys
from ast import literal_eval

subjects = ['ENG', 'MATH', 'CP', 'SPORT', 'SCI']
students = 1000

# Part 1: generate random scores [40-100] for 1000 students -> "scores.txt"
try:
    with open('scores.txt', 'w') as f:
        for i in range(1, students + 1):
            scores = {subject: random.randint(40, 100) for subject in subjects}
            f.write(f"Student {i}: {scores}\n")
    print(f"Successfully generated scores for {students} students in 'scores.txt'")
except PermissionError:
    print("Error: Permission denied. Cannot write to 'scores.txt'.")
    sys.exit(1)
except OSError as e:
    print(f"Error: Could not write to 'scores.txt': {e}")
    sys.exit(1)

# Part 2: transform score to grade (Thai grading scale)
def score_to_grade(score):
    if score >= 80:
        return 'A'
    elif score >= 75:
        return 'B+'
    elif score >= 70:
        return 'B'
    elif score >= 65:
        return 'C+'
    elif score >= 60:
        return 'C'
    elif score >= 55:
        return 'D+'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

def grade_to_gpa(grade):
    gpa_map = {
        'A': 4.0, 'B+': 3.5, 'B': 3.0,
        'C+': 2.5, 'C': 2.0, 'D+': 1.5,
        'D': 1.0, 'F': 0.0
    }
    return gpa_map.get(grade, 0.0)

def round_to_thai_gpa(gpa):
    # Snap to nearest valid Thai GPA: 0, 1, 1.5, 2, 2.5, 3, 3.5, 4
    valid = [0.0, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    return min(valid, key=lambda v: abs(v - gpa))

# Read "scores.txt", transform each score to a grade,
# find the average score, convert to average grade, and store everything in "grade.txt" in column format
try:
    with open('scores.txt', 'r') as f_in, open('grade.txt', 'w') as f_out:
        # Write header
        f_out.write(f"{'Student':<10}{'ENG':<8}{'MATH':<8}{'CP':<8}{'SPORT':<8}{'SCI':<8}{'AVG':<8}\n")
        f_out.write('-' * 58 + '\n')

        skipped = 0
        for line_num, line in enumerate(f_in, 1):
            try:
                student_id, scores_str = line.strip().split(': ', 1)
                scores = literal_eval(scores_str)

                # Validate that scores is a dict with the expected subjects
                if not isinstance(scores, dict):
                    raise ValueError(f"Expected dict, got {type(scores).__name__}")
                for subject in subjects:
                    if subject not in scores:
                        raise KeyError(f"Missing subject '{subject}'")
                    if not isinstance(scores[subject], (int, float)):
                        raise TypeError(f"Score for '{subject}' must be a number, got {type(scores[subject]).__name__}")

                grades = {subject: score_to_grade(score) for subject, score in scores.items()}
                gpas = [grade_to_gpa(grade) for grade in grades.values()]
                avg_gpa = sum(gpas) / len(gpas)
                avg_gpa = round_to_thai_gpa(avg_gpa)

                # Extract student number for cleaner display
                student_num = student_id.split()[1]
                f_out.write(f"{student_num:<10}{grades['ENG']:<8}{grades['MATH']:<8}{grades['CP']:<8}{grades['SPORT']:<8}{grades['SCI']:<8}{avg_gpa:<8.1f}\n")

            except (ValueError, KeyError, TypeError, SyntaxError) as e:
                print(f"Warning: Skipping invalid data on line {line_num}: {e}")
                skipped += 1
                continue

        if skipped > 0:
            print(f"Warning: {skipped} line(s) were skipped due to errors.")
        print(f"Successfully wrote grades to 'grade.txt'")

except FileNotFoundError:
    print("Error: 'scores.txt' not found. Please generate scores first.")
    sys.exit(1)
except PermissionError:
    print("Error: Permission denied. Cannot read 'scores.txt' or write 'grade.txt'.")
    sys.exit(1)
except OSError as e:
    print(f"Error: File I/O error: {e}")
    sys.exit(1)

# Print the contents of "grade.txt"
try:
    print("\nGrades stored in grade.txt:")
    with open('grade.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("Error: 'grade.txt' not found.")
except PermissionError:
    print("Error: Permission denied. Cannot read 'grade.txt'.")
except OSError as e:
    print(f"Error: Could not read 'grade.txt': {e}")