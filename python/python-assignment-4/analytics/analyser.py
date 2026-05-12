class DataAnalyser:

    def __init__(self, students):

        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented.")

    def print_results(self):

        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: {len(self.students)} students"


class CountryAnalyser(DataAnalyser):

    def __init__(self, students):
        super().__init__(students)

    def analyse(self):

        countries = {}

        for s in self.students:

            country = s["country"]

            if country in countries:
                countries[country] += 1
            else:
                countries[country] = 1

        top_3 = sorted(
            countries.items(),
            key=lambda x: x[1],
            reverse=True
        )[:3]

        self.result = {
            "total_students": len(self.students),
            "total_countries": len(countries),
            "top_3": top_3,
            "all_countries": countries
        }

        return self.result

    def print_results(self):

        print("\n" + "=" * 40)
        print("COUNTRY ANALYSIS REPORT")
        print("=" * 40)

        super().print_results()

        print("=" * 40)

    def __str__(self):
        return f"CountryAnalyser: {len(self.students)} students"