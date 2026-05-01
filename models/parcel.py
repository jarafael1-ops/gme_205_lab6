from spatial_object import SpatialObject

class Parcel(SpatialObject):
    """
    Parcel is a spatial object.
    Matches UML: parcel_id, parcel_area, geometry, zone, parcel_cost.
    """

    def __init__(self, parcel_id, geometry, parcel_area, zone, parcel_cost):
        super().__init__(geometry)
        self.parcel_id = int(parcel_id)
        self.parcel_area = float(parcel_area)
        self.geometry = geometry # polygon
        
        # Zone: matches the "Zone List" (commercial, residential, mixed-use)
        self.zone = zone 
        
        # Cost: This attribute connects the Parcel to the "Value" box in your UML
        self.parcel_cost = parcel_cost 
        
        self.buildings = [] 

    def compute_area(self):
        """Returns the area as required by the UML method list."""
        return self.parcel_area

    def compute_zone(self):
        """Returns the current zone type."""
        return self.zone

    def calculate_parcel_value(self):
        """
        Calculates the total value of the land plus all buildings on it.
        This represents the link to the 'Value' class in your diagram.
        """
        building_total = sum(b.calculate_building_cost() for b in self.buildings)
        return self.parcel_cost + building_total

    def add_building(self, building):
        if building not in self.buildings:
            self.buildings.append(building)
            if building.parcel != self:
                building.parcel = self

    def describe(self):
        return (
            f"Parcel {self.parcel_id}: Zone={self.zone}, "
            f"Land Cost={self.parcel_cost}, Total Buildings={len(self.buildings)}"
        )
    

