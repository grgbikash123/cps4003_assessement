from data_loader import DataLoader
from data_processor import DataRetriever
from data_visualizer import generate_pie_chart, generate_histogram
from dashboard import display_dashboard


# a) The system will present the user with a text-based user interface through which a user will select options to load the data, process the data, visualise the data, and export the data.
def process_the_loaded_data(retriever):
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
            total_records = retriever.total_records()
            print(
                f"""
                                +-----------------------------------+
                                     Total Number of Records: {total_records}  
                                +-----------------------------------+
                  """
            )

        elif choice == "2":
            departments = retriever.get_department_data().keys()

            print(
                """
                                +--------------------------------------+
                                |         Unique Departments           |
                                +--------------------------------------+ """
            )
            for department in departments:
                print(f"\t\t\t\t|          + {department:25} |  ")
            print("""\t\t\t\t|______________________________________|""")

        elif choice == "3":
            employee_id_to_retrieve = input(
                "\n\t\t\tEnter the Employee ID to retrieve: "
            )
            try:
                employee_id_to_retrieve = int(employee_id_to_retrieve)
                employee_record = retriever.retrieve_employee_by_id(
                    employee_id_to_retrieve
                )

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
                            education = retriever.get_education(value)
                            print(
                                f"""                                |   {key:19}: {education:21} |"""
                            )
                            continue

                        print(
                            f"""                                |   {key:19}: {value:21} |"""
                        )
                    print(
                        """                                |______________________________________________|"""
                    )
                """
                if employee_record:
                    
                    print("\n\t\t\t\t+----------------------------------------------+")
                    print(f"\t\t\t\t|      Record of Emplooyee with id  '{employee_record['EmployeeID']}'  |")
                    print("\t\t\t\t+----------------------------------------------+")
                    for key, value in employee_record.items():
                        if key == 'EmployeeID':
                            continue
                        print(f"\t\t\t\t|\t{key:19}: {value:17} |")
                    print("\t\t\t\t|______________________________________________|")
                """

            except ValueError:
                print("\n\t\t\t[!] Please enter the integer input")

            # employee_id_to_retrieve = 1414939

        elif choice == "4":
            department_to_retrieve = input(
                "\n\t\t\tEnter the department to retrieve records: "
            ).strip()
            records = retriever.retrieve_employee_by_department(department_to_retrieve)

        elif choice == "5":
            department_to_retrieve = input(
                "\n\t\t\tEnter the department to retrieve records: "
            ).strip()
            role_to_retrieve = input(
                "\t\t\tEnter the role to retrieve records: "
            ).strip()
            records = retriever.retrieve_employee_by_department_and_role(
                department_to_retrieve, role_to_retrieve
            )

        elif choice == "6":
            # Retrieve the records for all employees grouped by job role
            grouped_records_by_job_role = retriever.group_records_by_job_role()
            for job_role, records in grouped_records_by_job_role.items():
                header = f"Records for '{job_role}' job role {'':26}"
                retriever.print_employee_details(records, header)

        elif choice == "7":
            # Retrieve a summary of the attrition data for a department
            department_to_summary = input(
                "\n\t\t\tEnter the department to retrieve the summary: "
            ).strip()
            retriever.department_summary(department_to_summary)

        elif choice == "8":
            return

        else:
            print("\n\t\t\tInvalid choice")


def visualize_data(retriever):
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
            department_counts = retriever.get_department_data()
            generate_pie_chart(
                data=department_counts,
                title="Distribution of Employees Across Departments",
            )

        elif choice == "2":
            # Display a histogram of the distance employees work from home
            distance_data = retriever.get_distance_data()
            generate_histogram(
                data=distance_data,
                xlabel="Distance between the employee's Home and workplace",
                ylabel="Number of Employees",
                title="Distance Distribution of Employees work from home for the department",
            )

        elif choice == "3":
            display_dashboard(retriever)

        elif choice == "4":
            return

        else:
            print("\n\t\t\tInvalid choice")


def export_json(retriever):
    department = input("\n\t\t\tEnter the department to retrieve the summary: ").strip()
    retriever.department_summary(department=department, export=True)


def main():
    data_loader = DataLoader()
    data_retriever = None

    while True:
        print(
            """




                            +-----------------------------------------+
                            | Nurse Attrition System : Menu           |
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
            data_loader.load_data(file_path)
            data_retriever = DataRetriever(data_loader.data)
        elif choice == "2":
            if data_loader.data:
                process_the_loaded_data(data_retriever)
            else:
                print("\n\t\t\t [!] Data not loaded. Please load data first.")
        elif choice == "3":
            if data_loader.data:
                visualize_data(data_retriever)
            else:
                print("\n\t\t\t [!] Data not loaded. Please load data first.")
        elif choice == "4":
            if data_loader.data:
                export_json(data_retriever)
            else:
                print("\n\t\t\t [!] Data not loaded. Please load data first.")
        elif choice == "5":
            print("\n\t\t\t Exiting the program. Goodbye!")
            break
        else:
            print("\n\t\t\tInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
    """
    data_loader = DataLoader()
    data_loader.load_data("some.csv")
    data_retriever = DataRetriever(data_loader.data)
    Dashboard(data_retriever)
    """

    # department_to_summary = "Neurology"
    # data_retriever.department_summary(department_to_summary)
    # employee_record = data_retriever.retrieve_employee_by_department_and_role("Maternity","Other")
