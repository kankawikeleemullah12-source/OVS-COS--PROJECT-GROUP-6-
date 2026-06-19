import csv

def run_dictionary_pipeline():
    # Initialize a dynamic dictionary mapper for the 5 courses
    metrics = {
        "CHM102": 0,
        "CHM108": 0,
        "BIO102": 0,
        "BIO108": 0,
        "COS102": 0
    }
counter = 0

    with open("grades.csv", "r") as data_source:
        parsed_records = csv.DictReader(
            data_source,
            skipinitialspace=True
        )
