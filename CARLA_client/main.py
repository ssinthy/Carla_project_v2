from vehicle_control import *
from road_info import monitor_odd
from scenario_info import get_scenario_info
import threading

def main():
    scenario_info = {
                "road_type": "Motorway",
                "ego_position": "Approaching Intersection",
                "emv_position": "Cross Road",
                "emv_travel_direction": "Approaches Intersection"
            }
    
    # Main execution
    carla_town, ego_vehicle_spwan_point, emv_spawn_point = get_scenario_info(scenario_info)
    
    client, world = initialize_carla(carla_town)
    ego_vehicle, emergency_vehicle = spawn_vehicle(world, client, ego_vehicle_spwan_point, emv_spawn_point)
    camera, sensor_data = setup_camera(world, ego_vehicle)

    threading.Thread(target=monitor_odd, args=[ego_vehicle, emergency_vehicle, world]).start()
    threading.Thread(target=set_spectator, args=[world, ego_vehicle]).start()
    # manual_control(world, ego_vehicle, sensor_data)

    # Cleanup
    # camera.stop()
    # ego_vehicle.destroy()

if __name__ == '__main__':
    main()