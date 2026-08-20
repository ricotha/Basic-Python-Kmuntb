def main():
    student = {}
    student["student_id"] = input("Enter student ID: ")
    student["name"] = input("Enter name: ")
    student["major"] = input("Enter major: ")

    scores = []
    for i in range(3):
        while True:
            try:
                score = int(input(f"Enter score {i + 1}: "))
                if 0 <= score <= 100:
                    break
                print("Score must be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        scores.append(score)

    student["scores"] = scores
    total = sum(scores)
    average = total / len(scores)
    student["average"] = average
    if average >= 80:
        student["grade"] = "A"
    elif average >= 75:
        student["grade"] = "B+"
    elif average >= 70:
        student["grade"] = "B"
    elif average >= 65:
        student["grade"] = "C+"
    elif average >= 60:
        student["grade"] = "C"
    elif average >= 55:
        student["grade"] = "D+"
    elif average >= 50:
        student["grade"] = "D"
    else:
        student["grade"] = "F"

    print(f"Student ID: {student['student_id']}")
    print(f"Name: {student['name']}")
    print(f"Major: {student['major']}")
    print(f"Scores: {scores[0]}, {scores[1]}, {scores[2]}")
    print(f"Average: {student['average']:.2f}")
    print(f"Grade: {student['grade']}")

if __name__ == "__main__":
    main()