from data_loader import load_data
from data_processor import (
    get_total_records,
    get_distance_data,
    retrieve_employee_by_id,
    group_records_by_job_role,
    get_department_summary,
    get_department_data,
)
from dashboard import show_home

sample_csv_path = "nurse_attrition.csv"
sample_data = load_data(sample_csv_path)


def test_load_data():
    loaded_data = load_data(sample_csv_path)

    # Assertions to check if the loaded data has the expected structure
    assert isinstance(loaded_data, list), "Loaded data should be a list"
    assert len(loaded_data) > 0, "Loaded data should not be empty"

    # Assuming your data structure has specific fields, modify the assertions accordingly
    sample_record = loaded_data[0]
    assert "EmployeeID" in sample_record, "EmployeeID field is missing"
    assert "Age" in sample_record, "Age field is missing"
    assert "Gender" in sample_record, "Gender field is missing"
    # ... add more assertions for other expected fields

    print("Data loading unit test passed successfully.")


def test_get_total_records():
    assert get_total_records(sample_data) == len(sample_data)


def test_retrieve_employee_by_id():
    emp_id = 1421335
    emp_detail = {
        "EmployeeID": "1421335",
        "Age": "32",
        "Gender": "Male",
        "MaritalStatus": "Divorced",
        "Education": "2",
        "Department": "Maternity",
        "JobRole": "Other",
        "HourlyRate": "40",
        "YearsAtCompany": "6",
        "YearsInCurrRole": "2",
        "DistanceFromHome": "5",
        "BusinessTravel": "Rarely",
        "WorkLifeBalance": "2",
        "YearsLastPromotion": "0",
        "YearsCurrManager": "5",
        "Attrition": "No",
    }
    retreived_emp_detail = retrieve_employee_by_id(sample_data, emp_id)
    assert retreived_emp_detail == emp_detail


def test_get_distance_data():
    distance_data = get_distance_data(sample_data)
    assert len(distance_data) == len(sample_data)
    assert isinstance(distance_data[0], int)


def test_group_records_by_job_role():
    grouped_records = group_records_by_job_role(sample_data)
    assert len(grouped_records) == 4
    assert "Nurse" in grouped_records
    assert "Other" in grouped_records
    assert "Administrative" in grouped_records


def test_get_department_data():
    department_data = get_department_data(sample_data)
    assert isinstance(department_data, dict)
    assert "Maternity" in department_data
    assert "Cardiology" in department_data
    assert "Neurology" in department_data


def test_get_department_summary():
    department = "Neurology"  # Assuming a department from your sample data
    summary = get_department_summary(sample_data, department, export=True)

    # Adjust the following assertions based on the expected structure of the summary
    assert "num_employees" in summary
    assert "num_males" in summary
    assert "num_females" in summary
    assert "minimum_age" in summary
    assert "maximum_age" in summary
    assert "average_age" in summary
    assert "minimum_distance" in summary
    assert "maximum_distance" in summary
    assert "average_distance" in summary
    assert "minimum_hourly_rate" in summary
    assert "maximum_hourly_rate" in summary
    assert "average_hourly_rate" in summary
    assert "percentage_of_single_employee" in summary
    assert "percentage_of_married_employee" in summary
    assert "percentage_of_divorced_employee" in summary
    assert "pct_of_frequently_travel" in summary
    assert "pct_of_rarely_travel" in summary
    assert "pct_of_never_travel" in summary
    assert "mean_hourly_rate" in summary
    assert "std_dvt_hourly_rate" in summary
    assert "variance_hourly_rate" in summary
    assert "avg_worklife_balance" in summary
    assert "avg_attrition_rate" in summary
