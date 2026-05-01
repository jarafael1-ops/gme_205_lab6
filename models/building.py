from spatial_object import SpatialObject

class Building(SpatialObject):
    """
    Building is a spatial object.
    Matches the UML diagram attributes and relationships.
    """

    def __init__(self, building_id, geometry, usage, building_cost, building_type, parcel=None):
        super().__init__(geometry)
        self.building_id = building_id
        self.geometry = geometry # polygon
        self.usage = usage # from Usage List
        self.building_cost = building_cost # Matches UML
        self.building_type = building_type # Matches UML
        
        self.parcel = parcel
        self.households = [] # Container for the Household composition

        # Sync with Parcel if provided
        if self.parcel is not None:
            self.parcel.add_building(self)

    def calculate_building_cost(self):
        """Matches the method name in the UML diagram."""
        return self.building_cost

    def add_household(self, household):
        """Adds a household to the building's list."""
        if household not in self.households:
            self.households.append(household)

    def describe(self):
        parcel_text = self.parcel.parcel_id if self.parcel else "None"
        return (
            f"Building {self.building_id}: type={self.building_type}, "
            f"cost={self.building_cost}, parcel={parcel_text}"
        )