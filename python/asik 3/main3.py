import os
import csv
import json

# filemanager
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found.")
            return False

    def create_output_folder(self, folder='output'):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")


# dataloader
class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
        except Exception as e:
            print("Error loading file:", e)
        return self.students

    def preview(self, n=5):
        print("\nFirst rows:")
        print("-" * 30)
        for s in self.students[:n]:
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
        print("-" * 30)


# data analyser
class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        country_counts = {}

        for s in self.students:
            country = s['country']
            if country in country_counts:
                country_counts[country] += 1
            else:
                country_counts[country] = 1

        # top 3 countries
        top_3 = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]

        self.result = {
            "analysis": "Country Analysis",
            "total_students": len(self.students),
            "total_countries": len(country_counts),
            "top_3_countries": [
                {"country": c, "count": n} for c, n in top_3
            ],
            "all_countries": country_counts
        }

        return self.result

    def print_results(self):
        print("\nCountry Analysis")
        print("-" * 30)
        print("Total students :", self.result["total_students"])
        print("Total countries :", self.result["total_countries"])
        print("\nTop 3 Countries:")
        for i, c in enumerate(self.result["top_3_countries"], start=1):
            print(f"{i}. {c['country']} : {c['count']}")
        print("-" * 30)


# result saver
class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w') as f:
                json.dump(self.result, f, indent=4)
            print(f"Result saved to {self.output_path}")
        except Exception as e:
            print("Error saving file:", e)


# main
fm = FileManager('students.csv')

if not fm.check_file():
    print("Stopping program.")
    exit()

fm.create_output_folder()

dl = DataLoader('students.csv')
students = dl.load()
dl.preview()

# lambda / map / filter
print("\nLambda / Map / Filter")
print("-" * 30)

try:
    high_gpa = list(filter(lambda s: float(s['GPA']) > 3.5, students))
    print("Students with GPA > 3.5 :", len(high_gpa))

    gpa_values = list(map(lambda s: float(s['GPA']), students))
    print("GPA values (first 5) :", gpa_values[:5])

    good_attendance = list(filter(lambda s: float(s['class_attendance_percent']) > 90, students))
    print("Students attendance > 90% :", len(good_attendance))

except ValueError:
    print("Warning: Value conversion error in lambda section")

print("-" * 30)


# analysis
analyser = DataAnalyser(students)
analyser.analyse()
analyser.print_results()


# save
saver = ResultSaver(analyser.result, 'output/result.json')
saver.save_json()


# error test
print("\nTesting error handling:")
dl_wrong = DataLoader("wrong_file.csv")
dl_wrong.load()