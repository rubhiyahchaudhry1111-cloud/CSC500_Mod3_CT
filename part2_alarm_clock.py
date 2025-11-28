# Part 2: 24-Hour Alarm Clock

# Ask for current time in 24-hour format
current_time = int(input("Enter the current time (0-23): "))

# Ask how many hours to wait
hours_wait = int(input("Enter number of hours to wait for the alarm: "))

# Compute alarm time using modulo arithmetic
alarm_time = (current_time + hours_wait) % 24

# Display result
print(f"The alarm will go off at: {alarm_time}:00 hours")
