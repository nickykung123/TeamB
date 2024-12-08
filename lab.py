# Get data from Scanner
input_name = input("Name: ")
input_age = int(input("Christian Era: "))
input_score = int(input("Software testing score: "))

# Convert the data
year = 2024
age = year - input_age

grade = ""
if input_score >= 80:
    grade = "A"
elif input_score >= 75:
    grade = "B+"
elif input_score >= 70:
    grade = "B"
elif input_score >= 65:
    grade = "C+"
elif input_score >= 60:
    grade = "C"
elif input_score >= 55:
    grade = "D+"
elif input_score >= 50:
    grade = "D"
elif input_score < 50:
    grade = "F"

# Write the data to a file
with open("lab.txt", "w") as file:
    file.write(f"Name: {input_name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Software testing grade: {grade}\n")
