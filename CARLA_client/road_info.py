import carla
import time
import requests
import math
from odd import Taxonomy, OperationalDesignDomain

def calculate_distance(ego_vehicle_location, emv_vehicle_location):
    """Calculate the Euclidean distance between two locations."""
    dx = ego_vehicle_location.x - emv_vehicle_location.x
    dy = ego_vehicle_location.y - emv_vehicle_location.y
    dz = ego_vehicle_location.z - emv_vehicle_location.z
    return math.sqrt(dx**2 + dy**2 + dz**2)

def is_emv_in_same_directional_lane(waypoint1, waypoint2):
    """Check if two waypoints are in the same directional lane based on lane ID sign."""
    return ((waypoint1.lane_id < 0 and waypoint2.lane_id < 0) or
            (waypoint1.lane_id > 0 and waypoint2.lane_id > 0))

def get_odd_from_api(id):
    response = requests.get(f"http://127.0.0.1:5000/api/odd/{id}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get odd data. Status code: {response.status_code}")
        return None

def get_speed(vehicle):
    velocity = vehicle.get_velocity()
    # Calculate the magnitude of the velocity vector (speed)
    speed = math.sqrt(velocity.x**2 + velocity.y**2 + velocity.z**2)
    return speed

def monitor_odd(ego_vehicle, emergency_vehicle, world):
    if ego_vehicle is None:
        return    
    if emergency_vehicle is None:
        return
    map = world.get_map()

    # Fetch all ODDs from database and make odd objects
    odd_json = get_odd_from_api("667d781827704e647964a282")


    while True:
        time.sleep(0.5)
         # Get the current location of the vehicle
        ego_vehicle_location = ego_vehicle.get_location()
        emergency_vehicle_location = emergency_vehicle.get_location()
        # TODO: get road id
        # Get the road ID and check if it's a junction for ego vehicle
        waypoint_ego = map.get_waypoint(ego_vehicle_location)

        # Get the road ID and check if it's a junction for emv vehicle
        waypoint_emv = map.get_waypoint(emergency_vehicle_location)

        # Get ego vehicle velocity
        ego_vehicle_velocity = get_speed(ego_vehicle)

        # Get emergency vehicle velocity
        emergency_vehicle_velocity = get_speed(emergency_vehicle)

        emv_relative_pos = "on_other_road"

        if waypoint_emv.is_junction:
            emv_relative_pos = "on_junction"

        if waypoint_ego.road_id == waypoint_emv.road_id:
            # Check the condition and set lane_type if condition is true
            if is_emv_in_same_directional_lane(waypoint_ego, waypoint_emv):
                emv_relative_pos = "subject_lane"
            else:
                emv_relative_pos = "opposite_lane"

        distance_between_ego_and_emv = calculate_distance(ego_vehicle_location, emergency_vehicle_location)

        # Construct avdata from road info. Include all necessary information in avdata
        avdata = {
            Taxonomy.EGO_VEHICLE: {
                Taxonomy.SPEED: round(ego_vehicle_velocity, 2)
            },
            Taxonomy.EMERGENCY_VEHICLE: {
                Taxonomy.SPEED: round(emergency_vehicle_velocity, 2),
                Taxonomy.DISTANCE: round(distance_between_ego_and_emv, 2),
                Taxonomy.RELATIVE_POSITION: emv_relative_pos
            }
        }

        print(avdata)

        # Evaluate the avdata against ODD
        if not odd_json:
            continue
        
        odd = OperationalDesignDomain(odd_json=odd_json)

        is_within_odd = odd.check_within_odd(avdata)

        if is_within_odd:
            print("Inside ODD")
        else:
            print("Outside ODD")
            world.debug.draw_string(ego_vehicle_location, "Out of ODD", draw_shadow=False, color=carla.Color(255,0,0), life_time=0.5)
            bbox = ego_vehicle.bounding_box
            bbox.location += ego_vehicle.get_transform().location

            # Draw the bounding box
            world.debug.draw_box(bbox, ego_vehicle.get_transform().rotation, thickness=0.1, color=carla.Color(255, 0, 0, 0), life_time=0.5)
