# Question 2: File I/O Operations

# 1. Write initial feedback list to feedback.txt
feedback_list = [
    "The Presenter Was Great But The Room Was Cold",
    "The Workshop Provided Clear And Useful Python Examples",
    "The Workshop Provided Clear And Useful Python Examples test task yosua",
    "The Hands On Coding Session Was Engaging And Interactive"
]

with open("feedback.txt", "w") as file:
    for item in feedback_list:
        file.write(item + "\n")

print("--- Initial Feedback Written to feedback.txt ---")

# 2. Read and print all feedback lines one by one
print("\n--- Reading feedback.txt ---")
with open("feedback.txt", "r") as file:
    for line in file:
        print(line.strip())

# 3. Append a new feedback message and display updated content
new_feedback = "The Pacing Was Perfect And The Material Was Well Explained"
with open("feedback.txt", "a") as file:
    file.write(new_feedback + "\n")

print("\n--- Updated Feedback After Appending ---")
with open("feedback.txt", "r") as file:
    for line in file:
        print(line.strip())