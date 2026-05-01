class IrrigationProject(SpatialObject):
    def __init__(self, irrigation_project_id, project_area, project_location, project_name, geometry):
        super().__init__(geometry)
        self.irrigation_project_id = irrigation_project_id
        self.project_area = project_area
        self.project_location = project_location
        self.project_name = project_name
        self.parcels = []

    def Identification(self):
        return f"{self.irrigation_project_id}: {self.project_name}"


