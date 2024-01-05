from matplotlib.pyplot import margins
import json


class DataRetriever:
    def __init__(self, data):
        self.data = data

    # Retrieve the total number of records that have been loaded
    def total_records(self):
        return len(self.data) if self.data else 0

    # list of unique department names.
    def get_department_data(self):
        department_data = {}
        for record in self.data:
            department = record.get("Department")
            if department:
                if department in department_data:
                    department_data[department] += 1
                else:
                    department_data[department] = 1
        return department_data

    # the record for an employee using an employee id as specified  by the user.
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

    def get_education(self, num):
        num = int(num)
        if num == 1:
            return "GCSE"
        elif num == 2:
            return "A-Levels"
        elif num == 3:
            return "Bachelor"
        elif num == 4:
            return "Master"
        elif num == 5:
            return "Doctorate"

    def print_employee_details(self, records, header):
        if records:
            print(
                f"""
                        +----------------------------------------------------+
                        |{header.center(52)}|
                        +----------------------------------------------------+""",
                end="",
            )

            for record in records:
                print(
                    f"""
                        |             Employee ID  : {record['EmployeeID']:20}    |  
                        |             Age          : {record['Age']:10}              |  
                        |             Gender       : {record['Gender']:13}           |  
                        |             Education    : {self.get_education(record['Education']):16}        |  
                        |             Job Role     : {record['JobRole']:18}      |  
                        | {'     -------------------------------------':51}| """,
                    end="",
                )
            print("\n\t\t\t|____________________________________________________|")
        else:
            print(f"\n\t\t\t[!] No records found.")

    # the records for employees that work in a particular  department as specified by the user
    def retrieve_employee_by_department(self, department, visible=False):
        records_in_department = [
            record for record in self.data if record["Department"] == department
        ]
        header = f"Records for '{department}' department {'':17}"
        if visible:
            return records_in_department
        self.print_employee_details(records_in_department, header)

    # the records for employees that work in a particular  department and have a particular role as specified by the user
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

    # the records for all employees grouped by the job role.
    def group_records_by_job_role(self):
        grouped_records = {}
        for record in self.data:
            job_role = record["JobRole"]
            if job_role in grouped_records:
                grouped_records[job_role].append(record)
            else:
                grouped_records[job_role] = [record]
        return grouped_records

    # worklife balance
    def worklife(self, num):
        num = int(num)

        if num == 0:
            return "Bad"
        elif num == 1:
            return "Good"
        elif num == 2:
            return "Better"
        elif num == 3:
            return "Best"

    # summary of the attrition data for a department as specified by the user.
    def department_summary(self, department, export=False):
        department_records = [
            record for record in self.data if record["Department"] == department
        ]

        if not department_records:
            print(f"\n\t\t\t[!] No records found for department '{department}'.")
            return

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
        ### calculating mean
        mean_hourly_rate = sum(hourly_rates) / num_employees

        ### calculating variance
        squared_diff = []
        for rate in hourly_rates:
            squared_diff.append((rate - mean_hourly_rate) ** 2)
        variance_hourly_rate = sum(squared_diff) / num_employees

        ### calculating standard deviation
        std_hourly_rate = variance_hourly_rate**0.5

        ##  calculating average work-life balance for the department.
        work_life_balances = [
            float(record["WorkLifeBalance"]) for record in department_records
        ]
        avg_worklife_balance = sum(work_life_balances) / num_employees

        ##  calculating average attrition rate for the department.
        attrition_rates = [
            1 if record["Attrition"] == "Yes" else 0 for record in department_records
        ]
        avg_attrition_rate = sum(attrition_rates) / num_employees

        if not export:
            print(
                f"""
                            +--------------------------------------------------------------+
                            |               Summary for Department: {department:11} {'':9}  |
                            +--------------------------------------------------------------+
                            | Number of Employees                  : {num_employees:^6} {'':14} |
                            | Number of Male Employees             : {num_male:^6} {'':14} |
                            | Number of Female Employees           : {num_female:^6} {'':14} | 
                            | Minimum Age                          : {min_age:^6} {'':14} | 
                            | Maximum Age                          : {max_age:^6} {'':14} | 
                            | Average Age                          : {avg_age:^6.2f} {'':14} | 
                            | Minimum Distance                     : {min_distance:^6} {'':14} | 
                            | Maximum Distance                     : {max_distance:^6} {'':14} | 
                            | Average Distance                     : {avg_distance:^6.2f} {'':13}  | 
                            | Minimum Hourly Rate                  : {min_hourly_rate:^6} {'':14} | 
                            | Maximum Hourly Rate                  : {max_hourly_rate:^6} {'':14} | 
                            | Average Hourly Rate                  : {avg_hourly_rate:^6.2f} {'':13}  | 
                            | Percentage of Single Employees       : {single_percentage:^5.2f}% {'':14} |
                            | Percentage of Married Employees      : {married_percentage:^5.2f}% {'':14} |
                            | Percentage of Divorced Employees     : {divorced_percentage:^5.2f}% {'':14} |
                            | Percentage of Frequently Travel      : {frequently_travel_percentage:^5.2f}% {'':14} |
                            | Percentage of Rarely Travel          : {rarely_travel_percentage:^5.2f}% {'':14} |
                            | Percentage of Never Travel           : {never_travel_percentage:^5.2f}% {'':14} |
                            | Mean Hourly Rate                     : {mean_hourly_rate:^6.2f} {'':14} |
                            | Standard Deviation of Hourly Rate    : {std_hourly_rate:^6.2f} {'':14} |
                            | Variance of Hourly Rate              : {variance_hourly_rate:^6.2f} {'':14} |
                            | Average Work Life Balance            : {self.worklife(avg_worklife_balance):^6} {'':13}  | 
                            | Average Attrition Rate               : {avg_attrition_rate:^6.2%} {'':13}  | 
                            +--------------------------------------------------------------+
            """
            )

        if export:
            output_file_path = f"{department}.json"
            summary_json_data = {
                "department": department,
                "num_employees": num_employees,
                "num_males": num_male,
                "num_females": num_female,
                "minimum_age": min_age,
                "maximum_age": max_age,
                "average_age": round(avg_age, 2),
                "minimum_distance": min_distance,
                "maximum_distance": max_distance,
                "average_distance": round(avg_distance, 2),
                "minimum_hourly_rate": min_hourly_rate,
                "maximum_hourly_rate": max_hourly_rate,
                "average_hourly_rate": round(avg_hourly_rate, 2),
                "percentage_of_single_employee": round(single_percentage, 2),
                "percentage_of_married_employee": round(married_percentage, 2),
                "percentage_of_divorced_employee": round(divorced_percentage, 2),
                "pct_of_frequently_travel": round(frequently_travel_percentage, 2),
                "pct_of_rarely_travel": round(rarely_travel_percentage, 2),
                "pct_of_never_travel": round(never_travel_percentage, 2),
                "mean_hourly_rate": round(mean_hourly_rate, 2),
                "std_dvt_hourly_rate": round(std_hourly_rate, 2),
                "variance_hourly_rate": round(variance_hourly_rate, 2),
                "avg_worklife_balance": self.worklife(avg_worklife_balance),
                "avg_attrition_rate": round(avg_attrition_rate, 2),
            }
            with open(output_file_path, "w") as json_file:
                json.dump(summary_json_data, json_file)

            print(f"\n\t\t\t[+] Department summary exported to '{output_file_path}'.")
            return

    def get_distance_data(self):
        return [
            int(record["DistanceFromHome"])
            for record in self.data
            if "DistanceFromHome" in record
        ]
