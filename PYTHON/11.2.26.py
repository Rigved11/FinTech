marks = [78, 85, 90, 66, 72]

# Initialize counters
distinction_count = 0
fail_count = 0

# Loop through marks and apply logic
for m in marks:
    if m >= 75:
        distinction_count += 1
    elif m < 40:
        fail_count += 1

# Print results
print(f"Students with >= 75 marks: {distinction_count}")
print(f"Students who failed (< 40 marks): {fail_count}")