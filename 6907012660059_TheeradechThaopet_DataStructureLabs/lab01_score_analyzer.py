def main():
    """
    A program to analyze a set of student scores.
    """
    scores = []

    # Collect 5 scores from the user with validation
    for i in range(5):
        while True:
            try:
                score = int(input(f"Enter score {i + 1}: "))
                if 0 <= score <= 100:
                    break
                print("Score must be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        scores.append(score)

    # Calculate statistics
    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)
    passed = sum(1 for score in scores if score >= 50)

    # Display the results
    print("\n--- Score Analysis ---")
    print(f"All scores: {scores}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
    print(f"Number of students who passed (>= 50): {passed}")

if __name__ == "__main__":
    main()
