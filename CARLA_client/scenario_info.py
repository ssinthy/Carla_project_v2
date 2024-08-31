def get_scenario_info(scenario_info):
    print(scenario_info)
    ego_vehicle_spwan_point = 0
    emv_spawn_point = 1
    
    '''
    if scenario_info["road_type"] == "Motorway":
        carla_town = "Town05"
    elif scenario_info["road_type"] == "Expressway":
        carla_town = "Town05"
    elif scenario_info["road_type"] == "Local Road":
        carla_town = "Town01"
    '''    
        
    if scenario_info["ego_position"] == "Approaching Intersection":
        ego_vehicle_spwan_point = 108
    elif scenario_info["ego_position"] == "Traffic Lane":
        ego_vehicle_spwan_point = 21
    
    if scenario_info["emv_position"] == "Cross Road" and scenario_info["emv_travel_direction"] == "Approaches Intersection":
        emv_spawn_point = 56
    elif scenario_info["emv_position"] == "Same Road" and scenario_info["emv_travel_direction"] == "Approaches from Behind":
        emv_spawn_point = 83
            
    return ego_vehicle_spwan_point, emv_spawn_point