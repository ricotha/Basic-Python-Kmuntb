def main():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    temperatures = []
    for day in days:
        while True:
            try:
                temp = float(input(f"Enter temperature for {day}: "))
                if -50 <= temp <= 60:
                    break
                print("Temperature must be between -50°C and 60°C. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        temperatures.append((day, temp))

    print("\nDaily Temperatures:")
    for day, temp in temperatures:
        print(f"{day}: {temp}°C")

    total = sum(temp for day, temp in temperatures)
    average = total / len(temperatures)
    print(f"\nAverage temperature: {average:.2f}°C")

    max_temp = max(temp for day, temp in temperatures)
    min_temp = min(temp for day, temp in temperatures)

    hottest_days = [day for day, temp in temperatures if temp == max_temp]
    coolest_days = [day for day, temp in temperatures if temp == min_temp]

    print(f"Hottest day: {', '.join(hottest_days)}, {max_temp}°C")
    print(f"Coolest day: {', '.join(coolest_days)}, {min_temp}°C")

    print("\nDays above average:")
    for day, temp in temperatures:
        if temp > average:
            print(f"{day}: {temp}°C")

    sorted_temperatures = sorted(temperatures, key=lambda x: x[1], reverse=True)
    print("\nSorted by temperature (highest to lowest):")

    i = 0
    while i < len(sorted_temperatures):
        current_temp = sorted_temperatures[i][1]
        same_temp_days = [day for day, temp in sorted_temperatures if temp == current_temp]
        print(f"{', '.join(same_temp_days)}: {current_temp}°C")
        i += len(same_temp_days)

if __name__ == "__main__":
    main()