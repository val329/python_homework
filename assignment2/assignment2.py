import csv
import os
import custom_module
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)  # Assignment2 directory
CSV1_PATH = os.path.join(
    BASE_DIR, "..", "csv", "employees.csv"
)  # path to employees CSV file
CSV2_PATH = os.path.join(
    BASE_DIR, "..", "csv", "minutes1.csv"
)  # path to minutes1 CSV file
CSV3_PATH = os.path.join(
    BASE_DIR, "..", "csv", "minutes2.csv"
)  # path to minutes2 CSV file


# Task 2
# Reads an employees.csv file and returns a dictionary with first row as row header
# (key = fields) and all the rows (key = rows)
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


# {"fields": list of headers, "rows": list of rows }
employees = read_employees()
# print(employees)


# Task 3
# Returns the index by column header string
def column_index(header):
    # headers = employees["fields"]
    return employees["fields"].index(header)


employee_id_column = column_index("employee_id")
# print(employee_id_column)


# Task 4
# Returns an employee first name by row number from employees dictionary
def first_name(row):
    col = column_index("first_name")
    rows = employees["rows"]

    return rows[row][col]


# print(first_name(2))


# Task 5
# Returns rows of employees by employee ID
def employee_find(employee_id):

    # Returns True if there's a match in the rows given employee_id
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    # Filters out all rows that do not match
    matches = list(filter(employee_match, employees["rows"]))
    return matches


# print(employee_find(5))


# Task 6
# Returns rows of employees by employee ID using lambda function
def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]
        )
    )
    return matches


# print(employee_find2(5))


# Task 7
# Sorts employee dictionary by last name (no return)
def sort_by_last_name():
    col = column_index("last_name")
    employees["rows"].sort(key=(lambda row: row[col]))

    return employees["rows"]


sort_by_last_name()
# print(employees)


# Task 8
# Given a row from employees list, returns a dictionary with values mapped to corresponding hearders
# excluding the first column employee_id
def employee_dict(row):
    dictionary = dict(zip(employees["fields"][1:], row[1:]))
    return dictionary


# print(employee_dict(["20", "Thomas", "Calderon", "+64 +1-380-200-3211"]))


# Task 9
# Returns a dictionary of employee dictionaries with employee_id as keys
def all_employees_dict():

    all_emp = {}
    for row in employees["rows"]:
        keys = row[0]
        values = employee_dict(row)
        all_emp[keys] = values

    return all_emp


# print(all_employees_dict())


# Task 10
# Retrieves value from environmental variable THISVALUE. To set the value in terminal:
# export THISVALUE=ABC
def get_this_value():
    return os.getenv("THISVALUE")


# print(get_this_value())


# Task 11
# Stores the secret value in a custom module global variable
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)


set_that_secret("Shhhhhh!")
# print(custom_module.secret)


# Task 12
# Given the filepath, reads the file and stores the data into dictionaries
def read_csv(filepath):
    dictionary = dict()
    list_of_rows = []
    try:
        with open(filepath, "r") as file:
            reader = csv.reader(file)

            for i, row in enumerate(reader):
                if i == 0:
                    dictionary["fields"] = row
                else:
                    list_of_rows.append(tuple(row))
            dictionary["rows"] = list_of_rows
            return dictionary

    except Exception as e:
        print(f"An error occurred reading the file: {e}")
    else:
        print("The file was read ok.")


# # Creates two dicts, minutes1 and minutes2, by reading ../csv/minutes1.csv and ../csv/minutes2.csv.
def read_minutes():
    file1 = read_csv(CSV2_PATH)
    file2 = read_csv(CSV3_PATH)

    return file1, file2


minutes1, minutes2 = read_minutes()
custom_module.set_minutes(minutes1, minutes2)


# Task 13
# Creates two sets out of minutes1 and minutes2 dictionaries and combines them into
# one minutes_set, storing it in a global variable
def create_minutes_set():
    minutes_set = set(minutes1["rows"]).union(set(minutes2["rows"]))
    return minutes_set


minutes_set = create_minutes_set()
custom_module.minutes_set_variable(minutes_set)


# Task 14
# Converts strings of data into datetime
def create_minutes_list():
    minutes_list = list(minutes_set)
    minutes_tuple = list(
        map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list)
    )

    return minutes_tuple


minutes_list = create_minutes_list()
custom_module.minutes_list_variable(minutes_list)

# print(create_minutes_list())
# ('Gina Maldonado', 'February 13, 1987')


# Task 15
# Sorting minutes_list in ascending order of datetime, printing the data to minutes.csv file
def write_sorted_list():
    minutes_list.sort(
        key=lambda x: x[1]
    )  # sorting by the second element of minutes_list
    sorted_list = list(
        map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list)
    )  # converting datetime to string

    # printing to minutes.csv file
    try:
        with open("./minutes.csv", "a") as file:

            headers = minutes1["fields"]
            file.write(f"{headers} \n")

            for line in sorted_list:
                file.write(f"{line} \n")

    except Exception as e:
        print(f"An exception occured. {e}")

    return sorted_list


write_sorted_list()
# print(minutes_list)
