# Question 1: String Manipulation
raw_feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "

# Step 1: Remove leading/trailing spaces and convert to lowercase
step1 = raw_feedback.strip().lower()

# Step 2: Replace 'speaker' with 'presenter' and remove extra internal spaces
step2 = step1.replace("speaker", "presenter")
standardized_text = " ".join(step2.split())

# Step 3: Convert to title case and display using an f-string
final_cleaned_text = standardized_text.title()

print(f"Original Text: '{raw_feedback}'")
print(f"Cleaned Text : '{final_cleaned_text}'")