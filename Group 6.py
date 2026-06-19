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
        parsed_records = csv.DictReader(data_source)
        for entry in parsed_records:
            # Dynamically add scores to each course match
            for course in metrics:
                metrics[course] += int(entry[course])
            counter += 1
            
    with open("report.txt", "w") as log:
        log.write("============ STUDENT PERFORMANCE REPORT ============\n")
        log.write(f"Total Students Processed: {counter}\n\n")
        
        # Loop through the map to calculate and write averages automatically
        for course, aggregated_sum in metrics.items():
            computed_average = aggregated_sum / counter
            log.write(f"Average {course} Score: {computed_average:.2f}\n")
            
        log.write("====================================================\n")

run_dictionary_pipeline()
print("Report successfully generated as 'report.txt'!")

print("\n--- Displaying Generated Report ---")
with open("report.txt") as file_reader:
    print(file_reader.read())
