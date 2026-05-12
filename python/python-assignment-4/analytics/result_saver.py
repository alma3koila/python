import json


class ResultSaver:

    def __init__(self, result, output_path):

        self.result = result
        self.output_path = output_path

    def save_json(self):

        try:
            with open(self.output_path, "w") as file:

                json.dump(
                    self.result,
                    file,
                    indent=4
                )

            print("Result saved.")

        except Exception as e:
            print("Saving error:", e)