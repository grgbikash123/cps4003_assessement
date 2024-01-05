class DataRetriever:
    def __init__(self, data):
        self.data = data

    def total_records(self):
        return len(self.data) if self.data else 0

    def unique_departments(self):
        return (
            list(set(record["Department"] for record in self.data)) if self.data else []
        )

    def retrieve_employee_by_id(self, employee_id):
        return (
            next(
                (
                    record
                    for record in self.data
                    if int(record["EmployeeID"]) == employee_id
                ),
                None,
            )
            if self.data
            else None
        )

    def print_employee_details(self, records, header):
        if records:
            print(
                f"""
                +----------------------------------------------------------------------+
                |{header:^70}|
                +----------------------------------------------------------------------+""",
                end="",
            )
            for record in records:
                print(
                    f"""
                |             Employee ID  : {record['EmployeeID']:25}                 |  
                |             Age          : {record['Age']:18}                        |  
                |             Gender       : {record['Gender']:21}                     |  
                |             Education    : {record['Education']:24}                  |  
                |             Job Role     : {record['JobRole']:22}                    |  
                | {'     -------------------------------------':69}| """,
                    end="",
                )
            print(
                "\n\t\t|______________________________________________________________________|"
            )
        else:
            print(f"\n\t\t\t[!] No records found.")

    def retrieve_employee_by_department(self, department, visible=False):
        records_in_department = [
            record for record in self.data if record["Department"] == department
        ]
        header = f"Records for '{department}' department {'':17}"
        if visible:
            return records_in_department
        self.print_employee_details(records_in_department, header)

    def retrieve_employee_by_department_and_role(self, department, role):
        records_with_role = [
            record
            for record in self.data
            if record["Department"] == department and record["JobRole"] == role
        ]
        header = (
            f"Records for employee from '{department}' department and '{role}' role   "
        )
        self.print_employee_details(records_with_role, header)
        return records_with_role

    def group_records_by_job_role(self):
        grouped_records = {}
        for record in self.data:
            job_role = record["JobRole"]
            if job_role in grouped_records:
                grouped_records[job_role].append(record)
            else:
                grouped_records[job_role] = [record]
        return grouped_records

    def department_summary(self, department):
        department_records = [
            record for record in self.data if record["Department"] == department
        ]

        if not department_records:
            print(f"\n\t\t\t[!] No records found for department '{department}'.")
            return

        # Calculate statistics
        ## The number of employees in the department.
        num_employees = len(department_records)

        ## The number of employees that are male and female in the department
        num_male = 0
        num_female = 0

        for record in department_records:
            if record["Gender"] == "Male":
                num_male += 1
            elif record["Gender"] == "Female":
                num_female += 1

        ## The minimum, maximum and average age of an employee in the department.
        ages = [int(record["Age"]) for record in department_records]
        min_age = min(ages)
        max_age = max(ages)
        avg_age = sum(ages) / num_employees

        ## The minimum, maximum, and average distance employees work from home for the department.
        distanceFromHome = [
            int(record["DistanceFromHome"]) for record in department_records
        ]
        min_distance = min(distanceFromHome)
        max_distance = max(distanceFromHome)
        avg_distance = sum(distanceFromHome) / num_employees

        ## The minimum, maximum, and average hourly rate for the department.
        hourly_rates = [float(record["HourlyRate"]) for record in department_records]
        min_hourly_rate = min(hourly_rates)
        max_hourly_rate = max(hourly_rates)
        avg_hourly_rate = sum(hourly_rates) / num_employees

        ## The percentage of single, married and divorced employees in the department
        num_single = 0
        num_married = 0
        num_divorced = 0

        for record in department_records:
            if record["MaritalStatus"] == "Single":
                num_single += 1
            elif record["MaritalStatus"] == "Married":
                num_married += 1
            elif record["MaritalStatus"] == "Divorced":
                num_divorced += 1

        single_percentage = (num_single / num_employees) * 100
        married_percentage = (num_married / num_employees) * 100
        divorced_percentage = (num_divorced / num_employees) * 100

        ## The percentage of employees that frequently, rarely and never travel for business purposes in the department.
        num_frequently_travel = 0
        num_rarely_travel = 0
        num_never_travel = 0

        for record in department_records:
            travel_frequency = record["BusinessTravel"]
            if travel_frequency == "Frequently":
                num_frequently_travel += 1
            elif travel_frequency == "Rarely":
                num_rarely_travel += 1
            elif travel_frequency == "Never":
                num_never_travel += 1

        frequently_travel_percentage = (num_frequently_travel / num_employees) * 100
        rarely_travel_percentage = (num_rarely_travel / num_employees) * 100
        never_travel_percentage = (num_never_travel / num_employees) * 100

        ##  The mean, standard deviation and variance for the hourly rate of employees in the department.
        ### Calculate mean
        mean_hourly_rate = sum(hourly_rates) / num_employees

        ### Calculate variance
        squared_diff = []
        for rate in hourly_rates:
            squared_diff.append((rate - mean_hourly_rate) ** 2)
        variance_hourly_rate = sum(squared_diff) / num_employees

        ### Calculate standard deviation
        std_hourly_rate = variance_hourly_rate**0.5

        ##  The average work-life balance for the department.
        work_life_balances = [
            float(record["WorkLifeBalance"]) for record in department_records
        ]
        avg_work_life_balance = sum(work_life_balances) / num_employees

        ##  The average attrition rate for the department.
        attrition_rates = [
            1 if record["Attrition"] == "Yes" else 0 for record in department_records
        ]
        avg_attrition_rate = sum(attrition_rates) / num_employees

        print(
            f"""
            +------------------------------------------------------------------------+
            |               Summary for Department: {department:11} {'':20} |
            +------------------------------------------------------------------------+
            | Number of Employees                  : {num_employees:5} {'':25} |
            | Number of Male Employees             : {num_male:5} {'':25} |
            | Number of Female Employees           : {num_female:5} {'':25} | 
            | Minimum Age                          : {min_age:5} {'':25} | 
            | Maximum Age                          : {max_age:5} {'':25} | 
            | Average Age                          : {avg_age:.2f} {'':25} | 
            | Minimum Distance                     : {min_distance:5} {'':25} | 
            | Maximum Distance                     : {max_distance:5} {'':25} | 
            | Average Distance                     : {avg_distance:.2f} {'':25}  | 
            | Minimum Hourly Rate                  : {min_hourly_rate:5} {'':25} | 
            | Maximum Hourly Rate                  : {max_hourly_rate:5} {'':25} | 
            | Average Hourly Rate                  : {avg_hourly_rate:5.2f} {'':24}  | 
            | Percentage of Single Employees       : {single_percentage:5.2f}% {'':24} |
            | Percentage of Married Employees      : {married_percentage:5.2f}% {'':24} |
            | Percentage of Divorced Employees     : {divorced_percentage:5.2f}% {'':24} |
            | Percentage of Frequently Travel      : {frequently_travel_percentage:5.2f}% {'':24} |
            | Percentage of Rarely Travel          : {rarely_travel_percentage:5.2f}% {'':24} |
            | Percentage of Never Travel           : {never_travel_percentage:5.2f}% {'':24} |
            | Mean for Hourly Rate                 : {mean_hourly_rate:5.2f} {'':25} |
            | Standard Deviation for Hourly Rate   : {std_hourly_rate:5.2f} {'':25} |
            | Variance for Hourly Rate             : {variance_hourly_rate:5.2f} {'':25} |
            | Average Work Life Balance            : {avg_work_life_balance:.2f} {'':25}  | 
            | Average Attrition Rate               : {avg_attrition_rate:.2%} {'':24}  | 
            +------------------------------------------------------------------------+
        """
        )

    def get_distance_data(self):
        return [
            int(record["DistanceFromHome"])
            for record in self.data
            if "DistanceFromHome" in record
        ]
