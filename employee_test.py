from employee import employee_details
def test_employee_details():
    result = employee_details("Shreya","EMP101","IT","50000")
    expected = "Name : Shreya\nEmployee ID: EMP101\ndepartment:IT\nSalary:50000"
    assert result== expected 