def main():
    """
    A program to analyze and report weekly temperature data.
    """
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    temperatures = []

    # Collect temperature for each day
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

    # Display daily temperatures
    print("\nDaily Temperatures:")
    for day, temp in temperatures:
        print(f"{day}: {temp}°C")

    # Calculate average temperature
    total = sum(temp for day, temp in temperatures)
    average = total / len(temperatures)
    print(f"\nAverage temperature: {average:.2f}°C")

    # Find hottest and coolest days (handling ties)
    max_temp = max(temp for day, temp in temperatures)
    min_temp = min(temp for day, temp in temperatures)

    hottest_days = [day for day, temp in temperatures if temp == max_temp]
    coolest_days = [day for day, temp in temperatures if temp == min_temp]

    print(f"Hottest day: {', '.join(hottest_days)}, {max_temp}°C")
    print(f"Coolest day: {', '.join(coolest_days)}, {min_temp}°C")

    # Show days that are above average
    print("\nDays above average:")
    for day, temp in temperatures:
        if temp > average:
            print(f"{day}: {temp}°C")

    # Sort and display temperatures from highest to lowest (grouping same temps)
    sorted_temperatures = sorted(temperatures, key=lambda x: x[1], reverse=True)
    print("\nSorted by temperature (highest to lowest):")

    i = 0
    while i < len(sorted_temperatures):
        current_temp = sorted_temperatures[i][1]
        # Group days that have the same temperature
        same_temp_days = [day for day, temp in sorted_temperatures if temp == current_temp]
        print(f"{', '.join(same_temp_days)}: {current_temp}°C")
        i += len(same_temp_days)

if __name__ == "__main__":
    main()
