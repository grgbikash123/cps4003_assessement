class DataRetriever:
    def __init__(self, data):
        self.data = data

    def total_records(self):
        return len(self.data) if self.data else 0

    def unique_departments(self):
        return list(set(record['Department'] for record in self.data)) if self.data else []

    def retrieve_employee_by_id(self, employee_id):
        return next((record for record in self.data if int(record['EmployeeID']) == employee_id), None) if self.data else None

    def print_employee_details(self, records, header):
        if records:
            print(f"""
                +----------------------------------------------------------------------+
                |{header.center(70)}|
                +----------------------------------------------------------------------+""", end="")

            for record in records:
                print(f"""
                |             Employee ID  : {record['EmployeeID']:25}                 |  
                |             Age          : {record['Age']:18}                        |  
                |             Gender       : {record['Gender']:21}                     |  
                |             Education    : {record['Education']:24}                  |  
                |             Job Role     : {record['JobRole']:22}                    |  
                | {'     -------------------------------------':69}| """,end="")
            print("\n\t\t|______________________________________________________________________|")
        else:
            print(f"\n\t\t\t[!] No records found.")

    def retrieve_employee_by_department(self, department,visible=False):
        records_in_department = [record for record in self.data if record['Department'] == department]
        header = f"Records for '{department}' department {'':17}"
        if visible==True:
            return records_in_department
        self.print_employee_details(records_in_department, header)

    def retrieve_employee_by_department_and_role(self, department, role):
        records_with_role = [record for record in self.data if record['Department'] == department and record['JobRole'] == role]
        header = f"Records for employee from '{department}' department and '{role}' role   "
        self.print_employee_details(records_with_role, header)
        return records_with_role
