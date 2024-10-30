import pytest
from main import Patient

def test_patient_initialization():
    patient = Patient("John Doe", 25, 1, 22.2, 0, 0)
    assert patient.name == "John Doe"
    assert patient.age == 25
    assert patient.sex == 1
    assert patient.bmi == 22.2
    assert patient.num_of_children == 0
    assert patient.smoker == 0

def test_update_age():
    patient = Patient("John Doe", 25, 1, 22.2, 0, 0)
    patient.update_age(26)
    assert patient.age == 26

def test_update_num_children():
    patient = Patient("John Doe", 25, 1, 22.2, 0, 0)
    patient.update_num_children(1)
    assert patient.num_of_children == 1

def test_estimated_insurance_cost():
    patient = Patient("John Doe", 25, 1, 22.2, 0, 0)
    estimated_cost = 250 * 25 - 128 * 1 + 370 * 22.2 + 425 * 0 + 24000 * 0 - 12500
    assert patient.estimated_insurance_cost() == estimated_cost

def test_patient_profile():
    patient = Patient("John Doe", 25, 1, 22.2, 0, 0)
    profile = patient.patient_profile()
    expected_profile = {
        'Name': "John Doe",
        'Age': 25,
        'Sex': 1,
        'BMI': 22.2,
        'Number of Children': 0,
        'Smoker': 0
    }
    assert profile == expected_profile