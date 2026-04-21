# Task 3
# Add code that reads the contents of ../csv/employees.csv into a list of lists using the csv module.
import csv
import os

BASE_DIR = os.path.dirname(__file__)  # Assignment2 directory
CSV1_PATH = os.path.join(
    BASE_DIR, "..", "csv", "employees.csv"
)  # path to employees CSV file


def read_employees():
    dictionary = dict()
    list_of_rows = []
    try:
        with open(CSV1_PATH, "r") as file:
            reader = csv.reader(file)

            for i, row in enumerate(reader):
                if i == 0:
                    dictionary["fields"] = row
                else:
                    list_of_rows.append(row)
            dictionary["rows"] = list_of_rows
            return dictionary

    except Exception as e:
        print(f"An error occurred reading the file: {e}")
    else:
        print("The file was read ok.")


employees = read_employees()

# List of employees, first_name space last_name
full_name = [f"{row[1]} {row[2]}" for row in employees["rows"]]
print(full_name)

e_names = [word for word in full_name if "e" in word]
print(e_names)
