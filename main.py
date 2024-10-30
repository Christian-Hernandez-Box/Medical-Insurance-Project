class Patient:
    def __init__(self, name: str, age: int, sex: int, bmi: float, num_of_children: int, smoker: int):
        self.name = name
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker

    def update_age(self, new_age: int):
        self.age = new_age
        print(f"{self.name} is now {self.age} years old.")

    def update_num_children(self, new_num_children: int):
        self.num_of_children = new_num_children
        if self.num_of_children == 1:
            print(f"{self.name} has {self.num_of_children} child.")
        else:
            print(f"{self.name} has {self.num_of_children} children.")
        self.estimated_insurance_cost()

    def estimated_insurance_cost(self) -> float:
        # Actual insurance cost calculation
        estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
        print(f"Estimated insurance cost for {self.name} is ${estimated_cost:.2f}.")
        return estimated_cost

    def patient_profile(self) -> dict:
        patient_information = {
            'Name': self.name,
            'Age': self.age,
            'Sex': self.sex,
            'BMI': self.bmi,
            'Number of Children': self.num_of_children,
            'Smoker': self.smoker
        }
        return patient_information