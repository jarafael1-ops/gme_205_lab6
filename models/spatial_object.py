from spatial_object import SpatialObject

class IrrigationProject(SpatialObject):
    def __init__(self, project_id, geometry, project_area, project_location, project_name):
        super().__init__(geometry)
        self.irrigation_project_id = project_id
        self.project_area = project_area
        self.project_name = project_name
        self.related_parcels = []

    def add_parcel_to_overlay(self, parcel):
        """Manually adds a parcel to the project's overlay view."""
        self.related_parcels.append(parcel)

    def calculate_total_project_value(self):
        """Calculates the combined value of all land and buildings in the overlay."""
        return sum(p.calculate_parcel_value() for p in self.related_parcels)

class Parcel(SpatialObject):
    def __init__(self, parcel_id, geometry, parcel_area, zone, parcel_cost):
        super().__init__(geometry)
        self.parcel_id = parcel_id
        self.parcel_area = parcel_area
        self.zone = zone
        self.parcel_cost = parcel_cost
        self.buildings = []

    def calculate_parcel_value(self):
        """Sum of land cost and all buildings on this parcel."""
        building_total = sum(b.calculate_building_cost() for b in self.buildings)
        return self.parcel_cost + building_total

class Building(SpatialObject):
    def __init__(self, building_id, geometry, building_cost, building_type, parcel=None):
        super().__init__(geometry)
        self.building_id = building_id
        self.building_cost = building_cost
        self.building_type = building_type
        self.households = []
        if parcel:
            parcel.add_building(self)

    def calculate_building_cost(self):
        return self.building_cost

    def get_total_household_income(self):
        """Calculates the total income of all households in this building."""
        return sum(h.calculate_income() for h in self.households)

class Household:
    def __init__(self, household_id, income, number_people, tenure_type, building=None):
        self.household_id = household_id
        self.income = income
        self.tenure_type = tenure_type
        if building:
            building.add_household(self)

    def calculate_income(self):
        return self.income