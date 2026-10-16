# ==========================================
# Task / Question 4: String Manipulation with File I/O and Analytics
# ==========================================

keyword = "great"
total_feedback = 0
great_count = 0

# 1. Read feedback.txt and analyze contents
try:
    with open("feedback.txt", "r") as file:
        lines = file.readlines()
        total_feedback = len(lines)
        for line in lines:
            if keyword in line.lower():
                great_count += 1
except FileNotFoundError:
    print("feedback.txt not found for analysis.")

# 2. Write summary report to summary.txt
summary_content = f"=== Workshop Feedback Summary ===\nTotal Feedback: {total_feedback}\nMentions of 'Great': {great_count}\n"

with open("summary.txt", "w") as summary_file:
    summary_file.write(summary_content)

# 3. Formatted print statement on the console
print("--- Question 4 Output ---")
print(summary_content.strip())