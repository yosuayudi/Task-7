# ==========================================
# Task / Question 3: Exception Handling in File Operations
# ==========================================

print("--- Question 3 Output ---")
try:
    with open("feedback.txt", "r") as file:
        print("Attempting to Read Feedback File...")
        content = file.read()
        print(content)
        
except FileNotFoundError:
    print("File not found. Please create feedback.txt first.")
    
except PermissionError:
    print("Permission denied. Close the file and try again.")
    
finally:
    print("Operation completed.")