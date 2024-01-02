from data_loader import DataLoader
from data_processor import DataRetriever
from data_visualizer import visualize_pie_chart

# a) The system will present the user with a text-based user interface through which a user will select options to load the data, process the data, visualise the data, and export the data.
def process_the_loaded_data(retriever):
    while True:
        print("""

                            +---------------------------------------------------+
                            |   Nurse Attrition System : Menu > Process         |
                            +---------------------------------------------------+
                            | 1. Retrieve Total Number of Records               |
                            | 2. Retrieve a List of Unique Departments          |
                            | 3. Retrieve Employee Record by ID                 |
                            | 4. Retrieve Employees by Department               |
                            | 5. Retrieve Employees by Department and Role      |
                            | 6. Back to Menu                                   |
                            |___________________________________________________|
        """)

        choice = input("\t\t\tEnter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            total_records = retriever.total_records()
            print(f"""
                                +-----------------------------------+
                                     Total Number of Records: {total_records}  
                                +-----------------------------------+
                  """)

        elif choice == '2':
            departments = retriever.unique_departments()
            

            print(f"""
                                +--------------------------------------+
                                |         Unique Departments           |
                                +--------------------------------------+ """)
            for department in departments:
                print(f"\t\t\t\t|          + {department:25} |  ")
            print(f"""\t\t\t\t|______________________________________|""")

        elif choice == '3':
            employee_id_to_retrieve = input("\n\t\t\tEnter the Employee ID to retrieve: ")
            try:
                employee_id_to_retrieve = int(employee_id_to_retrieve)
                employee_record = retriever.retrieve_employee_by_id(employee_id_to_retrieve)

                if employee_record:
                    print(f"""
                                +----------------------------------------------+
                                |      Record of Emplooyee with id  '{employee_record['EmployeeID']}'  |
                                +----------------------------------------------+ """)
                    for key, value in employee_record.items():
                        if key == 'EmployeeID':
                            continue
                        print(f"""                                |   {key:19}: {value:21} |""")
                    print("""                                |______________________________________________|""")
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

        elif choice == '4':
            department_to_retrieve = input("\n\t\t\tEnter the department to retrieve records: ")
            records = retriever.retrieve_employee_by_department(department_to_retrieve)

        elif choice == '5':
            department_to_retrieve = input("\n\t\t\tEnter the department to retrieve records: ")
            role_to_retrieve = input("\t\t\tEnter the role to retrieve records: ")
            records = retriever.retrieve_employee_by_department_and_role(department_to_retrieve, role_to_retrieve)

        elif choice == '6':
            return

        else:
            print("\n\t\t\tInvalid choice")

def visualize_data(system):
    while True:
        print(f"""
                        +-------------------------------------------------------------------------+
                        |               Nurse Attrition System : Menu > Visualize                 | 
                        --------------------------------------------------------------------------+
                        | 1. Display a pie chart of the number of employees in each department    |
                        | 2. Back to Menu                                                         |
                        +-------------------------------------------------------------------------+

              """)

        choice = input("\t\t\tEnter your choice (1/2): ")

        if choice == '1':
            # Display a pie chart of the number of employees in each department
            department_counts = {department: len(system.retrieve_employee_by_department(department,visible=True)) for department in system.unique_departments()}
            visualize_pie_chart(department_counts)
        elif choice == '2':
            return
        else:
            print("\n\t\t\tInvalid choice")


def main():
    data_loader = DataLoader()
    data_retriever = None

    while True:
        print("""




                            +-----------------------------------------+
                            | Nurse Attrition System : Menu           |
                            |-----------------------------------------|
                            |        1. Load Data                     |
                            |        2. Process the Loaded Data       |
                            |        3. Visualize                     |
                            |        4. Exit                          |
                            |_________________________________________|
        """)



        choice = input("\t\t\tEnter your choice (1/2/3/4): ")

        if choice == '1':
            file_path = input("\n\t\t\tEnter the file path for nurse_attrition.csv: ")
            data_loader.load_data(file_path)
            data_retriever = DataRetriever(data_loader.data)
        elif choice == '2':
            if data_loader.data:
                process_the_loaded_data(data_retriever)
            else:
                print("\n\t\t\t [!] Data not loaded. Please load data first.")
        elif choice == '3':
            if data_loader.data:
                visualize_data(data_retriever)
            else:
                print("\n\t\t\t [!] Data not loaded. Please load data first.")
        elif choice == '4':
            print("\n\t\t\t Exiting the program. Goodbye!")
            break
        else:
            print("\n\t\t\tInvalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
    # data_loader = DataLoader()
    # data_loader.load_data("../some.csv")
    # data_retriever = DataRetriever(data_loader.data)
    """
    employee_record = data_retriever.retrieve_employee_by_department_and_role("Maternity","Other")
    """


