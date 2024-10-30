# Patient Insurance Estimator

This project provides a `Patient` class to model patient data and estimate their insurance costs based on various attributes such as age, sex, BMI, number of children, and smoking status. The project also includes unit tests using `pytest` to ensure the functionality of the `Patient` class.

## Features

- Initialize patient data
- Update patient age
- Update number of children
- Estimate insurance cost
- Retrieve patient profile

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/patient-insurance-estimator.git
    cd patient-insurance-estimator
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Example

```python
from main import Patient

# Create a new patient
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)

# Print patient name
print(patient1.name)

# Estimate insurance cost
patient1.estimated_insurance_cost()

# Update age and re-estimate insurance cost
patient1.update_age(26)
patient1.estimated_insurance_cost()

# Update number of children and re-estimate insurance cost
patient1.update_num_children(1)

# Print patient profile
print(patient1.patient_profile())