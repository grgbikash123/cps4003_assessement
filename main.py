from data_loader import load_data
from data_processor import (
    get_total_records,
    get_department_data,
    retrieve_employee_by_id,
    get_education,
    retrieve_employee_by_department,
    retrieve_employee_by_department_and_role,
    group_records_by_job_role,
    print_employee_list,
    get_department_summary,
    get_distance_data,
    get_worklife_balance,
)
from data_visualizer import generate_pie_chart, generate_histogram

from dashboard import display_dashboard

# global variable
data = list()


def print_employee_info(data, emp_id):
    emp_id = int(emp_id)
    employee_record = retrieve_employee_by_id(data, emp_id)

    if employee_record:
        print(
            f"""
                                +----------------------------------------------+
                                |      Record of Emplooyee with id  '{employee_record['EmployeeID']}'  |
                                +----------------------------------------------+ """
        )
        for key, value in employee_record.items():
            if key == "EmployeeID":
                continue
            if key == "Education":
                education = get_education(value)
                print(
                    f"""                                |   {key:19}: {education:21} |"""
                )
                continue
            if key == "WorkLifeBalance":
                worklife = get_worklife_balance(value)
                print(
                    f"""                                |   {key:19}: {worklife:21} |"""
                )
                continue

            print(f"""                                |   {key:19}: {value:21} |""")
        print(
            """                                |______________________________________________|"""
        )
    else:
        print(f"\n\t\t\tEmployee with id {emp_id} doesn't exist.")


# a) The system will present the user with a text-based user interface through which a user will select options to load the data, process the data, visualise the data, and export the data.
def process_the_loaded_data(data):
    while True:
        print(
            """

                            +---------------------------------------------------+
                            |   Nurse Attrition System : Menu > Process         |
                            +---------------------------------------------------+
                            | 1. Retrieve Total Number of Records               |
                            | 2. Retrieve a List of Unique Departments          |
                            | 3. Retrieve Employee Record by ID                 |
                            | 4. Retrieve Employees by Department               |
                            | 5. Retrieve Employees by Department and Job Role  |
                            | 6. Retreive Employees grouped by Job Role         |
                            | 7. Retreive summary for Department                |
                            | 8. Back to Menu                                   |
                            |___________________________________________________|
        """
        )

        choice = input("\t\t\tEnter your choice (1/2/3/4/5/6/7/8): ").strip()

        if choice == "1":
            total_records = get_total_records(data)
            print(
                f"""
                                    +-----------------------------------+
                                        Total Number of Records: {total_records}  
                                    +-----------------------------------+
                  """
            )

        elif choice == "2":
            departments = get_department_data(data).keys()

            print(
                """

                                    +--------------------------------------+
                                    |         Unique Departments           |
                                    +--------------------------------------+ """
            )
            for department in departments:
                print(f"\t\t\t\t    |          + {department:25} |  ")
            print("""\t\t\t\t    |______________________________________|""")

        elif choice == "3":
            employee_id_to_retrieve = input(
                "\n\t\t\tEnter the Employee ID to retrieve: "
            )
            try:
                employee_id_to_retrieve = int(employee_id_to_retrieve)
                print_employee_info(data, employee_id_to_retrieve)
            except ValueError:
                print("\n\t\t\t[!] Please enter the integer input")
        elif choice == "4":
            department_to_retrieve = input(
                "\n\t\t\tEnter the department to retrieve records: "
            ).strip()
            records = retrieve_employee_by_department(
                data=data, department=department_to_retrieve
            )

        elif choice == "5":
            department_to_retrieve = input(
                "\n\t\t\tEnter the department to retrieve records: "
            ).strip()
            role_to_retrieve = input(
                "\t\t\tEnter the role to retrieve records: "
            ).strip()
            records = retrieve_employee_by_department_and_role(
                data=data, department=department_to_retrieve, role=role_to_retrieve
            )

        elif choice == "6":
            # Retrieve the records for all employees grouped by job role
            grouped_records_by_job_role = group_records_by_job_role(data=data)
            for job_role, records in grouped_records_by_job_role.items():
                header = f"          Records for '{job_role}' job role {'':13}"
                print_employee_list(records, header)

        elif choice == "7":
            # Retrieve a summary of the attrition data for a department
            department_to_summary = input(
                "\n\t\t\tEnter the department to retrieve the summary: "
            ).strip()
            department_summary(data=data, department=department_to_summary)

        elif choice == "8":
            return

        else:
            print("\n\t\t\tInvalid choice")


def visualize_data(data):
    while True:
        print(
            """
                        +-------------------------------------------------------------------------+
                        |               Nurse Attrition System : Menu > Visualize                 | 
                        --------------------------------------------------------------------------+
                        | 1. Pie chart of the no. of employees in each department                 |
                        | 2. Histogram of the distance employees work from home                   |
                        | 3. Dashboard                                                            |
                        | 4. Back to Menu                                                         |
                        +-------------------------------------------------------------------------+

              """
        )

        choice = input("\t\t\tEnter your choice (1/2/3): ").strip()

        if choice == "1":
            # Display a pie chart of the number of employees in each department
            department_counts = get_department_data(data=data)
            generate_pie_chart(
                data=department_counts,
                title="Distribution of Employees Across Departments",
            )

        elif choice == "2":
            # Display a histogram of the distance employees work from home
            distance_data = get_distance_data(data=data)
            generate_histogram(
                data=distance_data,
                xlabel="Distance between the employee's Home and workplace",
                ylabel="Number of Employees",
                title="Distance Distribution of Employees work from home for the department",
            )

        elif choice == "3":
            display_dashboard(data)

        elif choice == "4":
            return

        else:
            print("\n\t\t\tInvalid choice")


def export_summary_of(data):
    department = input("\n\t\t\tEnter the department to retrieve the summary: ").strip()
    get_department_summary(data=data, department=department, export=True)


def is_loaded(data):
    if data is not None and len(data) > 0:
        return True
    else:
        return False


def main():
    while True:
        print(
            """




                            +-----------------------------------------+
                            |       Nurse Attrition System : Menu     |
                            |-----------------------------------------|
                            |        1. Load Data                     |
                            |        2. Process the Loaded Data       |
                            |        3. Visualize                     |
                            |        4. Export                        |
                            |        5. Exit                          |
                            |_________________________________________|
        """
        )

        choice = input("\t\t\tEnter your choice (1/2/3/4): ").strip()

        if choice == "1":
            file_path = input(
                "\n\t\t\tEnter the file path for nurse_attrition.csv: "
            ).strip()
            # file_path = 'nurse_attrition.csv'
            data = load_data(file_path)
        elif choice == "2":
            try:
                process_the_loaded_data(data)
            except UnboundLocalError:
                print("\n\t\t\t [!] Data not loaded. Please load data first.")
        elif choice == "3":
            try:
                visualize_data(data)
            except UnboundLocalError:
                print("\n\t\t\t [!] Data not loaded. Please load data first.")
        elif choice == "4":
            try:
                export_summary_of(data=data)
            except UnboundLocalError:
                print("\n\t\t\t [!] Data not loaded. Please load data first.")
        elif choice == "5":
            print("\n\t\t\t Exiting the program. Goodbye!")
            break
        else:
            print("\n\t\t\tInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
