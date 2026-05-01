class Household:
    def __init__(self, household_id, income, number_people, tenure_type, building=None):
        self.household_id = household_id
        self.income = income
        self.number_people = number_people
        # Tenure type: Should be 'owner' or 'renter' per your Diagram list
        self.tenure_type = tenure_type 
        self.building = building

        if self.building is not None:
            self.building.add_household(self)

    def calculate_income(self):
        """Matches 'calculate_income()' in the UML diagram."""
        return self.income

    def describe(self):
        return (f"Household {self.household_id}: {self.tenure_type}, "
                f"Income: {self.income}")
    
    