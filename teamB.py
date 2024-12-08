with open("lab.txt", "r") as file:
    data = file.readlines()
    
name_line = data[0].strip()  
age_line = data[1].strip()  
grade_line = data[2].strip() 

name = name_line.split(": ")[1]
age = int(age_line.split(": ")[1])
grade = grade_line.split(": ")[1]

christian_year = 2024 - age
buddhist_year = christian_year + 543

if grade == "A":
    rank = "High Distinction"
elif grade in ["B+", "B"]:
    rank = "Distinction"
elif grade in ["C+", "C"]:
    rank = "Good"
elif grade in ["D+", "D"]:
    rank = "Normal"
else:
    rank = "Failed"

with open("teamB.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Buddhist Era: {buddhist_year}\n")
    file.write(f"Software Testing Rank: {rank}\n")
