from vehicle_control import *
from road_info import monitor_odd
import threading

def main():
    # Main execution
    client, world = initialize_carla()
    ego_vehicle, emergency_vehicle = spawn_vehicle(world, client)
    camera, sensor_data = setup_camera(world, ego_vehicle)

    threading.Thread(target=monitor_odd, args=[ego_vehicle, emergency_vehicle, world]).start()
    threading.Thread(target=set_spectator, args=[world, ego_vehicle]).start()
    # manual_control(world, ego_vehicle, sensor_data)

    # Cleanup
    # camera.stop()
    # ego_vehicle.destroy()

if __name__ == '__main__':
    main()