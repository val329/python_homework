import pandas as pd

# Task 1

dictionary = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
}

task1_data_frame = pd.DataFrame(dictionary)             # create dataframe from dictionary
task1_with_salary = task1_data_frame.copy()         
task1_with_salary["Salary"] = [70000, 80000, 90000]     # add Salary column with values

task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1             # increment age of everyone by one

# write the new dataframe to a csv file
task1_older.to_csv("employees.csv", index=False, header=True, encoding=None)   

# Task 2

task2_employees = pd.read_csv('employees.csv')              # read employees from csv file
json_employees = pd.read_json('additional_employees.json')  # read additional employees from json file
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)    # combine all employees into one df

# Task 3

first_three = more_employees.head(3)
last_two = more_employees.tail(2)
employee_shape = more_employees.shape
print(more_employees.info())

# Task 4

dirty_data = pd.read_csv('dirty_data.csv')
clean_data = dirty_data.copy()

# Remove any duplicate rows from the DataFrame
clean_data = clean_data.drop_duplicates()

# Convert Age to numeric and handle missing values
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")

# Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data["Salary"] = clean_data["Salary"].replace("unknown", pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")

# Fill missing numeric values (use fillna). Fill Age with the mean and Salary with the median
mean_age = clean_data["Age"].mean()  
clean_data["Age"] = clean_data["Age"].fillna(mean_age)  
median_salary = clean_data["Salary"].median()
clean_data["Salary"] = clean_data["Salary"].fillna(median_salary)

# Convert Hire Date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], format='mixed', errors="coerce")

# Strip extra whitespace and standardize Name and Department as uppercase
clean_data["Department"] = clean_data["Department"].str.strip()
clean_data["Department"] = clean_data["Department"].str.upper()



