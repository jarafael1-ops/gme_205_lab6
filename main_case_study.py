from parcel import Parcel
from building import Building
from Irrigation project import Irrigation Project
from household import Household


def print_header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main():
    # ---------------------------------------------------------
    # 1. Create parcels
    # ---------------------------------------------------------
    p1 = Parcel(
        parcel_id="P101
        geometry={"x":5, "y":5},
        area=1000
        zone="Residential"
        parcel_cost=50000
    )



    # ---------------------------------------------------------
    # 2. Create buildings and assign them to parcels
    # ---------------------------------------------------------
    b1 = Building(
        building_id="201
        geometry={"x":5, "y":5},
        building_cost=150000,
        usage="Apartment
        parcel=p1
    )



    # ---------------------------------------------------------
    # 3. Create irrigation project and connect it to parcels
    # ---------------------------------------------------------
    ip1 = Overlay Irrigation Project(
        project_id="IP001",
        geometry={"x": 0, "y": 0},
        area=5000,
        project_location="Central Valley",  
        
    )

    # ---------------------------------------------------------
    # 4. Create households and assign them to buildings
    # ---------------------------------------------------------
    h1 = Household(
        household_id="H301
        num_people=4,
        income=75000,
        tenure_type="Owner",
        building=b1
    )
    # ---------------------------------------------------------
    # 5. Show object descriptions
    # ---------------------------------------------------------
    print_header("PARCELS")
    print(p1.describe())
    

    print_header("BUILDINGS")
    print(b1.describe())
   

    print_header("IRRIGATION PROJECT")
    print(ip1.describe())

    print_header("HOUSEHOLDS")
    print(h1.describe())
    

    # ---------------------------------------------------------
    # 6. Demonstrate class-specific behaviors
    # ---------------------------------------------------------
    print_header("CLASS-SPECIFIC METHODS")
    print(f"{p1.parcel_id} area: {p1.compute_area()}")
    print(f"{b1.building_id} building cost: {b1.calculate_building_cost()}")
    print(f"{ip1.project_id} area: {ip1.identification()}")
    print(f"{h1.household_id} total income: {h1.calculate_total_income()}")
    print(f"{b1.building_id} combined household income: {b1.total_household_income()}")


    # ---------------------------------------------------------
    # 7. Demonstrate shared spatial behavior
    # ---------------------------------------------------------
    print_header("SHARED SPATIAL BEHAVIOR")
    print(f" {p1.parcel_valued}: {p1.calculate_parcel_value()}")
    print(f"{b1.building_valued}: {b1.calculate_building_value()}")
    print(f" {h1.househol_income: {h1.calculate_total_income()}")
    print(f" {ip1:Irrigation_project_valued}: {ip1.calculate_total_project_value()}")
     


    # ---------------------------------------------------------
    # 8. Demonstrate relationships explicitly
    # ---------------------------------------------------------
    print_header("RELATIONSHIPS")
    print(f"Building {b1.building_id} is located on Parcel {b1.parcel.parcel_id}")
    print(f"Building {b2.building_id} is located on Parcel {b2.parcel.parcel_id}")

    for household in b1.households:
        print(f"Household {household.household_id} lives in Building {b1.building_id}")

    for household in b2.households:
        print(f"Household {household.household_id} lives in Building {b2.building_id}")

    for parcel in ip1.adjacent_parcels:
        print(f"Irrigation Project {ip1.project_id} is  to Parcel {parcel.parcel_id}")


    # ---------------------------------------------------------
    # 9. Small analysis examples
    # ---------------------------------------------------------
    print_header("SIMPLE ANALYSIS")
    print(f"Total households in {b1.building_id}: {len(b1.households)}")
    print(f"Total households in {b2.building_id}: {len(b2.households)}")

    richer_building = b1 if b1.total_household_income() > b2.total_household_income() else b2
    print(
        f"Building with higher total household income: "
        f"{richer_building.building_id} ({richer_building.total_household_income()})"
    )


if __name__ == "__main__":
    main()