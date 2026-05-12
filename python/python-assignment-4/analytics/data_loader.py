import csv


class DataLoader:

    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):

        print("Loading CSV data...")

        try:
            with open(self.filename, encoding="utf-8") as file:

                reader = csv.DictReader(file)
                self.students = list(reader)

            print(f"{len(self.students)} rows loaded.")

        except FileNotFoundError:
            print("CSV file not found.")

        except Exception as e:
            print("Loading error:", e)

        return self.students

    def preview(self, rows=5):

        print("\nPreview:")
        print("-" * 40)

        for s in self.students[:rows]:

            print(
                s["student_id"],
                s["country"],
                s["GPA"]
            )

        print("-" * 40)