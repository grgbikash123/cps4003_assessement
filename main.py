from data_processor import DataLoader, DataRetriever


def process_the_loaded_data(retriever):
    while True:
        print("\n\n\n\t\t\t Nurse Attrition System : Menu > Process ")
        print("\t\t\t-------------------------------------------")
        print("\t\t\t  1. Retrieve Total Number of Records")
        print("\t\t\t  2. Retrieve a List of Unique Departments")
        print("\t\t\t  3. Retrieve Employee Record by ID")
        print("\t\t\t  4. Back to Menu")

        choice = input("\t\t\tEnter your choice (1/2/3/4): ")

        if choice == "1":
            total_records = retriever.total_records()
            print(f"\n\t\t\tTotal Number of Records: {total_records}")
        elif choice == "2":
            departments = retriever.unique_departments()
            print("\n\t\t\tUnique Departments:")
            for department in departments:
                print(f"\t\t\t   - {department}")
        elif choice == "3":
            employee_id_to_retrieve = int(
                input("\n\t\t\tEnter the Employee ID to retrieve: ")
            )
            employee_record = retriever.retrieve_employee_by_id(employee_id_to_retrieve)
            if employee_record:
                print("\n\t\t\t   Employee Record:")
                print("\t\t\t-----------------------------------------------")
                for key, value in employee_record.items():
                    print(f"\t\t\t\t{key:19}: {value}")
                print("\t\t\t-----------------------------------------------")
        elif choice == "4":
            return
        else:
            print("\n\t\t\tInvalid choice")


def main():
    data_loader = DataLoader()
    data_retriever = None

    while True:
        print("\n\n\n\t\t\t Nurse Attrition System : Menu ")
        print("\t\t\t-------------------------------------------")
        print("\t\t\t 1. Load Data")
        print("\t\t\t 2. Process the Loaded Data")
        print("\t\t\t 3. Exit")

        choice = input("\t\t\tEnter your choice (1/2/3): ")

        if choice == "1":
            file_path = input("\n\t\t\tEnter the file path for nurse_attrition.csv: ")
            data_loader.load_data(file_path)
        elif choice == "2":
            if data_loader.data:
                data_retriever = DataRetriever(data_loader.data)
                process_the_loaded_data(data_retriever)
            else:
                print("\n\t\t\t [!] Data not loaded. Please load data first.")
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("\n\t\t\tInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
