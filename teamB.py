import unittest

def process_student_data(file_content):
    try:
        data = file_content.split("\n")
        if len(data) < 3:
            raise ValueError("The file does not contain enough information (name, age, and grade are required).")

        name_line = data[0].strip()  
        age_line = data[1].strip()  
        grade_line = data[2].strip() 

        if len(name_line.split(": ")) < 2 or len(age_line.split(": ")) < 2 or len(grade_line.split(": ")) < 2:
            raise ValueError("One or more fields (name, age, grade) are missing.")

        name = name_line.split(": ")[1]
        
        try:
            age = int(age_line.split(": ")[1])
        except ValueError:
            raise ValueError("Age must be an integer.")
        
        grade = grade_line.split(": ")[1]

        valid_grades = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
        if grade not in valid_grades:
            raise ValueError(f"Grade must be one of {valid_grades}.")

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

        print(f"Name: {name}")
        print(f"Buddhist Era: {buddhist_year}")
        print(f"Software Testing Rank: {rank}")

        return name, buddhist_year, rank
    except (ValueError, IndexError) as e:
        return {"error": str(e)}


class TestStudentDataProcessing(unittest.TestCase):

    def test_correct_data(self):
        file_content = "Name: nicky\nAge: 20\nGrade: A"
        result = process_student_data(file_content)
        self.assertEqual(result, ("nicky", 2547, "High Distinction"))

    def test_missing_data(self):
        file_content = "Name: nicky\nAge: 20"
        result = process_student_data(file_content)
        self.assertTrue("error" in result)
        self.assertIn("The file does not contain enough information", result["error"])

    def test_missing_fields(self):
        file_content = "Name: nicky\nAge: \nGrade: A"
        result = process_student_data(file_content)
        self.assertTrue("error" in result)
        self.assertIn("One or more fields", result["error"])

    def test_invalid_age(self):
        file_content = "Name: nicky\nAge: ABC\nGrade: A"
        result = process_student_data(file_content)
        self.assertTrue("error" in result)
        self.assertIn("Age must be an integer", result["error"])

    def test_invalid_grade(self):
        file_content = "Name: nicky\nAge: 20\nGrade: Z"
        result = process_student_data(file_content)
        self.assertTrue("error" in result)
        self.assertIn("Grade must be one of", result["error"])

    def test_missing_colon_in_name(self):
        file_content = "Name nicky\nAge: 20\nGrade: A"
        result = process_student_data(file_content)
        self.assertTrue("error" in result)
        self.assertIn("One or more fields", result["error"])

    def test_missing_colon_in_age(self):
        file_content = "Name: nicky\nAge 20\nGrade: A"
        result = process_student_data(file_content)
        self.assertTrue("error" in result)
        self.assertIn("One or more fields", result["error"])


if __name__ == '__main__':
    unittest.main()
