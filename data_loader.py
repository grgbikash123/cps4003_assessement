import csv


class DataLoader:
    def __init__(self):
        self.data = None

    def load_data(self, file_path):
        try:
            with open(file_path, "r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                self.data = list(csv_reader)
                print("\n\t\t\t[+] Data loaded successfully.")
        except FileNotFoundError as e:
            print(f"\n\t\t\t[x] '{file_path}': {e.strerror} (OS error {e.errno})")
        except PermissionError as e:
            print(f"\n\t\t\t[x] '{file_path}': {e.strerror} (OS error {e.errno})")
