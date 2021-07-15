#Function collecting dictionary with vehicle data entered by user and calculating Total Fuel cost
def fuel_calc(v_data):
    mltply_list = []
    for n1,n2 in zip(v_data["mileage"], v_data["Driving_pattern_km"]):
        mltply_list.append(n2/n1)
    Sum = sum(mltply_list)
    cost_of_fuel = Sum * v_data["fuel_market_cost"]
    print(f"Total cost of Fuel is {cost_of_fuel}")
    return cost_of_fuel
#Function collecting dictionary with vehicle data entered by user and calculating Total Insurance cost
def Total_insurance_cost(ve_data):
    fixed_insur_cost = 800
    deprecated_value = ve_data["Cost_of_new_vehicle"] - 10000
    print(f"Deprecated value of the vehicle is {deprecated_value}")

#Checking user entered data to calculate the depreciation slab
    if ve_data["Brand_of_vehicle"] in ["bmw","mercedes","tesla","jaguar"]:
        depreciation = 30
    elif ve_data["Brand_of_vehicle"] in ["toyota","nissan","mitsubishi","honda"]:
        depreciation = 20
    elif ve_data["Brand_of_vehicle"] in ["kia","hyundai","renault","ford"]:
        depreciation = 10
    
    current_vehicle_cost = deprecated_value - (ve_data["age_of_vehicle"] * (deprecated_value/depreciation))
    print(f"Current cost of vehicle is {current_vehicle_cost}")
#Checking user entered top speed data to calculate appropriate top speed added value to the insurance cost
    if ve_data["Top_speed"] >= 100 and ve_data["Top_speed"] < 140:
        top_speed_add = 0.02
    elif ve_data["Top_speed"] >= 140 and ve_data["Top_speed"] < 200:
        top_speed_add = 0.04
    elif ve_data["Top_speed"] > 200:
        top_speed_add = 0.06
    current_insurance = fixed_insur_cost + (current_vehicle_cost * top_speed_add)
    print(f"Insurance cost after considering top speed {current_insurance}")
##checking user entered accident data to give discount if no accidents and to add extra accident charges on to insurance cost
    if ve_data["accidents_last_year"] == 0:
        acc_insur_add = -0.10
    elif ve_data["accidents_last_year"] >= 1 and ve_data["accidents_last_year"] <=3:
        acc_insur_add = 0.15
    elif ve_data["accidents_last_year"] > 3:
        acc_insur_add = 0.30
    current_insurance = current_insurance + (acc_insur_add * current_insurance)
    print(f"Insurance cost considering number of accidents {current_insurance}")
#If the vehicle is 4wd then we shall check if the KM driven on offroad compared to total driver km is whether more than 40%, if yes then additional offroad insurance cost
    if ve_data["four_wd"] and (ve_data["Driving_pattern_km"][2]/sum(ve_data["Driving_pattern_km"]))*100 >= 40:
        Total_insurance_cost = current_insurance + (0.20* current_insurance)
        print(f"Insurance cost considering off road and excessive offroad KMs{Total_insurance_cost}")
        return Total_insurance_cost
    print(f"Insurance cost of the vehicle {current_insurance}")
    return current_insurance
    
brands = ["bmw","mercedes","tesla","jaguar","toyota","nissan","mitsubishi","honda","kia","hyundai","renault","ford"]
brand_of_v = input("Please enter brand of the vehicle. NOTE!!Only bmw,mercedes,tesla,jaguar,toyota,nissan,mitsubishi,honda,kia,hyundai,renault,ford accepted")
while brand_of_v not in brands:
    print("Please enter an accepted model")
    brand_of_v = input("Please enter brand of the vehicle. NOTE!!Only bmw,mercedes,tesla,jaguar,toyota,nissan,mitsubishi,honda,kia,hyundai,renault,ford accepted")

type_of_v = input("Is the vehicle 4 wheel drive or not (Y/N):")
if type_of_v == "y" or type_of_v == "Y":
    type_of_v = True
else:
    type_of_v = False

vehicle_data = {
    "Cost_of_new_vehicle": int(float(input("Enter cost of new vehicle:"))),
    "age_of_vehicle": int(float(input("Enter the age of vehicle as in number of years used:"))),
    "Brand_of_vehicle": brand_of_v,
    "mileage" : [float(input("Enter your city KM/L")),float(input("Enter your Highway KM/L")),float(input("Enter your offroad KM/L"))],
    "Driving_pattern_km" : [int(float(input("Enter your city KM"))),int(float(input("Enter your Highway KM"))),int(float(input("Enter your offroad KM")))],
    "accidents_last_year": int(float(input("Enter number of accidents encountered during the last 1 year:"))),
    "four_wd" : type_of_v,
    "Top_speed" : int(float(input("Enter the top speed of the vehicle:"))),
    "fuel_market_cost" : float(input("Enter the market price for fuel per litre"))

}

brand = vehicle_data["Brand_of_vehicle"]
age = vehicle_data["age_of_vehicle"]
Total_vehicle_expense = fuel_calc(vehicle_data) + Total_insurance_cost(vehicle_data)
print(f"Total expense for your {brand} of {age} years is {Total_vehicle_expense}")