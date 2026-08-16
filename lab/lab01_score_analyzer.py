Score = []
for i in range(5):
    score = int(input("Enter score {}: ".format(i + 1)))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100. Please try again.")
        score = int(input("Enter score {}: ".format(i + 1)))
    Score.append(score)

print("All scores:", Score)
total = sum(Score)
average = total / len(Score)
highest = max(Score)
lowest = min(Score)
passed = sum(1 for score in Score if score >= 50)

print("Total:", total)
print("Average: {:.2f}".format(average))
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Number of students who passed:", passed)