days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temperatures = []

for day in days:
    temp = float(input(f"Enter temperature for {day}: "))
    temperatures.append((day, temp))

print("\nDaily Temperatures:")
for day, temp in temperatures:
    print(f"{day}: {temp}°C")

total = 0
for day, temp in temperatures:
    total += temp
average = total / len(temperatures)
print(f"\nAverage temperature: {average:.2f}°C")

hottest = temperatures[0]
coolest = temperatures[0]
for day, temp in temperatures:
    if temp > hottest[1]:
        hottest = (day, temp)
    if temp < coolest[1]:
        coolest = (day, temp)
print(f"Hottest day: {hottest[0]}, {hottest[1]}°C")
print(f"Coolest day: {coolest[0]}, {coolest[1]}°C")

print("\nDays above average:")
for day, temp in temperatures:
    if temp > average:
        print(f"{day}: {temp}°C")

sorted_temperatures = sorted(temperatures, key=lambda x: x[1], reverse=True)
print("\nSorted by temperature (highest to lowest):")
for day, temp in sorted_temperatures:
    print(f"{day}: {temp}°C")
