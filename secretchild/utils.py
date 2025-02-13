import csv
import random
import io


def read_csv(file):

    employees = []
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.reader(decoded_file)
    next(reader)
    for row in reader:
        employees.append((row[0], row[1]))
    return employees

def read_previous_assignments(file):

    previous_assignments = {}
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.reader(decoded_file)
    next(reader)
    for row in reader:
        previous_assignments[row[1]] = row[3]
    return previous_assignments

def assign_secret_santa(employees, previous_assignments):

    assignments = {}
    available = employees[:]
    random.shuffle(available)

    for emp_name, emp_email in employees:
        choices = [e for e in available if e[1] != emp_email and e[1] != previous_assignments.get(emp_email)]

        if not choices:
            return None

        secret_child = random.choice(choices)
        available.remove(secret_child)
        assignments[emp_email] = secret_child

    return assignments

def generate_output_csv(assignments):
    
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"])

    for emp_email, (child_name, child_email) in assignments.items():
        writer.writerow([emp_email, emp_email, child_name, child_email])

    output.seek(0)
    return output
