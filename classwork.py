# """
# Module 5 classwork:
# A simple example of saving and loading a student record with JSON.
# """

# import json
# import os
# from datetime import datetime
# from pathlib import Path

# # Keep the JSON file in the same folder as this Python file.
# folder = Path(__file__).parent
# file_path = folder / "student.json"

# # A small student record, like information a school might keep.
# student = {
#     "name": "Ada",
#     "course": "Python",
#     "score": 85,
#     "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# }

# # 1. Save the Python dictionary into a JSON file.
# with open(file_path, "w", encoding="utf-8") as file:
#     json.dump(student, file, indent=4)

# print("Student record saved.")

# # 2. Read the JSON file and turn its contents back into Python data.
# try:
#     with open(file_path, "r", encoding="utf-8") as file:
#         saved_student = json.load(file)

#     print("\nHere is the record we loaded:")
#     print("Name:", saved_student["name"])
#     print("Course:", saved_student["course"])
#     print("Score:", saved_student["score"])
#     print("Last updated:", saved_student["last_updated"])

# except FileNotFoundError:
#     print("Sorry, the student file could not be found.")

# # 3. A small example of checking a computer setting.
# # If this setting is not present, Python uses the word "not set".
# school_name = os.environ.get("SCHOOL_NAME", "not set")
# print("\nSCHOOL_NAME environment setting:", school_name)

# # 4. pathlib can check whether the file is there.
# print("Does student.json exist?", file_path.exists())

# The idea: call that is calling an API
from datetime import datetime 
import os
from pathlib import Path
current_date = datetime.now()
print(f"\n     the date is{current_date}")


user_name = os.getenv("USERNAME")
print(user_name)

print(os.getenv("COMPUTERNAME"))

print(os.getenv("USERPROFILE"))

file = Path("main.py")
print(file.exists())


# finally how i understand json.load and json.dump







