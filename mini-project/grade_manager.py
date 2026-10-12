"""
Student Grade Manager
Python Mini Project
"""

# =====================================================
# Data structures
# =====================================================
SUBJECTS = ["Python", "Math", "Law", "English", "Finance"]  # list

GRADE_POINTS = {"A": 4.0, "B+": 3.5, "B": 3.0, "C+": 2.5,
                "C": 2.0, "D+": 1.5, "D": 1.0, "F": 0.0}            # dict

FILE_NAME = "students.txt"

DEBUG = False   # change to True to see debug messages


# =====================================================
# Debugging helper
# =====================================================
def debug(message):
    """Print a message only when DEBUG is True."""
    if DEBUG:
        print("[DEBUG]", message)


# =====================================================
# Function: score -> grade
# =====================================================
def score_to_grade(score):
    """Convert a score (0-100) to a letter grade."""
    if score >= 80:
        return "A"
    elif score >= 75:
        return "B+"
    elif score >= 70:
        return "B"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 55:
        return "D+"
    elif score >= 50:
        return "D"
    else:
        return "F"


# =====================================================
# Object-Oriented Programming: Student class
# =====================================================
class Student:
    def __init__(self, student_id, name, scores):
        self.student_id = student_id   # text, e.g. "001"
        self.name = name               # text, e.g. "RICO"
        self.scores = scores           # list of 5 numbers

    def average(self):
        """Average of all scores."""
        return sum(self.scores) / len(self.scores)

    def grade(self):
        """Letter grade from the average."""
        return score_to_grade(self.average())

    def gpa(self):
        """GPA = average of grade points (all subjects have equal credit)."""
        total = 0
        for score in self.scores:
            total += GRADE_POINTS[score_to_grade(score)]
        return total / len(self.scores)

    def show_card(self):
        """Draw the report card."""
        border = "+" + "-" * 30 + "+"    # top and bottom line
        divider = "|" + "-" * 30 + "|"   # line between sections
        print(border)
        print("|" + "REPORT CARD".center(30) + "|")
        print(divider)
        print("| Full Name : " + self.name.ljust(22) + "|")
        print("| Student ID   : " + self.student_id.ljust(22) + "|")
        print(divider)
        for i in range(len(SUBJECTS)):
            text = f" {SUBJECTS[i]:<12}{self.scores[i]:>5}{score_to_grade(self.scores[i]):>8}"
            print("|" + text.ljust(30) + "|")
        print(divider)
        print("|" + f" Average : {self.average():.2f}".ljust(30) + "|")
        print("|" + f" GPA     : {self.gpa():.2f}".ljust(30) + "|")
        print("|" + f" Result  : {self.grade()}".ljust(30) + "|")
        print(border)

    def to_line(self):
        """Make one line of text to save in the file."""
        text = self.student_id + "," + self.name
        for score in self.scores:
            text = text + "," + str(score)
        return text


# =====================================================
# File handling
# =====================================================
def save_students(students):
    """Write all students to the file (one student per line)."""
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(student.to_line() + "\n")
    debug("Saved " + str(len(students)) + " students")


def load_students():
    """Read students from the file. Return a list of Student objects."""
    students = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")          # ["001", "RICO", "88", ...]
                scores = []
                for text in parts[2:]:
                    scores.append(int(text))
                students.append(Student(parts[0], parts[1], scores))
        print("Loaded", len(students), "student(s) from", FILE_NAME)
    except FileNotFoundError:
        print("No saved file yet. Starting with an empty list.")
    except ValueError:
        print("The file has wrong data. Some students were not loaded.")
    debug("Loaded list: " + str(len(students)))
    return students


# =====================================================
# Input functions with error handling
# =====================================================
def get_score(prompt):
    """Ask until the user types a score from 0 to 100."""
    while True:
        try:
            score = int(input(prompt))
            if 0 <= score <= 100:
                return score
            print("  Score must be between 0 and 100.")
        except ValueError:
            print("  Please type a number (not letters).")


def ask_yes_no(prompt):
    """Ask until the user types y or n. Return True for y, False for n."""
    while True:
        answer = input(prompt).strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        print("  Please type y or n.")


def find_student(students, student_id):
    """Return the Student with this ID, or None if not found."""
    for student in students:
        if student.student_id == student_id:
            return student
    return None


# =====================================================
# Menu functions
# =====================================================
def add_student(students):
    print("\n--- Add Student ---")
    count = 0   # how many students were added in this round
    question = "Add student? (y/n): "

    while True:
        # y = add a student, n = exit option 1 and go back to the menu
        if not ask_yes_no("\n" + question):
            break

        student_id = input("Student ID: ").strip()
        if student_id == "":
            print("ID cannot be empty.")
            continue
        if find_student(students, student_id) is not None:
            print("This ID already exists.")
            continue

        name = input("Student name: ").strip().upper().replace(",", " ")
        if name == "":
            print("Name cannot be empty.")
            continue

        scores = []
        for subject in SUBJECTS:
            scores.append(get_score(subject + " score (0-100): "))

        new_student = Student(student_id, name, scores)
        students.append(new_student)
        save_students(students)
        count += 1
        print("Student added!")
        new_student.show_card()

        question = "Add more student? (y/n): "   # next time the question changes

    print("Finished adding. Total added:", count)


def show_all(students):
    print("\n--- All Students ---")
    if len(students) == 0:
        print("No students yet.")
        return
    for student in students:
        student.show_card()


def edit_student(students):
    print("\n--- Edit Scores ---")
    student = find_student(students, input("Student ID to edit: ").strip())
    if student is None:
        print("Student not found.")
        return

    student.show_card()
    print("Press Enter to keep the old score.")
    for i in range(len(SUBJECTS)):
        text = input(f"{SUBJECTS[i]} [{student.scores[i]}]: ").strip()
        if text == "":
            continue
        try:
            new_score = int(text)
            if 0 <= new_score <= 100:
                student.scores[i] = new_score
            else:
                print("  Must be 0-100. Kept old score.")
        except ValueError:
            print("  Not a number. Kept old score.")

    save_students(students)
    print("Scores updated!")
    student.show_card()


def delete_student(students):
    print("\n--- Delete Student ---")
    student = find_student(students, input("Student ID to delete: ").strip())
    if student is None:
        print("Student not found.")
        return

    student.show_card()
    sure = input("Delete this student? (y/n): ").strip().lower()
    if sure == "y":
        students.remove(student)
        save_students(students)
        print("Student deleted.")
    else:
        print("Cancelled.")


def search_student(students):
    print("\n--- Search Student ---")
    keyword = input("Search by name or ID: ").strip().lower()
    if keyword == "":
        print("Please type a name or ID.")
        return

    found = False
    for student in students:
        if keyword in student.name.lower() or keyword in student.student_id.lower():
            student.show_card()
            found = True
    if not found:
        print("No student found.")


def show_top_student(students):
    print("\n--- Top Student ---")
    if len(students) == 0:
        print("No students yet.")
        return
    best = students[0]
    for student in students:
        if student.average() > best.average():
            best = student
    best.show_card()


# =====================================================
# Main program
# =====================================================
def main():
    students = load_students()

    while True:
        print("\n===== STUDENT GRADE MANAGER =====")
        print("1. Add student")
        print("2. Show all report cards")
        print("3. Edit scores")
        print("4. Delete student")
        print("5. Search student")
        print("6. Top student")
        print("0. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_all(students)
        elif choice == "3":
            edit_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            search_student(students)
        elif choice == "6":
            show_top_student(students)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()