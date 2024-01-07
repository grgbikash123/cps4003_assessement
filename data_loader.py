import csv


def load_data(file_path):
    try:
        with open(file_path, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
            print("\n\t\t\t[+] Data loaded successfully.")
            return data
    except FileNotFoundError as e:
        print(f"\n\t\t\t[x] '{file_path}': {e.strerror} (OS error {e.errno})")
    except PermissionError as e:
        print(f"\n\t\t\t[x] '{file_path}': {e.strerror} (OS error {e.errno})")
