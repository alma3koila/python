from analytics import (
    FileManager,
    DataLoader,
    ResultSaver,
    Report
)

from analytics.analyser import CountryAnalyser


def main():
    file_name = "students.csv"

    #праверка файлов
    fm = FileManager(file_name)

    if not fm.check_file():
        print("Program stopped.")
        return

    fm.create_output_folder()

    # выгрузка даты
    loader = DataLoader(file_name)
    students = loader.load()

    if not students:
        print("No data loaded.")
        return

    loader.preview()

    # lambdafilter
    print("\nStudents with GPA > 3.5")

    try:
        high_gpa = list(
            filter(lambda s: float(s["GPA"]) > 3.5, students)
        )

        print("Count:", len(high_gpa))

    except ValueError:
        print("Error while converting GPA values")

    # analyser
    analyser = CountryAnalyser(students)

    # сахран
    saver = ResultSaver(
        analyser.result,
        "output/result.json"
    )

    # репорт
    report = Report(analyser, saver)
    report.generate()

    # с асика полиморф
    print("\nRunning analysers:")
    print("-" * 40)

    analysers = [
        CountryAnalyser(students),
        CountryAnalyser(students[:10])
    ]

    for a in analysers:
        print(a)
        a.analyse()
        a.print_results()


if __name__ == "__main__":
    main()