import csv

class DataLoader:
    def __init__(self):
        self.data = None

    def load_data(self, file_path):
        try:
            with open(file_path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                self.data = list(csv_reader)
                print("\n\t\t\t[+] Data loaded successfully.")
        except FileNotFoundError:
            print(f"\n\t\t\t[x] '{file_path}': No such file or directory (OS error 2)")
        except PermissionError:
            print(f"\n\t\t\t[x] '{file_path}': Permission denied (OS error 13)")

class DataRetriever:
    def __init__(self, data):
        self.data = data

    def total_records(self):
        if self.data:
            return len(self.data)
        else:
            return 0

    def unique_departments(self):
        if self.data:
            departments = set(record['Department'] for record in self.data)
            return list(departments)
        else:
            return []

    def retrieve_employee_by_id(self, employee_id):
        if self.data:
            for record in self.data:
                if int(record['EmployeeID']) == employee_id:
                    return record
            print(f"\n\t\t\t[!] No employee found with ID '{employee_id}'")
            return None
        else:
            return None

