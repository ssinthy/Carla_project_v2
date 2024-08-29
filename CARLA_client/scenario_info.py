def get_scenario_info(scenario_info):
    print(scenario_info)
    carla_town = "Town5"
    ego_vehicle_spwan_point = 0
    emv_spawn_point = 1
    
    print(scenario_info["road_type"])
    if scenario_info["road_type"] == "Motorway":
        carla_town = "Town05"
    elif scenario_info["road_type"] == "Expressway":
        carla_town = "Town05"
    elif scenario_info["road_type"] == "Local Road":
        carla_town = "Town01"
        
        
    if carla_town == "Town05":
        if scenario_info["ego_position"] == "Approaching Intersection":
            ego_vehicle_spwan_point = 108
        if scenario_info["emv_position"] == "Cross Road" and scenario_info["emv_travel_direction"] == "Approaches Intersection":
            emv_spawn_point = 56
            
    return carla_town, ego_vehicle_spwan_point, emv_spawn_point